📈 **Documentation Application Bitcoin Dashboard**
=======================================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #f7931e 0%, #4CAF50 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; margin: 30px 0;">
      <h2 style="margin: 0 0 15px 0;">₿ Bitcoin Prediction Dashboard</h2>
      <p style="margin: 0; font-size: 1.1em;">Application Streamlit pour l'analyse et la prédiction des cryptomonnaies</p>
   </div>

🎯 **Vue d'Ensemble**
====================

Cette application Streamlit offre une interface complète pour l'analyse des cryptomonnaies Bitcoin et Ethereum, incluant des fonctionnalités de prédiction basées sur l'intelligence artificielle.

**Fonctionnalités Principales**

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
      <div style="flex: 1; min-width: 250px; background: #e8f5e8; padding: 20px; border-radius: 10px; border-left: 4px solid #4CAF50;">
         <h4 style="margin: 0 0 10px 0; color: #2e7d32;">📊 Visualisation Temps Réel</h4>
         <p style="margin: 0; font-size: 0.95em;">Affichage des prix actuels BTC/ETH avec graphiques interactifs</p>
      </div>
      
      <div style="flex: 1; min-width: 250px; background: #fff3e0; padding: 20px; border-radius: 10px; border-left: 4px solid #ff9800;">
         <h4 style="margin: 0 0 10px 0; color: #ef6c00;">📈 Analyse Statistique</h4>
         <p style="margin: 0; font-size: 0.95em;">Calculs de corrélation et métriques de performance</p>
      </div>
      
      <div style="flex: 1; min-width: 250px; background: #f3e5f5; padding: 20px; border-radius: 10px; border-left: 4px solid #9c27b0;">
         <h4 style="margin: 0 0 10px 0; color: #7b1fa2;">🔮 Prédictions IA</h4>
         <p style="margin: 0; font-size: 0.95em;">Modèle GRU pour prédire les prix futurs</p>
      </div>
      
      <div style="flex: 1; min-width: 250px; background: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 4px solid #2196f3;">
         <h4 style="margin: 0 0 10px 0; color: #1976d2;">📰 Actualités</h4>
         <p style="margin: 0; font-size: 0.95em;">Feed d'actualités financières en temps réel</p>
      </div>
   </div>

🏗️ **Architecture de l'Application**
=====================================

**Structure du Code**

.. code-block:: python

   app.py
   ├── Configuration Streamlit
   ├── Styles CSS personnalisés
   ├── Fonctions utilitaires
   │   ├── get_crypto_data()
   │   ├── get_crypto_news()
   │   ├── calculate_correlation()
   │   └── create_sequences_for_prediction()
   └── Sections de l'interface
       ├── Prix des Cryptomonnaies
       ├── Statistiques & Corrélation
       ├── Actualités Finance
       └── Prédictions Bitcoin

**Dépendances Principales**

.. raw:: html

   <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0;">📦 Bibliothèques Requises</h4>
      <ul style="margin: 0; color: #495057;">
         <li><strong>streamlit</strong> - Framework d'interface utilisateur</li>
         <li><strong>pandas/numpy</strong> - Manipulation et analyse de données</li>
         <li><strong>plotly</strong> - Visualisations interactives</li>
         <li><strong>keras</strong> - Modèles d'apprentissage automatique</li>
         <li><strong>sklearn</strong> - Préprocessing des données</li>
         <li><strong>requests</strong> - Appels API</li>
      </ul>
   </div>

📊 **Sections de l'Application**
================================

**1. Prix des Cryptomonnaies**

Cette section affiche les données en temps réel pour Bitcoin et Ethereum :

- Prix actuels avec variations quotidiennes
- Tableaux des données récentes (10 derniers jours)
- Graphiques d'évolution sur 30 jours
- Métriques de volume et prix extrêmes

**2. Statistiques & Corrélation**

Analyse approfondie des relations entre BTC et ETH :

- Statistiques descriptives (moyenne, médiane, volatilité)
- Corrélation glissante avec fenêtre ajustable
- Comparaison des performances normalisées
- Visualisations interactives

**3. Actualités Finance**

Intégration du feed d'actualités CryptoCompare :

- Articles récents sur les cryptomonnaies
- Métadonnées (source, date, résumé)
- Interface de lecture optimisée
- Liens vers articles complets

**4. Prédictions Bitcoin**

Module de prédiction utilisant le modèle GRU entraîné :

- Paramètres configurables (nombre de jours, tolérance au risque)
- Génération de prédictions multi-jours
- Recommandations d'investissement automatisées
- Visualisation des tendances prédites

🔧 **Fonctions Techniques Clés**
===============================

**Récupération des Données**

.. code-block:: python

   @st.cache_data(ttl=300)
   def get_crypto_data(symbol, limit=100):
       """Récupère les données crypto depuis CryptoCompare API
       
       Args:
           symbol (str): Symbole de la cryptomonnaie (BTC, ETH)
           limit (int): Nombre de jours de données
           
       Returns:
           DataFrame: Données historiques formatées
       """

**Calcul de Corrélation**

.. code-block:: python

   def calculate_correlation(btc_data, eth_data, window=30):
       """Calcule la corrélation glissante entre BTC et ETH
       
       Args:
           btc_data, eth_data (DataFrame): Données des cryptomonnaies
           window (int): Taille de la fenêtre glissante
           
       Returns:
           Series: Corrélation dans le temps
       """

