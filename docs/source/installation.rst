============
Installation
============

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; text-align: center; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
      <h2 style="margin: 0; font-size: 2.2em; font-weight: bold;">⚙️ Guide d'Installation</h2>
      <p style="font-size: 1.1em; margin: 15px 0; opacity: 0.9;">Configuration exclusive pour Google Colab</p>
   </div>

🌟 **Google Colab Uniquement**
==============================

.. raw:: html

   <div style="background: #fff3cd; border: 1px solid #ffeaa7; padding: 20px; border-radius: 10px; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0; color: #856404;">ℹ️ Information importante</h4>

Ce projet est conçu exclusivement pour fonctionner sur **Google Colab**. Aucune installation locale n'est nécessaire ou supportée.

.. raw:: html

   <div style="background: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3; margin: 15px 0;">
      <h5 style="margin: 0 0 8px 0; color: #1976d2;">🎯 Avantages de Google Colab</h5>
      <ul style="margin: 8px 0; padding-left: 20px;">
         <li>Environnement préconfigué avec GPU gratuit</li>
         <li>Toutes les bibliothèques nécessaires disponibles</li>
         <li>Aucune configuration requise</li>
         <li>Accès immédiat depuis n'importe quel navigateur</li>
      </ul>
   </div>

.. raw:: html

   </div>

📦 **Options d'Utilisation**
============================

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0; color: #2c3e50;">🚀 Deux méthodes disponibles</h3>

**Option 1 : Utiliser les notebooks existants (Recommandé)**
============================================================

.. raw:: html

   <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: 15px 0;">

**1. Accédez au dossier notebooks du projet**

.. code-block:: bash

   cd notebooks

**2. Téléchargez les fichiers nécessaires**

- ``Analyse_Statistique_Corrélation_Choix_Modèle.ipynb`` - Analyse complète et modèles de deep learning
- ``pmdarima.ipynb`` - Modélisation ARIMA automatisée
- ``BTC-to-ETH_best_model_search.ipynb`` - Recherche et sélection du meilleur modèle
- ``BTC-to-ETH_Streamlit.ipynb`` - Application Streamlit interactive

**3. Uploadez dans Google Colab**

1. Ouvrez `Google Colab <https://colab.research.google.com/>`_
2. Cliquez sur "Importer" → "Choisir un fichier"
3. Sélectionnez le notebook désiré
4. Exécutez toutes les cellules pour accéder à l'application

.. raw:: html

   </div>

**Option 2 : Créer un nouveau notebook**
========================================

.. raw:: html

   <div style="background: #fff8e1; border: 2px solid #ffb74d; padding: 25px; border-radius: 15px; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0; color: #ef6c00;">🛠️ Configuration manuelle</h3>

Pour créer votre propre notebook avec l'application Streamlit :

**1. Créez un nouveau notebook sur Google Colab**

**2. Copiez et exécutez ce code dans une cellule :**

.. code-block:: python

   # Installation des dépendances
   !pip install streamlit pyngrok --quiet
   
   # Clonage du projet
   !git clone --recursive https://github.com/YoussefAIDT/ETH-to-BTC.git
   
   # Navigation vers le dossier app
   %cd ETH-to-BTC/app
   
   # Configuration du token ngrok (remplacez par votre token)
   !ngrok authtoken VOTRE_TOKEN_NGROK

**3. Lancez l'application :**

.. code-block:: python

   from pyngrok import ngrok
   
   # Ouvre un tunnel vers http://localhost:8501
   public_url = ngrok.connect(8501)
   print("🚀 L'application est disponible ici :", public_url)
   
   # Démarre Streamlit en arrière-plan
   !streamlit run app.py &

**4. Accédez à votre application**

L'URL publique sera affichée avec le message :
``🚀 L'application est disponible ici : NgrokTunnel: "https://xxxx-xx-xx-xx-xx.ngrok.io"``

.. raw:: html

   </div>

🔑 **Configuration Ngrok**
=========================

.. raw:: html

   <div style="background: #ffebee; border-left: 5px solid #f44336; padding: 20px; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0; color: #c62828;">🔐 Token d'authentification</h3>

Pour utiliser l'Option 2, vous devez :

1. **Créer un compte** sur `Ngrok <https://ngrok.com/>`_
2. **Obtenir votre token** depuis le dashboard Ngrok
3. **Remplacer** ``VOTRE_TOKEN_NGROK`` dans le code par votre token personnel

.. note::
   Le token fourni en exemple est à usage personnel et ne doit pas être utilisé par d'autres utilisateurs.

.. raw:: html

   </div>

📋 **Notebooks Disponibles**
============================

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 25px 0;">

.. raw:: html

   <div style="background: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 4px solid #2196f3;">
      <h4 style="margin: 0 0 10px 0; color: #1976d2;">📊 Analyse_Statistique_Corrélation_Choix_Modèle.ipynb</h4>
      <p style="margin: 0; font-size: 0.9em;">Analyse complète des données et implémentation des modèles de deep learning pour la prédiction ETH/BTC.</p>
   </div>

.. raw:: html

   <div style="background: #f3e5f5; padding: 20px; border-radius: 10px; border-left: 4px solid #9c27b0;">
      <h4 style="margin: 0 0 10px 0; color: #7b1fa2;">📈 pmdarima.ipynb</h4>
      <p style="margin: 0; font-size: 0.9em;">Modélisation ARIMA automatisée avec pmdarima pour l'analyse des séries temporelles.</p>
   </div>

.. raw:: html

   <div style="background: #e8f5e8; padding: 20px; border-radius: 10px; border-left: 4px solid #4caf50;">
      <h4 style="margin: 0 0 10px 0; color: #388e3c;">🎯 BTC-to-ETH_best_model_search.ipynb</h4>
      <p style="margin: 0; font-size: 0.9em;">Recherche et sélection automatique du meilleur modèle de prédiction basé sur les métriques de performance.</p>
   </div>

.. raw:: html

   <div style="background: #fff3e0; padding: 20px; border-radius: 10px; border-left: 4px solid #ff9800;">
      <h4 style="margin: 0 0 10px 0; color: #f57c00;">🚀 BTC-to-ETH_Streamlit.ipynb</h4>
      <p style="margin: 0; font-size: 0.9em;">Application web interactive Streamlit pour la prédiction en temps réel avec interface utilisateur intuitive.</p>
   </div>

.. raw:: html

   </div>

✅ **Démarrage Rapide**
======================

.. raw:: html

   <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 15px; color: white; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0;">🚀 En 3 étapes simples</h3>

**Étape 1** : Ouvrez `Google Colab <https://colab.research.google.com/>`_

**Étape 2** : Choisissez votre méthode :
- Importez un notebook existant depuis le projet, OU
- Créez un nouveau notebook avec le code de configuration

**Étape 3** : Exécutez les cellules et profitez de l'application !

.. raw:: html

   </div>

🆘 **Support et Aide**
=====================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; margin: 30px 0;">

Si vous rencontrez des difficultés :

1. **📖 Vérifiez** que vous utilisez bien Google Colab
2. **🔑 Assurez-vous** d'avoir un token Ngrok valide (Option 2)
3. **🐛 Ouvrez** une issue sur GitHub avec les détails de l'erreur
4. **💬 Contactez** l'équipe de développement

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

.. tip::
   **Prochaine étape** : Une fois l'application lancée, dirigez-vous vers :doc:`correlation_analysis` pour comprendre les fondements théoriques du projet.
