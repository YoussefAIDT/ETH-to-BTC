============
Installation
============

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; text-align: center; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
      <h2 style="margin: 0; font-size: 2.2em; font-weight: bold;">⚙️ Guide d'Installation</h2>
      <p style="font-size: 1.1em; margin: 15px 0; opacity: 0.9;">Configuration rapide et optimisée pour votre environnement</p>
   </div>

🔧 **Prérequis Système**
========================

.. raw:: html

   <div style="background: #fff3cd; border: 1px solid #ffeaa7; padding: 20px; border-radius: 10px; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0; color: #856404;">⚠️ Vérifications préalables</h4>

Avant de commencer l'installation, assurez-vous d'avoir :

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 20px 0;">
      
      <div style="background: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3;">
         <h5 style="margin: 0 0 8px 0; color: #1976d2;">🐍 Python</h5>
         <p style="margin: 0; font-size: 0.9em;">Version 3.8 ou supérieure</p>
      </div>
      
      <div style="background: #f3e5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #9c27b0;">
         <h5 style="margin: 0 0 8px 0; color: #7b1fa2;">💾 Mémoire RAM</h5>
         <p style="margin: 0; font-size: 0.9em;">Minimum 8GB recommandé</p>
      </div>
      
      <div style="background: #e8f5e8; padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50;">
         <h5 style="margin: 0 0 8px 0; color: #388e3c;">💻 Espace disque</h5>
         <p style="margin: 0; font-size: 0.9em;">2GB d'espace libre</p>
      </div>
      
   </div>

.. raw:: html

   </div>

**Vérification de Python** :

.. code-block:: bash

   python --version
   # Doit afficher Python 3.8.x ou supérieur

🚀 **Installation Rapide**
==========================

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0; color: #2c3e50;">📥 Méthode recommandée</h3>

**Étape 1 : Cloner le dépôt**

.. code-block:: bash

   git clone https://github.com/YoussefAIDT/ETH-to-BTC.git
   cd ETH-to-BTC

**Étape 2 : Créer un environnement virtuel**

.. code-block:: bash

   # Création de l'environnement
   python -m venv eth_btc_env
   
   # Activation (Linux/Mac)
   source eth_btc_env/bin/activate
   
   # Activation (Windows)
   eth_btc_env\Scripts\activate

**Étape 3 : Installer les dépendances**

.. code-block:: bash

   pip install --upgrade pip
   pip install -r requirements.txt

.. raw:: html

   </div>

📦 **Installation via Google Colab** (Recommandé)
=================================================

.. raw:: html

   <div style="background: #fff8e1; border: 2px solid #ffb74d; padding: 25px; border-radius: 15px; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0; color: #ef6c00;">🌟 Option la plus simple</h3>

Pour une utilisation immédiate sans configuration locale :

.. raw:: html

   <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: 15px 0;">

**1. Accédez au dossier notebooks**

.. code-block:: bash

   cd notebooks

**2. Téléchargez les fichiers nécessaires**

- ``Analyse_Statistique_Corrélation_Choix_Modèle.ipynb`` - Analyse complète et modèles de deep learning
- ``pmdarima.ipynb`` - Modélisation ARIMA automatisée

**3. Uploadez dans Google Colab**

1. Ouvrez `Google Colab <https://colab.research.google.com/>`_
2. Cliquez sur "Importer" → "Choisir un fichier"
3. Sélectionnez le notebook désiré
4. Les dépendances s'installeront automatiquement

.. raw:: html

   </div>

.. note::
   **Avantage Colab** : Environnement préconfigué avec GPU gratuit et toutes les bibliothèques nécessaires.

.. raw:: html

   </div>

🔧 **Installation Avancée (Développeurs)**
==========================================

.. raw:: html

   <div style="background: #fce4ec; border-left: 5px solid #e91e63; padding: 20px; margin: 20px 0;">