**Préparation des Séquences**

.. code-block:: python

   def create_sequences_for_prediction(eth_prices, btc_prices, seq_length):
       """Crée des séquences pour alimenter le modèle GRU
       
       Args:
           eth_prices, btc_prices (array): Prix historiques
           seq_length (int): Longueur de la séquence
           
       Returns:
           array: Séquence formatée pour prédiction
       """

⚙️ **Configuration et Déploiement**
===================================

**Installation des Dépendances**

.. code-block:: bash

   pip install streamlit pandas numpy matplotlib plotly seaborn
   pip install keras scikit-learn requests

**Lancement de l'Application**

.. code-block:: bash

   streamlit run app.py

**Configuration Streamlit**

.. raw:: html

   <div style="background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 4px solid #ffc107; margin: 20px 0;">
      <h4 style="margin: 0 0 10px 0; color: #856404;">⚙️ Paramètres de Page</h4>
      <ul style="margin: 0; color: #856404;">
         <li><strong>Titre :</strong> "📈 ETH-to-BTC"</li>
         <li><strong>Icône :</strong> ₿</li>
         <li><strong>Layout :</strong> Wide (pleine largeur)</li>
         <li><strong>Sidebar :</strong> Étendue par défaut</li>
      </ul>
   </div>

🎨 **Interface Utilisateur**
============================

**Design Responsive**

L'application utilise un design moderne avec :

- Gradients CSS pour les en-têtes
- Cartes colorées pour les métriques
- Navigation par sidebar
- Graphiques interactifs Plotly

**Palette de Couleurs**

.. raw:: html

   <div style="display: flex; gap: 10px; margin: 20px 0;">
      <div style="background: #f7931e; color: white; padding: 10px; border-radius: 5px; text-align: center;">
         <strong>Bitcoin</strong><br>#f7931e
      </div>
      <div style="background: #4CAF50; color: white; padding: 10px; border-radius: 5px; text-align: center;">
         <strong>Ethereum</strong><br>#4CAF50
      </div>
      <div style="background: #667eea; color: white; padding: 10px; border-radius: 5px; text-align: center;">
         <strong>Métriques</strong><br>#667eea
      </div>
      <div style="background: #f093fb; color: white; padding: 10px; border-radius: 5px; text-align: center;">
         <strong>Prédictions</strong><br>#f093fb
      </div>
   </div>

🔮 **Module de Prédiction**
===========================

**Processus de Prédiction**

1. **Chargement du Modèle** : Import du modèle GRU pré-entraîné
2. **Préparation des Données** : Normalisation et séquençage
3. **Génération des Prédictions** : Prédictions itératives multi-jours
4. **Post-traitement** : Dénormalisation et calcul des métriques
5. **Recommandations** : Génération automatique de conseils

**Algorithme de Recommandation**

.. raw:: html

   <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 4px solid #6f42c1;">
      <h4 style="margin: 0 0 15px 0; color: #6f42c1;">🤖 Logique de Recommandation</h4>
      <ul style="margin: 0; color: #495057;">
         <li><strong>Variation > +5% :</strong> 🟢 ACHETER (tendance haussière forte)</li>
         <li><strong>Variation +2% to +5% :</strong> 🟡 ACHETER PRUDENT (haussière modérée)</li>
         <li><strong>Variation -2% to +2% :</strong> ⚪ HOLD (mouvement latéral)</li>
         <li><strong>Variation -5% to -2% :</strong> 🟠 VENDRE PARTIEL (baissière modérée)</li>
         <li><strong>Variation < -5% :</strong> 🔴 VENDRE (tendance baissière forte)</li>
      </ul>
   </div>

⚠️ **Limitations et Avertissements**
====================================

.. important::
   **Avertissements Importants :**
   
   - Les prédictions ne constituent pas des conseils financiers
   - Les marchés crypto sont extrêmement volatils
   - L'application est à des fins éducatives uniquement
   - Investissez toujours de manière responsable

**Limitations Techniques**

- Dépendance aux APIs externes (CryptoCompare)
- Cache de 5 minutes pour les données temps réel
- Modèle GRU basé sur des données historiques limitées
- Pas de prise en compte des événements externes

🔧 **Maintenance et Évolution**
==============================

**Améliorations Futures**

.. raw:: html

   <div style="background: #e8f5e8; padding: 20px; border-radius: 10px; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0; color: #2e7d32;">🚀 Roadmap de Développement</h4>
      <ul style="margin: 0; color: #2e7d32;">
         <li>Intégration de modèles multiples (LSTM, Transformer)</li>
         <li>Support d'autres cryptomonnaies (ADA, DOT, etc.)</li>
         <li>Alertes par email/SMS</li>
         <li>Backtesting des stratégies</li>
         <li>API REST pour intégrations externes</li>
         <li>Mode sombre / personnalisation UI</li>
      </ul>
   </div>

**Monitoring et Performance**

- Cache intelligent pour optimiser les performances
- Gestion d'erreur robuste pour les appels API
- Logging des prédictions pour analyse
- Métriques d'utilisation utilisateur

📞 **Contact & Support**
========================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; margin: 30px 0;">
      <h3 style="margin: 0 0 15px 0;">Développé par Youssef AIDT & Zakariae Zemmahi</h3>
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
   Cette documentation couvre la version actuelle de l'application. Pour les mises à jour et nouvelles fonctionnalités, consultez le repository GitHub du projet.
