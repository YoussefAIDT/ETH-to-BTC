from keras.models import Sequential
from keras.layers import GRU, LSTM, Bidirectional, Conv1D, MaxPooling1D, Flatten, Dense, Dropout
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
import numpy as np


def build_gru_model(seq_length: int, units: int = 128, dropout: float = 0.1, learning_rate: float = 0.01):
    """
    Construit un modèle GRU pour la prédiction
    
    Args:
        seq_length: Longueur des séquences d'entrée
        units: Nombre d'unités dans la couche GRU
        dropout: Taux de dropout
        learning_rate: Taux d'apprentissage
        
    Returns:
        Modèle Keras compilé
    """
    model = Sequential()
    model.add(GRU(units=units, input_shape=(seq_length, 2)))
    model.add(Dropout(dropout))
    model.add(Dense(1))
    model.compile(optimizer=Adam(learning_rate=learning_rate), loss='mse')
    return model


def build_cnn_bilstm_model(seq_length: int, filters: int = 64, lstm_units: int = 50, dropout: float = 0.2):
    """
    Construit un modèle hybride CNN-BiLSTM
    
    Args:
        seq_length: Longueur des séquences d'entrée
        filters: Nombre de filtres pour les couches CNN
        lstm_units: Nombre d'unités LSTM
        dropout: Taux de dropout
        
    Returns:
        Modèle Keras compilé
    """
    model = Sequential()
    
    # Couches CNN
    model.add(Conv1D(filters=filters, kernel_size=3, activation='relu', input_shape=(seq_length, 2)))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Dropout(dropout))
    
    # Couches BiLSTM
    model.add(Bidirectional(LSTM(lstm_units, return_sequences=True)))
    model.add(Dropout(dropout))
    model.add(Bidirectional(LSTM(lstm_units)))
    model.add(Dropout(dropout))
    
    # Couche de sortie
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))
    
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])
    return model


def get_early_stopping(patience: int = 10):
    """
    Retourne un callback EarlyStopping
    """
    return EarlyStopping(monitor='val_loss', patience=patience, restore_best_weights=True)
