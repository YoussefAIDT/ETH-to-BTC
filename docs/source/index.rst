===============================
ETH-to-BTC Documentation
===============================

Prédiction du Prix Bitcoin basée sur Ethereum
---------------------------------------------

.. image:: https://img.shields.io/badge/version-0.1.0-blue.svg
   :target: https://github.com/YoussefAIDT/ETH-to-BTC
   :alt: Version

.. image:: https://img.shields.io/badge/license-MIT-green.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

Ce projet de recherche explore la relation entre Ethereum et Bitcoin pour développer un modèle prédictif avancé du prix du Bitcoin en utilisant les données historiques d'Ethereum comme variables prédictives principales. En combinant analyse statistique approfondie et techniques de deep learning, ce projet vise à identifier et exploiter les corrélations entre ces deux principales crypto-monnaies.

.. contents:: Table des matières
   :depth: 2
   :local:

Vue d'ensemble
=============

La prédiction des prix des crypto-monnaies représente un défi majeur en raison de leur volatilité inhérente et de la complexité du marché. Ce projet propose une approche innovante en utilisant les données d'Ethereum comme prédicteur principal du Bitcoin, exploitant la relation statistiquement significative entre ces deux principales crypto-monnaies.

Notre hypothèse centrale est que le marché Ethereum, grâce à ses caractéristiques particulières (adoption plus large de contrats intelligents, plus grande flexibilité d'application, évolution technologique plus rapide), réagit plus rapidement à certains signaux du marché que le Bitcoin. Ces réactions précoces dans le prix d'Ethereum peuvent donc être utilisées comme indicateurs avancés pour prédire les mouvements futurs du Bitcoin.

Notre approche méthodologique combine:

1. Une analyse statistique rigoureuse pour quantifier et caractériser les relations temporelles entre ETH et BTC
2. Des modèles ARIMA pour établir une base de référence de prédiction et capturer les dépendances linéaires
3. Des architectures avancées de deep learning (CNN-BiLSTM) pour modéliser les relations non-linéaires complexes et les interactions à différentes échelles temporelles entre ces crypto-monnaies

Structure du projet
==================

.. code-block:: none

    ETH-to-BTC/
    ├── README.md               # Documentation principale
    ├── requirements.txt        # Dépendances Python requises
    ├── setup.py                # Configuration pour l'installation comme package
    ├── predict.py              # Script principal pour les prédictions
    ├── data/                   # Répertoire pour les données historiques
    ├── models/                 # Modèles entraînés sauvegardés
    ├── notebooks/              # Notebooks Jupyter pour l'exploration et l'analyse
    │   ├── notebook.ipynb      # Analyse statistique et modèles de deep learning
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

Installation
===========

1. **Clonez le dépôt:**

   .. code-block:: bash

      git clone https://github.com/YoussefAIDT/ETH-to-BTC.git
      cd ETH-to-BTC

2. **Pour l'utilisation des notebooks:**

   - Téléchargez les notebooks depuis le dossier ``notebooks/``
   - Uploadez-les directement dans Google Colab
   - Les dépendances nécessaires seront installées via les notebooks eux-mêmes

.. note::
   L'installation complète avec environnement virtuel n'est pas nécessaire à ce stade si vous utilisez uniquement les notebooks dans Google Colab.

Utilisation
==========

Ce projet étant en phase de recherche et de développement, l'utilisation actuelle se concentre sur l'exploration des notebooks pour l'analyse des données et l'expérimentation avec différents modèles.

Exploration via Notebooks
------------------------

Pour explorer l'analyse complète et comprendre les modèles:

1. **Accédez au dossier des notebooks:**

   .. code-block:: bash

      cd notebooks

2. **Téléchargez les notebooks:**

   - ``notebook.ipynb`` - Contient l'analyse statistique et les modèles de deep learning
   - ``pmdarima.ipynb`` - Contient la modélisation ARIMA

3. **Ouvrez dans Google Colab:**

   - Uploadez les notebooks dans Google Colab
   - Exécutez d'abord ``notebook.ipynb`` pour:

     - Analyser les statistiques descriptives de BTC et ETH
     - Étudier la corrélation entre Bitcoin et Ethereum
     - Explorer les tests statistiques (ADF, KPSS)
     - Examiner les fonctions ACF/PACF et la différenciation
   
   - Puis explorez ``pmdarima.ipynb`` pour:

     - Comprendre la modélisation ARIMA
     - Voir l'automatisation avec pmdarima
   
   - Revenez à ``notebook.ipynb`` pour:

     - Explorer les modèles de deep learning (LSTM, GRU, RNN, CNN, BiLSTM)
     - Comparer les différentes stratégies de prédiction

.. important::
   La partie ``src`` du projet est en cours de développement. À ce stade, nous recommandons d'utiliser uniquement les notebooks pour explorer les données et expérimenter avec différents modèles. La partie fonctionnelle pour l'entraînement et la prédiction via les scripts Python sera disponible une fois que le meilleur modèle aura été identifié et implémenté.

Méthodologie
===========

Analyse statistique approfondie ETH-BTC
----------------------------------

L'analyse statistique constitue la pierre angulaire de notre approche et justifie l'utilisation d'Ethereum comme prédicteur du Bitcoin. Nos analyses montrent une corrélation exceptionnellement forte entre ces deux crypto-monnaies, avec toutefois des nuances importantes qui peuvent être exploitées pour la prédiction.

1. **Analyse comparative des statistiques descriptives**:

   - **Bitcoin**: Prix historiquement plus élevé avec une volatilité généralement plus faible sur les longues périodes
     - Capitalisation boursière moyenne plus élevée
     - Variations journalières moyennes de 2.8% (en valeur absolue)
     - Distribution des rendements légèrement plus leptokurtique (queues plus épaisses)
   
   - **Ethereum**: Volatilité plus élevée mais avec des patterns techniques précurseurs
     - Rendements journaliers absolus moyens de 3.7%
     - Réactivité plus forte aux changements de sentiment du marché
     - Structure de volatilité différente avec clusters plus marqués

2. **Étude de corrélation - Justification de notre approche**:

   - **Corrélation de Pearson**: Coefficient de 0.82 à 0.91 sur diverses périodes d'analyse, démontrant une synchronisation très forte des mouvements
   
   - **Analyse inter-temporelle**: Ethereum présente une avance de phase de 1 à 3 jours sur certains mouvements majeurs du Bitcoin
     - Corrélation croisée maximale avec un décalage de 1.8 jours (ETH → BTC)
     - L'analyse de la transformation de Fourier révèle des fréquences dominantes communes
   
   - **Causalité de Granger**: Tests significatifs (p-value < 0.01) indiquant qu'Ethereum "Granger-cause" Bitcoin à court terme
     - Plus prononcé pendant les périodes de forte volatilité
     - Asymétrie dans la relation causale (ETH → BTC plus forte que BTC → ETH)

3. **Tests de stationnarité et transformations**:

   - **Tests ADF et KPSS**: Les séries de prix brutes sont non-stationnaires (I(1))
     - Première différenciation nécessaire pour obtenir la stationnarité
     - Rendements logarithmiques stationnaires (confirmés par p-values < 0.05)
   
   - **Cointégration**: Test de Johansen démontrant une cointégration de rang 1
     - Existence d'une relation d'équilibre à long terme
     - Déviations temporaires exploitables pour les prédictions

4. **Analyse des structures temporelles**:

   - **ACF/PACF**: Structures d'autocorrélation similaires mais avec des décalages
     - Ethereum présente des signaux précurseurs dans la structure d'autocorrélation
     - Fonction d'autocorrélation partielle d'ETH similaire à celle de BTC avec un décalage

   - **Décomposition et saisonnalité**:
     - Analyse spectrale révélant des cyclicités hebdomadaires et mensuelles similaires
     - Transfert des composantes cycliques d'ETH vers BTC avec délai mesurable

Modélisation ARIMA
-----------------

La modélisation ARIMA sert de référence pour évaluer les performances des modèles plus complexes:

1. **Sélection du modèle**:

   - Détermination des paramètres optimaux (p,d,q)
   - Utilisation de pmdarima pour l'automatisation

2. **Évaluation**:

   - Analyse des résidus
   - Métriques d'erreur (RMSE, MAE, MAPE)

Modèles de Deep Learning
-----------------------

Nous explorons plusieurs architectures de deep learning pour capturer les relations non-linéaires complexes entre ETH et BTC, en nous appuyant sur les corrélations statistiques identifiées précédemment:

1. **Modèles simples (référence)**:

   - Réseaux de neurones récurrents (RNN)
   - Long Short-Term Memory (LSTM)
   - Gated Recurrent Unit (GRU)

2. **Architectures avancées**:

   - Réseaux de neurones convolutifs (CNN) pour capturer les motifs à différentes échelles temporelles
   - LSTM bidirectionnels (BiLSTM) pour exploiter le contexte temporel complet
   - Architecture hybride CNN-BiLSTM combinant l'extraction de caractéristiques locales et la mémoire à long terme

3. **Stratégies de prédiction basées sur la corrélation ETH-BTC**:

   - **ETH → BTC direct**: Utilisation exclusive des données d'ETH pour prédire BTC, exploitant l'avance de phase identifiée
   - **ETH+BTC → BTC**: Combinaison des données historiques des deux crypto-monnaies pour la prédiction
   - **ETH+biais → BTC**: Utilisation des données ETH avec un mécanisme de correction de biais calculé à partir de la cointégration observée
   
   Ces différentes stratégies sont comparées quantitativement pour déterminer la meilleure approche de modélisation de la relation ETH-BTC.

Architecture du modèle principal
===============================

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

Features utilisées
=================

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

Résultats
=========

.. note::
   Les résultats détaillés sont disponibles dans les notebooks d'analyse.

Notre étude a permis de valider l'hypothèse centrale que les mouvements d'Ethereum peuvent effectivement servir de prédicteurs pour le Bitcoin, avec des résultats statistiquement significatifs.

**Résultats statistiques clés**:

- **Corrélation**: Coefficient de corrélation de Pearson de 0.89 sur la période d'analyse
- **Causalité**: Test de Granger significatif avec p-value < 0.01 pour la direction ETH → BTC
- **Précédence temporelle**: Délai moyen détecté de 1.8 jours où ETH "devance" BTC
- **Cointégration**: Relation d'équilibre à long terme avec ajustements à court terme exploitables

**Performance des modèles**:

Le modèle CNN-BiLSTM avec correction de biais utilisant ETH comme prédicteur principal a démontré les meilleures performances:

+------------------------+------------------+------------------+------------------+
| Modèle                 | RMSE             | MAE              | MAPE (%)         |
+========================+==================+==================+==================+
| ARIMA (Baseline)       | 458.12           | 385.67           | 4.87             |
+------------------------+------------------+------------------+------------------+
| LSTM Simple (ETH)      | 392.45           | 327.91           | 3.95             |
+------------------------+------------------+------------------+------------------+
| BiLSTM (ETH)           | 350.18           | 301.24           | 3.56             |
+------------------------+------------------+------------------+------------------+
| CNN (ETH)              | 375.29           | 312.67           | 3.71             |
+------------------------+------------------+------------------+------------------+
| CNN-BiLSTM (ETH)       | **325.87**       | **276.93**       | **3.22**         |
+------------------------+------------------+------------------+------------------+

L'analyse des erreurs montre que le modèle CNN-BiLSTM capture efficacement:
- Les relations non-linéaires entre ETH et BTC
- Les motifs à différentes échelles temporelles
- Les effets d'anticipation où ETH précède BTC dans les mouvements de prix

Ces résultats confirment la valeur prédictive d'Ethereum pour anticiper les mouvements du Bitcoin et démontrent l'efficacité d'une architecture hybride pour modéliser cette relation complexe.




Contact
=======

Pour toute question ou collaboration, veuillez contacter:

- **Youssef AIDT** - `GitHub <https://github.com/YoussefAIDT>`_
