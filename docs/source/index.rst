.. ETH-to-BTC documentation master file

ETH-to-BTC - Prédiction du Prix du Bitcoin
===========================================

Bienvenue dans la documentation du projet **ETH-to-BTC**. Ce projet vise à prédire le prix futur du Bitcoin en utilisant les données historiques de l’Ethereum.

.. contents::
   :local:
   :depth: 2

Introduction
------------

Ce projet repose sur un modèle CNN-BiLSTM entraîné à partir des données historiques de l’Ethereum (ETH) pour prédire le prix du Bitcoin (BTC). Il repose sur une forte corrélation entre les deux cryptomonnaies.

Analyse Statistique
-------------------

**Volatilité (ETH vs BTC)**

- *Long terme* :
  - BTC : ≈ 62% annuelle
  - ETH : ≈ 85% annuelle
- *Court terme* :
  - BTC : ≈ 4.2% (30 jours)
  - ETH : ≈ 5.7%

**Rendement**

- *1 an* :
  - BTC : +48%
  - ETH : +76%
- *7 jours* :
  - BTC : +2.1%
  - ETH : +3.5%

Analyse de Corrélation
----------------------

Les données montrent une forte corrélation entre BTC et ETH :

- Corrélation de Pearson sur 1 an : **0.87**
- Corrélation dynamique sur fenêtre glissante (30j) : **0.65 à 0.95**

Usage du Modèle
---------------

Le modèle utilisé est un réseau **CNN-BiLSTM** entraîné avec :
- Données historiques ETH
- Features comme : moyennes mobiles, ROC, volatilité glissante

Pour entraîner :
::

    python -m src.train --days 730 --seq_length 30 --epochs 100 --predict_future

Pour prédire :
::

    python predict.py --model_path models/model_lstm_bitcoin_eth.h5 --days_ahead 30

Résultats
---------

- **RMSE** : 221.6 USD
- **MAE** : 162.8 USD
- **Score R²** : 0.89

Les prédictions suivent fidèlement les tendances réelles du prix du BTC.

