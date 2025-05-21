import requests
import pandas as pd
import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, Bidirectional, Conv1D, MaxPooling1D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.regularizers import l1_l2

# =========================
# Récupération des données
# =========================

def collect_data_crypto_compare(symbol, start_timestamp, end_timestamp):
    url = 'https://min-api.cryptocompare.com/data/v2/histoday'
    days = (end_timestamp - start_timestamp) // (24 * 3600) + 1
    limit = min(2000, days)

    params = {
        'fsym': symbol,
        'tsym': 'USD',
        'limit': limit,
        'toTs': end_timestamp
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'Success':
            df = pd.DataFrame(data['Data']['Data'])
            df['time'] = pd.to_datetime(df['time'], unit='s')
            return df
        else:
            print(f"Erreur API: {data['Message']}")
            return None
    else:
        print(f"Erreur HTTP: {response.status_code}")
        return None

# =========================================
# Prétraitement des données + features ETH
# =========================================

def preprocess_data(btc_df, eth_df):
    df = pd.merge(btc_df[['time', 'close', 'high', 'low', 'volumefrom', 'volumeto']],
                  eth_df[['time', 'close', 'high', 'low', 'volumefrom', 'volumeto']],
                  on='time',
                  suffixes=('_btc', '_eth'))
    df = df.sort_values('time')

    df['eth_ma7'] = df['close_eth'].rolling(window=7).mean()
    df['eth_ma14'] = df['close_eth'].rolling(window=14).mean()
    df['eth_ma30'] = df['close_eth'].rolling(window=30).mean()
    df['eth_volatility7'] = df['close_eth'].rolling(window=7).std()
    df['eth_daily_range'] = df['high_eth'] - df['low_eth']
    df['eth_volume_price_ratio'] = df['volumeto_eth'] / df['close_eth']
    df['eth_roc5'] = df['close_eth'].pct_change(periods=5)
    df['eth_roc10'] = df['close_eth'].pct_change(periods=10)
    df['btc_return'] = df['close_btc'].pct_change()
    df['eth_return'] = df['close_eth'].pct_change()
    df['eth_momentum5'] = df['close_eth'] / df['close_eth'].shift(5)
    df['eth_momentum10'] = df['close_eth'] / df['close_eth'].shift(10)

    df.dropna(inplace=True)
    return df

# =====================
# Séquences X/y
# =====================

def create_sequences(df, seq_length=30):
    features_list = [
        'close_eth', 'eth_ma7', 'eth_ma14', 'eth_ma30',
        'eth_volatility7', 'eth_daily_range', 'eth_volume_price_ratio',
        'eth_roc5', 'eth_roc10', 'eth_momentum5', 'eth_momentum10', 'eth_return'
    ]
    target = 'close_btc'
    X, y = [], []
    for i in range(len(df) - seq_length):
        feature_sequence = df[features_list].iloc[i:i+seq_length].values
        X.append(feature_sequence)
        y.append(df[target].iloc[i+seq_length])
    return np.array(X), np.array(y).reshape(-1, 1)

# ====================
# Modèle CNN-BiLSTM
# ====================

def build_simple_rnn_model(seq_length, features=12):
    model = Sequential([
        Conv1D(filters=64, kernel_size=3, activation='relu', padding='same', input_shape=(seq_length, features)),
        MaxPooling1D(pool_size=2),
        Dropout(0.2),
        Conv1D(filters=128, kernel_size=3, activation='relu', padding='same'),
        MaxPooling1D(pool_size=2),
        Dropout(0.2),
        Bidirectional(LSTM(128, return_sequences=True, kernel_regularizer=l1_l2(l1=1e-5, l2=1e-4))),
        Dropout(0.3),
        LSTM(128, return_sequences=False, kernel_regularizer=l1_l2(l1=1e-5, l2=1e-4)),
        Dropout(0.3),
        Dense(64, activation='relu', kernel_regularizer=l1_l2(l1=1e-5, l2=1e-4)),
        Dense(32, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])
    return model

# ========================
# Entraînement + Analyse
# ========================

def main(bitcoin_data, ethereum_data):
    if bitcoin_data is None or ethereum_data is None:
        print("Erreur de récupération des données.")
        return None

    data = preprocess_data(bitcoin_data, ethereum_data)

    feature_scaler = MinMaxScaler()
    btc_scaler = MinMaxScaler()

    features_list = [
        'close_eth', 'eth_ma7', 'eth_ma14', 'eth_ma30',
        'eth_volatility7', 'eth_daily_range', 'eth_volume_price_ratio',
        'eth_roc5', 'eth_roc10', 'eth_momentum5', 'eth_momentum10', 'eth_return'
    ]

    data[features_list] = feature_scaler.fit_transform(data[features_list])
    data['close_btc'] = btc_scaler.fit_transform(data[['close_btc']])

    seq_length = 30
    X, y = create_sequences(data, seq_length)

    train_size = int(len(X) * 0.7)
    val_size = int(len(X) * 0.15)
    X_train, X_val, X_test = X[:train_size], X[train_size:train_size+val_size], X[train_size+val_size:]
    y_train, y_val, y_test = y[:train_size], y[train_size:train_size+val_size], y[train_size+val_size:]

    model = build_simple_rnn_model(seq_length, features=len(features_list))

    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True, verbose=1)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=0.00005, verbose=1)

    history = model.fit(X_train, y_train, epochs=100, batch_size=32,
                        validation_data=(X_val, y_val),
                        callbacks=[early_stopping, reduce_lr], verbose=1)

    y_pred = model.predict(X_test)
    y_test_btc = btc_scaler.inverse_transform(y_test)
    y_pred_btc = btc_scaler.inverse_transform(y_pred)

    mse = mean_squared_error(y_test_btc, y_pred_btc)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test_btc, y_pred_btc)

    print(f"MSE: {mse:.2f}, RMSE: {rmse:.2f}, R²: {r2:.4f}")

    bias = np.mean(y_test_btc - y_pred_btc)
    y_pred_btc_corrected = y_pred_btc + bias

    mse_corrected = mean_squared_error(y_test_btc, y_pred_btc_corrected)
    rmse_corrected = np.sqrt(mse_corrected)
    r2_corrected = r2_score(y_test_btc, y_pred_btc_corrected)

    print(f"Après correction : MSE = {mse_corrected:.2f}, RMSE = {rmse_corrected:.2f}, R² = {r2_corrected:.4f}")

    test_dates = data['time'].iloc[-len(y_test):].values

    plt.figure(figsize=(12, 6))
    plt.plot(test_dates, y_test_btc, label='Réel', color='blue')
    plt.plot(test_dates, y_pred_btc, label='Prédit (non corrigé)', color='red', linestyle='--')
    plt.plot(test_dates, y_pred_btc_corrected, label='Prédit (corrigé)', color='green', linestyle='-.')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return model, feature_scaler, btc_scaler, bias, X, data

