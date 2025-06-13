# ETH-to-BTC: Prédiction du Prix Bitcoin basée sur Ethereum

Ce projet de recherche explore la relation entre Ethereum et Bitcoin pour développer un modèle prédictif avancé du prix du Bitcoin en utilisant les données historiques d'Ethereum comme variables prédictives principales. En combinant analyse statistique approfondie et techniques de deep learning, ce projet vise à identifier et exploiter les corrélations entre ces deux principales crypto-monnaies.

## 📋 Table des matières

- [Vue d'ensemble](#vue-densemble)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
  - [Exploration via Notebooks](#exploration-via-notebooks)
  - [Entraînement d'un nouveau modèle](#entraînement-dun-nouveau-modèle)
  - [Prédiction avec un modèle existant](#prédiction-avec-un-modèle-existant)
- [Méthodologie](#méthodologie)
  - [Analyse statistique](#analyse-statistique)
  - [Modélisation ARIMA](#modélisation-arima)
  - [Modèles de Deep Learning](#modèles-de-deep-learning)
- [Architecture du modèle principal](#architecture-du-modèle-principal)
- [Features utilisées](#features-utilisées)
- [Résultats](#résultats)
- [Licence](#licence)
- [Contact](#contact)

## Vue d'ensemble

La prédiction des prix des crypto-monnaies représente un défi majeur en raison de leur volatilité inhérente. Ce projet propose une approche innovante en utilisant les données d'Ethereum comme prédicteur principal du Bitcoin, exploitant les relations et corrélations entre ces deux actifs. Notre méthodologie combine:

1. Une analyse statistique rigoureuse pour comprendre les relations temporelles
2. Des modèles ARIMA pour établir une base de référence de prédiction
3. Des architectures avancées de deep learning (CNN-BiLSTM) pour capturer les patterns complexes

## Structure du projet

```
ETH-to-BTC/
├── README.md               # Documentation principale
├── requirements.txt        # Dépendances Python requises
├── setup.py                # Configuration pour l'installation comme package
├── predict.py              # Script principal pour les prédictions
├── data/                   # Répertoire pour les données historiques
├── models/                 # Modèles entraînés sauvegardés
├── notebooks/              # Notebooks Jupyter pour l'exploration et l'analyse
│   ├── Analyse_Statistique_Corrélation_Choix_Modèle.ipynb      # Analyse statistique et modèles de deep learning
│   └── pmdarima.ipynb      # Modélisation avec ARIMA/pmdarima
└── src/                    # Code source principal
    ├── __init__.py
    ├── data/               # Module pour la collecte et gestion des données
    │   ├── __init__.py
    │   └── collector.py    # Récupération des données historiques
    ├── features/           # Module pour le prétraitement des features
    │   ├── __init__.py
    │   └── preprocessing.py # Traitement et création de features
    ├── models/             # Implémentations des modèles
    │   ├── __init__.py
    │   └── cnn_bilstm.py   # Architecture du modèle hybride CNN-BiLSTM
    ├── utils/              # Fonctions utilitaires
    │   ├── __init__.py
    │   └── visualization.py # Outils de visualisation des résultats
    └── train.py            # Script d'entraînement des modèles
```

## Installation

1. **Clonez le dépôt:**
   ```bash
   git clone https://github.com/YoussefAIDT/ETH-to-BTC.git
   cd ETH-to-BTC
   ```

2. **Pour l'utilisation des notebooks:**
   - Téléchargez les notebooks depuis le dossier `notebooks/`
   - Uploadez-les directement dans Google Colab
   - Les dépendances nécessaires seront installées via les notebooks eux-mêmes

> **Note:** L'installation complète avec environnement virtuel n'est pas nécessaire à ce stade si vous utilisez uniquement les notebooks dans Google Colab.

## Utilisation

Ce projet étant en phase de recherche et de développement, l'utilisation actuelle se concentre sur l'exploration des notebooks pour l'analyse des données et l'expérimentation avec différents modèles.

### Exploration via Notebooks

Pour explorer l'analyse complète et comprendre les modèles:

1. **Accédez au dossier des notebooks:**
   ```bash
   cd notebooks
   ```

2. **Téléchargez les notebooks:**
   - `Analyse_Statistique_Corrélation_Choix_Modèle.ipynb` - Contient l'analyse statistique et les modèles de deep learning
   - `pmdarima.ipynb` - Contient la modélisation ARIMA

3. **Ouvrez dans Google Colab:**
   - Uploadez les notebooks dans Google Colab
   - Exécutez d'abord `Analyse_Statistique_Corrélation_Choix_Modèle.ipynb` pour:
     - Analyser les statistiques descriptives de BTC et ETH
     - Étudier la corrélation entre Bitcoin et Ethereum
     - Explorer les tests statistiques (ADF, KPSS)
     - Examiner les fonctions ACF/PACF et la différenciation
   
   - Puis explorez `pmdarima.ipynb` pour:
     - Comprendre la modélisation ARIMA
     - Voir l'automatisation avec pmdarima
   
   - Revenez à `Analyse_Statistique_Corrélation_Choix_Modèle.ipynb` pour:
     - Explorer les modèles de deep learning (LSTM, GRU, RNN, CNN, BiLSTM)
     - Comparer les différentes stratégies de prédiction

> **Note importante:** La partie `src` du projet est en cours de développement. À ce stade, nous recommandons d'utiliser uniquement les notebooks pour explorer les données et expérimenter avec différents modèles. La partie fonctionnelle pour l'entraînement et la prédiction via les scripts Python sera disponible une fois que le meilleur modèle aura été identifié et implémenté.

## Méthodologie

### Analyse statistique

L'analyse statistique constitue le socle de notre approche et comprend:

1. **Analyse descriptive**:
   - Statistiques des rendements et prix de BTC et ETH
   - Analyse de la volatilité historique

2. **Étude de corrélation**:
   - Corrélation de Pearson entre BTC et ETH
   - Corrélation croisée avec différents décalages temporels
   - Analyse de la causalité de Granger

3. **Tests de stationnarité**:
   - Test Augmented Dickey-Fuller (ADF)
   - Test Kwiatkowski-Phillips-Schmidt-Shin (KPSS)

4. **Analyse des séries temporelles**:
   - Fonctions d'autocorrélation (ACF)
   - Fonctions d'autocorrélation partielle (PACF)
   - Techniques de différenciation pour obtenir la stationnarité

### Modélisation ARIMA

La modélisation ARIMA sert de référence pour évaluer les performances des modèles plus complexes:

1. **Sélection du modèle**:
   - Détermination des paramètres optimaux (p,d,q)
   - Utilisation de pmdarima pour l'automatisation

2. **Évaluation**:
   - Analyse des résidus
   - Métriques d'erreur (RMSE, MAE, MAPE)

### Modèles de Deep Learning

Plusieurs architectures de deep learning sont explorées pour capturer les relations complexes:

1. **Modèles simples**:
   - Réseaux de neurones récurrents (RNN)
   - Long Short-Term Memory (LSTM)
   - Gated Recurrent Unit (GRU)

2. **Architectures avancées**:
   - Réseaux de neurones convolutifs (CNN)
   - LSTM bidirectionnels (BiLSTM)
   - Architecture hybride CNN-BiLSTM

3. **Stratégies de prédiction**:
   - Prédiction de BTC à partir d'ETH uniquement
   - Prédiction de BTC à partir de BTC et ETH combinés
   - Prédiction de BTC à partir d'ETH avec correction de biais

## Architecture du modèle principal

Notre modèle hybride CNN-BiLSTM combine les avantages des réseaux convolutifs et récurrents:

1. **Couches convolutives**:
   - Extraction des caractéristiques locales et des motifs à court terme
   - Réduction du bruit dans les séries temporelles

2. **Couches BiLSTM**:
   - Capture des dépendances à long terme dans les deux directions temporelles
   - Prise en compte du contexte complet des séquences

3. **Techniques de régularisation**:
   - Dropout pour éviter le surapprentissage
   - Régularisation L1-L2 pour améliorer la généralisation

4. **Mécanisme de correction de biais**:
   - Ajustement des prédictions basé sur l'analyse statistique
   - Compensation des décalages systématiques entre ETH et BTC

## Features utilisées

Le modèle exploite diverses caractéristiques d'Ethereum pour prédire le Bitcoin:

1. **Métriques de prix**:
   - Prix de clôture journalier
   - Moyennes mobiles (7, 14, 30 jours)
   - Amplitude quotidienne (High-Low)

2. **Indicateurs de volatilité**:
   - Volatilité sur 7 jours (écart-type des rendements)
   - Ratio volume/prix (indicateur de la pression du marché)

3. **Indicateurs techniques**:
   - Rate of Change (5 et 10 jours)
   - Indicateurs de momentum (5 et 10 jours)
   - Rendements quotidiens logarithmiques

4. **Features dérivées**:
   - Différences entre les moyennes mobiles
   - Ratios de volatilité
   - Métriques de tendance

## Résultats

*Note: Les résultats détaillés sont disponibles dans les notebooks d'analyse.*

Le modèle CNN-BiLSTM avec correction de biais a démontré les meilleures performances prédictives, surpassant les modèles ARIMA classiques et les architectures de deep learning plus simples. Les métriques clés incluent:

- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)
- MAPE (Mean Absolute Percentage Error)
- Coefficient de détermination (R²)


## Contact

Pour toute question ou collaboration, veuillez contacter:

- **Youssef AIDT** - [GitHub](https://github.com/YoussefAIDT)
