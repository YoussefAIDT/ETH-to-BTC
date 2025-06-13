#!/usr/bin/env python3
"""
Script d'entraînement principal pour les modèles de prédiction Bitcoin
Utilise la structure modulaire du projet
"""

import os
import time
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split

# Imports des modules du projet
from data.collector import collect_data_crypto_compare, preprocess_data
from features.preprocessing import prepare_training_data
from models.cnn_bilstm import build_gru_model, build_cnn_bilstm_model, get_early_stopping
from utils.visualization import plot_predictions, plot_training_history, print_metrics


def train_gru_model(data, seq_length=32, units=128, dropout=0.1, learning_rate=0.01, 
                   validation_split=0.2, epochs=100, batch_size=32):
    """
    Entraîne un modèle GRU pour la prédiction du prix Bitcoin
    
    Args:
        data: DataFrame avec les données prétraitées
        seq_length: Longueur des séquences
        units: Nombre d'unités GRU
        dropout: Taux de dropout
        learning_rate: Taux d'apprentissage
        validation_split: Proportion des données pour la validation
        epochs: Nombre d'epochs
        batch_size: Taille des batches
    
    Returns:
        Tuple (model, history, metrics)
    """
    print("🚀 Début de l'entraînement du modèle GRU...")
    
    # Préparation des données
    X, y, eth_scaler, btc_scaler = prepare_training_data(data, seq_length)
    
    # Division train/test
    train_size = int(len(X) * (1 - validation_split))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    print(f"📊 Données d'entraînement: {len(X_train)} échantillons")
    print(f"📊 Données de test: {len(X_test)} échantillons")
    
    # Construction du modèle
    model = build_gru_model(seq_length, units, dropout, learning_rate)
    early_stop = get_early_stopping(patience=15)
    
    print("🏗️ Architecture du modèle:")
    model.summary()
    
    # Entraînement
    print("\n🎯 Début de l'entraînement...")
    start_time = time.time()
    
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.2,
        callbacks=[early_stop],
        verbose=1
    )
    
    training_time = time.time() - start_time
    print(f"⏱️ Temps d'entraînement: {training_time:.2f} secondes")
    
    # Prédictions et évaluation
    print("\n🔍 Évaluation du modèle...")
    y_pred = model.predict(X_test, verbose=0)
    
    # Dé-normalisation
    y_test_inv = btc_scaler.inverse_transform(y_test.reshape(-1, 1)).flatten()
    y_pred_inv = btc_scaler.inverse_transform(y_pred).flatten()
    
    # Métriques
    print_metrics(y_test_inv, y_pred_inv)
    
    # Visualisations
    test_dates = data['time'].iloc[-len(y_test):].values
    plot_predictions(y_test_inv, y_pred_inv, test_dates, "Prédiction GRU - Prix Bitcoin")
    plot_training_history(history)
    
    return model, history, (y_test_inv, y_pred_inv)


def train_cnn_bilstm_model(data, seq_length=32, filters=64, lstm_units=50, dropout=0.2, 
                          validation_split=0.2, epochs=100, batch_size=32):
    """
    Entraîne un modèle CNN-BiLSTM pour la prédiction du prix Bitcoin
    
    Args:
        data: DataFrame avec les données prétraitées
        seq_length: Longueur des séquences
        filters: Nombre de filtres CNN
        lstm_units: Nombre d'unités LSTM
        dropout: Taux de dropout
        validation_split: Proportion des données pour la validation
        epochs: Nombre d'epochs
        batch_size: Taille des batches
    
    Returns:
        Tuple (model, history, metrics)
    """
    print("🚀 Début de l'entraînement du modèle CNN-BiLSTM...")
    
    # Préparation des données
    X, y, eth_scaler, btc_scaler = prepare_training_data(data, seq_length)
    
    # Division train/test
    train_size = int(len(X) * (1 - validation_split))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    print(f"📊 Données d'entraînement: {len(X_train)} échantillons")
    print(f"📊 Données de test: {len(X_test)} échantillons")
    
    # Construction du modèle
    model = build_cnn_bilstm_model(seq_length, filters, lstm_units, dropout)
    early_stop = get_early_stopping(patience=20)
    
    print("🏗️ Architecture du modèle:")
    model.summary()
    
    # Entraînement
    print("\n🎯 Début de l'entraînement...")
    start_time = time.time()
    
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.2,
        callbacks=[early_stop],
        verbose=1
    )
    
    training_time = time.time() - start_time
    print(f"⏱️ Temps d'entraînement: {training_time:.2f} secondes")
    
    # Prédictions et évaluation
    print("\n🔍 Évaluation du modèle...")
    y_pred = model.predict(X_test, verbose=0)
    
    # Dé-normalisation
    y_test_inv = btc_scaler.inverse_transform(y_test.reshape(-1, 1)).flatten()
    y_pred_inv = btc_scaler.inverse_transform(y_pred).flatten()
    
    # Métriques
    print_metrics(y_test_inv, y_pred_inv)
    
    # Visualisations
    test_dates = data['time'].iloc[-len(y_test):].values
    plot_predictions(y_test_inv, y_pred_inv, test_dates, "Prédiction CNN-BiLSTM - Prix Bitcoin")
    plot_training_history(history)
    
    return model, history, (y_test_inv, y_pred_inv)