Pour les développeurs souhaitant contribuer ou personnaliser le projet :

**Installation en mode développement**

.. code-block:: bash

   # Clonage avec historique complet
   git clone --recursive https://github.com/YoussefAIDT/ETH-to-BTC.git
   cd ETH-to-BTC
   
   # Installation en mode éditable
   pip install -e .
   
   # Installation des outils de développement
   pip install -r requirements-dev.txt

**Configuration GPU (optionnel)**

.. code-block:: bash

   # Pour NVIDIA GPU avec CUDA
   pip install tensorflow-gpu==2.12.0
   
   # Vérification GPU
   python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

.. raw:: html

   </div>

📋 **Dépendances Principales**
=============================

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 25px 0;">

**🤖 Machine Learning**

.. code-block:: text

   tensorflow>=2.8.0
   scikit-learn>=1.0.0
   pmdarima>=2.0.0
   statsmodels>=0.13.0

**📊 Analyse de données**

.. code-block:: text

   pandas>=1.3.0
   numpy>=1.21.0
   matplotlib>=3.5.0
   seaborn>=0.11.0
   plotly>=5.0.0

**🔧 Utilitaires**

.. code-block:: text

   yfinance>=0.1.70
   requests>=2.25.0
   tqdm>=4.62.0

.. raw:: html

   </div>

✅ **Vérification de l'Installation**
====================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 15px; color: white; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0;">🧪 Tests de validation</h3>

Exécutez ces commandes pour vérifier que tout fonctionne correctement :

.. code-block:: python

   # Test des imports principaux
   import tensorflow as tf
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   print("✅ TensorFlow version:", tf.__version__)
   print("✅ Pandas version:", pd.__version__)
   print("✅ NumPy version:", np.__version__)

**Test de fonctionnement**

.. code-block:: bash

   # Depuis le répertoire du projet
   python -c "from src.data.collector import *; print('✅ Import successful')"

.. raw:: html

   </div>

🐛 **Résolution des Problèmes**
===============================

.. raw:: html

   <div style="background: #ffebee; border-left: 5px solid #f44336; padding: 20px; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0; color: #c62828;">🔧 Erreurs courantes</h3>

**Problème : Erreur d'importation TensorFlow**

.. code-block:: bash

   # Solution
   pip uninstall tensorflow
   pip install tensorflow==2.12.0

**Problème : Conflits de versions**

.. code-block:: bash

   # Réinstallation propre
   pip freeze > temp_requirements.txt
   pip uninstall -r temp_requirements.txt -y
   pip install -r requirements.txt

**Problème : Mémoire insuffisante**

- Utilisez Google Colab avec GPU
- Réduisez la taille des batches dans les notebooks
- Fermez les autres applications

.. raw:: html

   </div>

🆘 **Support et Aide**
=====================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; margin: 30px 0;">

Si vous rencontrez des difficultés :

1. **📖 Consultez** la section FAQ dans la documentation
2. **🐛 Ouvrez** une issue sur GitHub avec les détails de l'erreur
3. **💬 Contactez** l'équipe de développement

.. raw:: html

   <div style="margin-top: 20px;">
      <a href="https://github.com/YoussefAIDT/ETH-to-BTC/issues" style="background: rgba(255,255,255,0.2); color: white; padding: 10px 20px; border-radius: 25px; text-decoration: none; font-weight: bold; margin: 0 10px;">
         🐛 Signaler un bug
      </a>
      <a href="https://github.com/YoussefAIDT" style="background: rgba(255,255,255,0.2); color: white; padding: 10px 20px; border-radius: 25px; text-decoration: none; font-weight: bold; margin: 0 10px;">
         👨‍💻 Contact développeur
      </a>
   </div>

.. raw:: html

   </div>

.. tip::
   **Prochaine étape** : Une fois l'installation terminée, dirigez-vous vers :doc:`correlation_analysis` pour comprendre les fondements théoriques du projet.
