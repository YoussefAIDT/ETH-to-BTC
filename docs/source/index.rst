===============================
ETH-to-BTC Documentation
===============================

.. raw:: html

   <div style="text-align: center; margin: 30px 0;">
      <img src="https://img.shields.io/badge/version-0.1.0-blue.svg" alt="Version" style="margin: 5px;">
      <img src="https://img.shields.io/badge/python-3.8+-orange.svg" alt="Python" style="margin: 5px;">
      <img src="https://img.shields.io/badge/TensorFlow-2.0+-red.svg" alt="TensorFlow" style="margin: 5px;">
   </div>

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px; border-radius: 15px; color: white; text-align: center; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
      <h2 style="margin: 0; font-size: 2.5em; font-weight: bold;"> Prédiction Bitcoin avec Ethereum</h2>
      <p style="font-size: 1.2em; margin: 20px 0; opacity: 0.9;">Modèle prédictif avancé utilisant les corrélations temporelles ETH-BTC</p>
   </div>

Vue d'ensemble
==============

.. raw:: html

   <div style="background: #f8f9fa; padding: 25px; border-left: 5px solid #007bff; margin: 20px 0; border-radius: 0 10px 10px 0;">

Ce projet de recherche révolutionnaire explore la relation symbiotique entre **Ethereum** et **Bitcoin** pour développer un modèle prédictif de nouvelle génération. En combinant analyse statistique rigoureuse et techniques de deep learning avancées, nous dévoilons les patterns cachés qui régissent les mouvements de ces crypto-monnaies.

.. raw:: html

   </div>

🎯 **Objectif Principal**
-------------------------

Notre hypothèse centrale repose sur le fait que le marché Ethereum, grâce à ses caractéristiques uniques (adoption massive des smart contracts, flexibilité applicative, évolution technologique rapide), agit comme un **indicateur avancé** pour le Bitcoin.

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">📊 Analyse Statistique</h3>
         <p style="margin: 0; opacity: 0.9;">Corrélation de Pearson de 0,82 entre ETH et BTC, indiquant une forte dépendance linéaire positive. </p>
      </div>
      
      <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🧠 Deep Learning</h3>
         <p style="margin: 0; opacity: 0.9;">Architecture GRU avec couche Dropout, adaptée à la modélisation des séquences temporelles et à la réduction du surapprentissage.</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">⚡ Prédiction</h3>
         <p style="margin: 0; opacity: 0.9;">Le modèle prédit le prix du BTC au jour J+1 à partir d’une séquence de 32 jours passés, combinant les données ETH et BTC.</p>
      </div>
      
   </div>

🔬 **Approche Méthodologique**
------------------------------

Notre stratégie multi-dimensionnelle combine :

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">

1. **📈 Analyse Statistique Approfondie** - Quantification des relations temporelles ETH-BTC
2. **📉 Modélisation ARIMA** - Établissement d'une baseline de référence robuste  
3. **🤖 Deep Learning Avancé** - Architecture GRU avec Dropout, efficace pour capturer les dépendances séquentielles des prix.
4. **🎯 Validation Empirique** - Tests rigoureux sur données historiques étendues
5. **🖥️ Interface Streamlit** – Déploiement d’une application interactive pour visualiser les prédictions du modèle à partir de nouvelles données.

.. raw:: html

   </div>

📚 **Table des matières**
=========================

.. toctree::
   :maxdepth: 2
   :caption: Documentation complète
   :numbered:

   statistical_analysis
   correlation_analysis
   installation
   model_description
   results
   app

.. raw:: html

   <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; margin: 30px 0; text-align: center;">
      <h3 style="margin: 0 0 15px 0; color: #8b4513;">🚀 Démarrage rapide</h3>
      <p style="margin: 0; color: #5d4e37;">Commencez par la section <strong>Installation</strong> puis explorez l’<strong>Analyse de corrélation</strong> ETH-BTC pour comprendre les fondements statistiques de notre approche prédictive.</p>
   </div>

