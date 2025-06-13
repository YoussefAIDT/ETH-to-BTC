import numpy as np
from sklearn.preprocessing import MinMaxScaler
from typing import Tuple, List


def create_sequences(eth_prices: np.ndarray, btc_prices: np.ndarray, seq_length: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Crée des séquences temporelles pour l'entraînement
    
    Args:
        eth_prices: Prix Ethereum
        btc_prices: Prix Bitcoin
        seq_length: Longueur de la séquence
        
    Returns:
        Tuple (X, y) avec les séquences d'entrée et les targets
    """
    X, y = [], []
    for i in range(len(eth_prices) - seq_length):
        X.append(np.column_stack((eth_prices[i:i+seq_length], btc_prices[i:i+seq_length])))
        y.append(btc_prices[i+seq_length])
    return np.array(X), np.array(y)


def scale_data(data: np.ndarray) -> Tuple[np.ndarray, MinMaxScaler]:
    """
    Normalise les données avec MinMaxScaler
    
    Args:
        data: Données à normaliser
        
    Returns:
        Tuple (données normalisées, scaler)
    """
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data.reshape(-1, 1))
    return scaled_data.flatten(), scaler


def prepare_training_data(df, seq_length: int = 32) -> Tuple[np.ndarray, np.ndarray, MinMaxScaler, MinMaxScaler]:
    """
    Prépare les données pour l'entraînement
    
    Args:
        df: DataFrame avec les données
        seq_length: Longueur des séquences
        
    Returns:
        Tuple (X, y, eth_scaler, btc_scaler)
    """
    # Scaling
    eth_scaled, eth_scaler = scale_data(df['close_eth'].values)
    btc_scaled, btc_scaler = scale_data(df['close_btc'].values)
    
    # Création des séquences
    X, y = create_sequences(eth_scaled, btc_scaled, seq_length)
    X = X.reshape((X.shape[0], X.shape[1], 2))
    
    return X, y, eth_scaler, btc_scaler