# =======================
# Prédiction future
# =======================

def predict_future_price(model, feature_scaler, btc_scaler, bias, last_sequence, days_ahead=30):
    predictions = []
    current_sequence = last_sequence.copy()

    for _ in range(days_ahead):
        pred = model.predict(current_sequence.reshape(1, current_sequence.shape[0], current_sequence.shape[1]))
        pred_btc = btc_scaler.inverse_transform(pred)[0][0]
        pred_btc_corrected = pred_btc + bias
        predictions.append(pred_btc_corrected)

    return predictions

# ======================
# Lancement du script
# ======================

if __name__ == "__main__":
    end_timestamp = int(time.time())
    start_timestamp = end_timestamp - (2 * 365 * 24 * 3600)

    btc_data = collect_data_crypto_compare('BTC', start_timestamp, end_timestamp)
    eth_data = collect_data_crypto_compare('ETH', start_timestamp, end_timestamp)

    results = main(btc_data, eth_data)

    if results:
        model, feature_scaler, btc_scaler, bias, X, data = results
        last_sequence = X[-1]
        future_predictions = predict_future_price(model, feature_scaler, btc_scaler, bias, last_sequence, days_ahead=30)

        print("\nPrévisions des 30 prochains jours :")
        for i, price in enumerate(future_predictions, 1):
            print(f"Jour {i}: {price:.2f} USD")
