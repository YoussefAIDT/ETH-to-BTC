import pandas as pd
import requests
import numpy as np
from typing import Optional, Tuple


def collect_data_crypto_compare(crypto_symbol: str, start_timestamp: int, end_timestamp: int) -> Optional[pd.DataFrame]:
    """
    Collecte les données historiques depuis CryptoCompare API
    
    Args:
        crypto_symbol: Symbole de la cryptomonnaie (ex: 'BTC', 'ETH')
        start_timestamp: Timestamp de début
        end_timestamp: Timestamp de fin
        
    Returns:
        DataFrame avec les données historiques ou None si erreur
    """
    url = f'https://min-api.cryptocompare.com/data/v2/histoday'
    params = {
        'fsym': crypto_symbol,
        'tsym': 'USD',
        'limit': 2000,
        'toTs': end_timestamp,
        'extraParams': 'crypto_prediction'
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()['Data']['Data']
            df = pd.DataFrame(data)
            df['time'] = pd.to_datetime(df['time'], unit='s')
            return df
        else:
            print(f"Erreur lors de la récupération des données : {response.status_code}")
            return None
    except Exception as e:
        print(f"Erreur lors de la récupération des données: {e}")
        return None


def preprocess_data(btc_df: pd.DataFrame, eth_df: pd.DataFrame) -> pd.DataFrame:
    """
    Prétraite et combine les données BTC et ETH
    
    Args:
        btc_df: DataFrame avec les données Bitcoin
        eth_df: DataFrame avec les données Ethereum
        
    Returns:
        DataFrame combiné et prétraité
    """
    # Fusion des données sur la colonne time
    df = pd.merge(btc_df[['time', 'close']], eth_df[['time', 'close']], 
                  on='time', suffixes=('_btc', '_eth'))
    
    # Tri par date
    df = df.sort_values('time')
    
    # Calcul des rendements
    df['btc_return'] = df['close_btc'].pct_change()
    df['eth_return'] = df['close_eth'].pct_change()
    
    # Suppression des valeurs manquantes
    df.dropna(inplace=True)
    
    return df