def compare_models(data):
    """
    Compare les performances des différents modèles
    
    Args:
        data: DataFrame avec les données prétraitées
    """
    print("\n" + "="*60)
    print("🏆 COMPARAISON DES MODÈLES")
    print("="*60)
    
    models_results = []
    
    # Entraînement GRU
    print("\n1️⃣ Entraînement du modèle GRU...")
    gru_model, gru_history, gru_predictions = train_gru_model(data)
    models_results.append(("GRU", gru_model, gru_predictions))
    
    # Sauvegarde GRU
    gru_model.save("../models/gru_model.h5")
    print("✅ Modèle GRU sauvegardé: models/gru_model.h5")
    
    # Entraînement CNN-BiLSTM
    print("\n2️⃣ Entraînement du modèle CNN-BiLSTM...")
    cnn_model, cnn_history, cnn_predictions = train_cnn_bilstm_model(data)
    models_results.append(("CNN-BiLSTM", cnn_model, cnn_predictions))
    
    # Sauvegarde CNN-BiLSTM
    cnn_model.save("../models/cnn_bilstm_model.h5")
    print("✅ Modèle CNN-BiLSTM sauvegardé: models/cnn_bilstm_model.h5")
    
    # Comparaison finale
    print("\n" + "="*60)
    print("📊 RÉSULTATS FINAUX")
    print("="*60)
    
    best_model = None
    best_r2 = -float('inf')
    best_model_name = ""
    
    for model_name, model, (y_true, y_pred) in models_results:
        from utils.visualization import calculate_metrics
        metrics = calculate_metrics(y_true, y_pred)
        
        print(f"\n🤖 {model_name}:")
        print(f"   RMSE: ${metrics['RMSE']:,.2f}")
        print(f"   R²:   {metrics['R²']:.4f}")
        print(f"   MAE:  ${metrics['MAE']:,.2f}")
        
        if metrics['R²'] > best_r2:
            best_r2 = metrics['R²']
            best_model = model
            best_model_name = model_name
    
    # Sauvegarde du meilleur modèle
    print(f"\n🏆 Le meilleur modèle est: {best_model_name} (R² = {best_r2:.4f})")
    best_model.save("../models/best_model.h5")
    print("✅ Meilleur modèle sauvegardé: models/best_model.h5")
    
    return models_results, best_model, best_model_name


def main():
    """
    Fonction principale d'exécution du script d'entraînement
    """
    print("🚀 DÉMARRAGE DU SCRIPT D'ENTRAÎNEMENT BITCOIN")
    print("="*60)
    
    # Collecte des données
    print("\n📡 Collecte des données...")
    btc_data = collect_data_crypto_compare('BTC', days=365)
    eth_data = collect_data_crypto_compare('ETH', days=365)
    
    if btc_data is None or eth_data is None:
        print("❌ Erreur lors de la collecte des données")
        return
    
    print(f"✅ Données BTC collectées: {len(btc_data)} jours")
    print(f"✅ Données ETH collectées: {len(eth_data)} jours")
    
    # Prétraitement des données
    print("\n🔧 Prétraitement des données...")
    combined_data = preprocess_data(btc_data, eth_data)
    
    if combined_data is None:
        print("❌ Erreur lors du prétraitement des données")
        return
    
    print(f"✅ Données prétraitées: {len(combined_data)} échantillons")
    
    # Créer le dossier models s'il n'existe pas
    os.makedirs("../models", exist_ok=True)
    
    # Comparaison des modèles
    models_results, best_model, best_model_name = compare_models(combined_data)
    
    # Résumé final
    print("\n" + "="*60)
    print("🎉 ENTRAÎNEMENT TERMINÉ AVEC SUCCÈS!")
    print("="*60)
    print(f"🏆 Meilleur modèle: {best_model_name}")
    print(f"📁 Modèles sauvegardés dans: ../models/")
    print(f"📊 Nombre total de modèles entraînés: {len(models_results)}")
    
    # Affichage des prochaines étapes
    print("\n💡 PROCHAINES ÉTAPES:")
    print("   1. Utilisez le meilleur modèle pour faire des prédictions")
    print("   2. Testez les modèles avec de nouvelles données")
    print("   3. Déployez l'application Streamlit avec app.py")
    print("   4. Surveillez les performances en temps réel")
    
    print(f"\n⏰ Script terminé à: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Entraînement interrompu par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")
        import traceback
        traceback.print_exc()