🏗️ Architecture du Projet
==========================

.. code-block:: none

    ETH-to-BTC/
    ├── README.md                         # Documentation principale du projet
    ├── requirements.txt                  # Dépendances Python
    ├── setup.py                          # Configuration de packaging
    ├── app/
    │   └── app.py                        # Application Streamlit (interface utilisateur)
    ├── models/                           # Modèles entraînés (.h5)
    │   ├── best_best_model.h5
    │   ├── model_gru_bitcoin_eth.h5
    │   ├── model_lstm_bitcoin_eth.h5
    │   └── model_rnn_simple_bitcoin_eth.h5
    ├── data/                             # Données brutes et transformées
    ├── notebooks/                        # Notebooks Jupyter d'analyse
    │   ├── Analyse_Statistique_Corrélation_Choix_Modèle.ipynb
    │   ├── BTC_to_ETH_Best_Model_Search.ipynb
    │   ├── ETH-to-BTC_Streamlit.ipynb
    │   └── pmdarima.ipynb
    ├── src/                              # Code source
    │   ├── predict.py                    # Script de prédiction
    │   ├── train.py                      # Script d'entraînement
    │   ├── data/
    │   │   ├── __init__.py
    │   │   └── collector.py              # Collecte des données via API
    │   ├── features/
    │   │   ├── __init__.py
    │   │   └── preprocessing.py          # Nettoyage et feature engineering
    │   ├── models/
    │   │   ├── __init__.py
    │   │   └── model.py                  # Définition des architectures de modèles
    │   └── utils/
    │       ├── __init__.py
    │       └── visualization.py          # Fonctions de visualisation
    ├── docs/                             # Documentation ReadTheDocs
    ├── .gitattributes                    # Configuration Git
    └── .readthedocs.yml                  # Configuration ReadTheDocs



💡 **Points Clés**
==================

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
      
      <div style="flex: 1; min-width: 200px; background: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 4px solid #2196f3;">
         <h4 style="margin: 0 0 10px 0; color: #1976d2;">🔍 Innovation</h4>
         <p style="margin: 0; font-size: 0.95em;">Premier modèle exploitant systématiquement ETH comme prédicteur de BTC</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #f3e5f5; padding: 20px; border-radius: 10px; border-left: 4px solid #9c27b0;">
         <h4 style="margin: 0 0 10px 0; color: #7b1fa2;">⚡ Performance</h4>
         <p style="margin: 0; font-size: 0.95em;">Le modèle GRU atteint un **R² de 0,98**, indiquant une très forte capacité à expliquer la variance des prix réels du Bitcoin, ce qui confirme la qualité de la prédiction.</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #e8f5e8; padding: 20px; border-radius: 10px; border-left: 4px solid #4caf50;">
         <h4 style="margin: 0 0 10px 0; color: #388e3c;">📊 Validation</h4>
         <p style="margin: 0; font-size: 0.95em;">Le modèle a été soumis à des tests statistiques rigoureux ainsi qu’à une validation croisée étendue, garantissant sa robustesse et sa fiabilité sur des données historiques variées.</p>
      </div>
      
   </div>

📞 **Contact & Support**
========================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; margin: 30px 0;">
      <h3 style="margin: 0 0 15px 0;">Développé par Youssef ES-SAAIDI & Zakariae ZEMMAHI</h3>
      <p style="margin: 0;">
         <a href="https://github.com/YoussefAIDT" style="color: #fff; text-decoration: none; font-weight: bold; margin-right: 15px;">
            🐙 YoussefAIDT GitHub
         </a>
         <a href="https://github.com/zakariazemmahi" style="color: #fff; text-decoration: none; font-weight: bold;">
            🐙 zakariazemmahi GitHub
         </a>
      </p>
   </div>

.. note::
   Cette documentation est en développement actif. Pour les dernières mises à jour, consultez le repository GitHub.
