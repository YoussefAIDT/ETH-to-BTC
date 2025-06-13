import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from typing import Optional


def plot_predictions(y_true: np.ndarray, y_pred: np.ndarray, dates: Optional[np.ndarray] = None, 
                    title: str = "Prédictions vs Réalité"):
    """
    Affiche un graphique comparant les prédictions aux valeurs réelles
    
    Args:
        y_true: Valeurs réelles
        y_pred: Valeurs prédites
        dates: Dates correspondantes (optionnel)
        title: Titre du graphique
    """
    plt.figure(figsize=(12, 6))
    
    if dates is not None:
        plt.plot(dates, y_true, label='Prix BTC réel', color='blue', linewidth=2)
        plt.plot(dates, y_pred, label='Prix BTC prédit', color='red', linestyle='--', linewidth=2)
        plt.xticks(rotation=45)
    else:
        plt.plot(y_true, label='Prix BTC réel', color='blue', linewidth=2)
        plt.plot(y_pred, label='Prix BTC prédit', color='red', linestyle='--', linewidth=2)
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Date' if dates is not None else 'Échantillons')
    plt.ylabel('Prix BTC (USD)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_training_history(history):
    """
    Affiche l'historique d'entraînement
    
    Args:
        history: Historique retourné par model.fit()
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Loss
    ax1.plot(history.history['loss'], label='Train Loss')
    if 'val_loss' in history.history:
        ax1.plot(history.history['val_loss'], label='Validation Loss')
    ax1.set_title('Model Loss')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.legend()
    ax1.grid(True)
    
    # MAE (si disponible)
    if 'mae' in history.history:
        ax2.plot(history.history['mae'], label='Train MAE')
        if 'val_mae' in history.history:
            ax2.plot(history.history['val_mae'], label='Validation MAE')
        ax2.set_title('Model MAE')
        ax2.set_xlabel('Epoch')
        ax2.set_ylabel('MAE')
        ax2.legend()
        ax2.grid(True)
    
    plt.tight_layout()
    plt.show()


def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """
    Calcule les métriques de performance
    
    Args:
        y_true: Valeurs réelles
        y_pred: Valeurs prédites
        
    Returns:
        Dictionnaire avec les métriques
    """
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    mae = np.mean(np.abs(y_true - y_pred))
    
    return {
        'MSE': mse,
        'RMSE': rmse,
        'R²': r2,
        'MAE': mae
    }


def print_metrics(y_true: np.ndarray, y_pred: np.ndarray):
    """
    Affiche les métriques de performance
    """
    metrics = calculate_metrics(y_true, y_pred)
    
    print("\n" + "="*50)
    print("📊 ÉVALUATION DU MODÈLE")
    print("="*50)
    print(f"MSE  : {metrics['MSE']:,.2f}")
    print(f"RMSE : {metrics['RMSE']:,.2f}")
    print(f"MAE  : {metrics['MAE']:,.2f}")
    print(f"R²   : {metrics['R²']:.4f}")
    print("="*50)
