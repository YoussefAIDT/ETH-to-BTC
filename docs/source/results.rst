===============================
Résultats et Performances du Modèle GRU
===============================

.. raw:: html

   <div style="text-align: center; margin: 30px 0;">
      <img src="https://img.shields.io/badge/R²-0.9853-brightgreen.svg" alt="R²" style="margin: 5px;">
      <img src="https://img.shields.io/badge/RMSE-2066.86-orange.svg" alt="RMSE" style="margin: 5px;">
      <img src="https://img.shields.io/badge/MSE-4271928.91-blue.svg" alt="MSE" style="margin: 5px;">
      <img src="https://img.shields.io/badge/Époques-25-success.svg" alt="Époques" style="margin: 5px;">
   </div>

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px; border-radius: 15px; color: white; text-align: center; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
      <h2 style="margin: 0; font-size: 2.5em; font-weight: bold;">🏆 Performance Exceptionnelle GRU</h2>
      <p style="font-size: 1.2em; margin: 20px 0; opacity: 0.9;">98.53% de variance expliquée pour la prédiction Bitcoin</p>
   </div>

Vue d'ensemble
==============

.. raw:: html

   <div style="background: #f8f9fa; padding: 25px; border-left: 5px solid #28a745; margin: 20px 0; border-radius: 0 10px 10px 0;">

Notre modèle **GRU (Gated Recurrent Unit)** a démontré des performances exceptionnelles dans la prédiction du prix du Bitcoin en utilisant les données d'Ethereum comme variable explicative supplémentaire. Avec un **R² de 0.9853**, le modèle explique 98.53% de la variance des prix Bitcoin.

.. raw:: html

   </div>

🎯 **Métriques de Performance Finales**
=======================================

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">📊 R² Score</h3>
         <div style="font-size: 2em; font-weight: bold; margin: 10px 0;">0.9853</div>
         <p style="margin: 0; opacity: 0.8;">98.53% de variance expliquée</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">📈 RMSE</h3>
         <div style="font-size: 2em; font-weight: bold; margin: 10px 0; color: #8b4513;">$2,066.86</div>
         <p style="margin: 0; opacity: 0.8;">Root Mean Square Error</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🎯 MSE</h3>
         <div style="font-size: 2em; font-weight: bold; margin: 10px 0;">4,271,928.91</div>
         <p style="margin: 0; opacity: 0.8;">Mean Squared Error</p>
      </div>
      
   </div>

**Interprétation des Résultats**

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">

**Coefficient de Détermination (R²)** :
   Le R² de **0.9853** indique que notre modèle explique 98.53% de la variance du prix du Bitcoin. Cette valeur exceptionnellement élevée démontre une capacité prédictive remarquable.

**Erreur Quadratique Moyenne (RMSE)** :
   La RMSE de **$2,066.86** représente l'erreur moyenne de prédiction. Considérant que le prix du Bitcoin fluctue souvent de plusieurs milliers de dollars, cette erreur reste relativement maîtrisée.

**Erreur Quadratique Moyenne (MSE)** :
   La MSE de **4,271,928.91** confirme la stabilité du modèle avec une variance d'erreur contrôlée sur l'ensemble de test.

.. raw:: html

   </div>

📊 **Analyse de la Courbe d'Apprentissage**
===========================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">

L'entraînement du modèle révèle une **convergence optimale** en seulement 25 époques :

.. raw:: html

   </div>

**Phases d'Apprentissage**

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
      
      <div style="flex: 1; min-width: 250px; background: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 4px solid #2196f3;">
         <h4 style="margin: 0 0 10px 0; color: #1976d2;">📈 Phase 1 (Époques 1-5)</h4>
         <p style="margin: 0; font-size: 0.95em;"><strong>Convergence rapide initiale</strong><br>
         Loss: 0.0206 → 3.5309e-04<br>
         Val Loss: 5.2204e-04 → 1.8190e-04</p>
      </div>
      
      <div style="flex: 1; min-width: 250px; background: #f3e5f5; padding: 20px; border-radius: 10px; border-left: 4px solid #9c27b0;">
         <h4 style="margin: 0 0 10px 0; color: #7b1fa2;">🎯 Phase 2 (Époques 6-15)</h4>
         <p style="margin: 0; font-size: 0.95em;"><strong>Stabilisation progressive</strong><br>
         Réduction constante validation loss<br>
         Meilleure performance: Époque 15</p>
      </div>
      
      <div style="flex: 1; min-width: 250px; background: #e8f5e8; padding: 20px; border-radius: 10px; border-left: 4px solid #4caf50;">
         <h4 style="margin: 0 0 10px 0; color: #388e3c;">⚡ Phase 3 (Époques 16-25)</h4>
         <p style="margin: 0; font-size: 0.95em;"><strong>Convergence finale</strong><br>
         Early stopping déclenché<br>
         Restauration meilleurs poids</p>
      </div>
      
   </div>

**Logs d'Entraînement Détaillés**

.. code-block:: text

   Epoch 1/100: loss: 0.0206 - val_loss: 5.2204e-04
   Epoch 2/100: loss: 4.3709e-04 - val_loss: 3.2758e-04
   Epoch 3/100: loss: 3.9694e-04 - val_loss: 1.6735e-04
   ...
   Epoch 15/100: loss: 2.1376e-04 - val_loss: 1.5449e-04  # Meilleure performance
   ...
   Epoch 25/100: loss: 2.1269e-04 - val_loss: 1.6502e-04  # Early stopping

**Caractéristiques de Convergence**

.. raw:: html

   <div style="background: #fff3cd; padding: 20px; border-radius: 10px; border-left: 4px solid #ffc107; margin: 20px 0;">

- **Convergence rapide** : Stabilisation en 25 époques seulement
- **Pas de surapprentissage** : Validation loss reste stable
- **Early stopping efficace** : Arrêt automatique optimal à l'époque 25
- **Restauration optimale** : Retour aux poids de l'époque 15

.. raw:: html

   </div>

🛠️ **Configuration du Modèle**
==============================

**Architecture GRU Utilisée**

.. code-block:: python

   # Configuration du modèle GRU
   def build_gru_model(seq_length, units=128, dropout=0.1, learning_rate=0.01):
       model = Sequential()
       model.add(GRU(units=units, input_shape=(seq_length, 2)))
       model.add(Dropout(dropout))
       model.add(Dense(1))
       model.compile(optimizer=Adam(learning_rate=learning_rate), loss='mse')
       return model

.. raw:: html

   <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; margin: 20px 0;">

**Paramètres d'Architecture** :

- **Type** : Sequential avec couche GRU
- **Unités GRU** : 128 neurones
- **Dropout** : 0.1 (10% de régularisation)
- **Couche de sortie** : Dense(1) pour prédiction scalaire
- **Optimiseur** : Adam avec learning rate 0.01
- **Fonction de perte** : Mean Squared Error (MSE)

.. raw:: html

   </div>

**Paramètres d'Entraînement**

.. raw:: html

   <div style="overflow-x: auto; margin: 20px 0;">
      <table style="width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
         <thead style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
            <tr>
               <th style="padding: 15px; text-align: left; border: none;">Paramètre</th>
               <th style="padding: 15px; text-align: center; border: none;">Valeur</th>
               <th style="padding: 15px; text-align: left; border: none;">Description</th>
            </tr>
         </thead>
         <tbody>
            <tr style="background: #f8f9fa; border-bottom: 1px solid #eee;">
               <td style="padding: 15px; font-weight: bold;">Longueur de séquence</td>
               <td style="padding: 15px; text-align: center;">32</td>
               <td style="padding: 15px;">Nombre de pas de temps d'entrée</td>
            </tr>
            <tr style="background: white; border-bottom: 1px solid #eee;">
               <td style="padding: 15px; font-weight: bold;">Variables d'entrée</td>
               <td style="padding: 15px; text-align: center;">2</td>
               <td style="padding: 15px;">Prix ETH normalisé + Prix BTC normalisé</td>
            </tr>
            <tr style="background: #f8f9fa; border-bottom: 1px solid #eee;">
               <td style="padding: 15px; font-weight: bold;">Taille de batch</td>
               <td style="padding: 15px; text-align: center;">32</td>
               <td style="padding: 15px;">Échantillons traités simultanément</td>
            </tr>
            <tr style="background: white; border-bottom: 1px solid #eee;">
               <td style="padding: 15px; font-weight: bold;">Learning rate</td>
               <td style="padding: 15px; text-align: center;">0.01</td>
               <td style="padding: 15px;">Taux d'apprentissage Adam</td>
            </tr>
            <tr style="background: #f8f9fa; border-bottom: 1px solid #eee;">
               <td style="padding: 15px; font-weight: bold;">Early stopping patience</td>
               <td style="padding: 15px; text-align: center;">10</td>
               <td style="padding: 15px;">Époques sans amélioration avant arrêt</td>
            </tr>
            <tr style="background: white;">
               <td style="padding: 15px; font-weight: bold;">Validation split</td>
               <td style="padding: 15px; text-align: center;">20%</td>
               <td style="padding: 15px;">Portion des données pour validation</td>
            </tr>
         </tbody>
      </table>
   </div>

📈 **Données et Prétraitement**
===============================

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">

**Source des Données** :

- **API** : CryptoCompare (min-api.cryptocompare.com)
- **Période** : Mars 2021 - Présent
- **Fréquence** : Données journalières (histoday)
- **Cryptomonnaies** : Bitcoin (BTC) et Ethereum (ETH)
- **Limite** : 2000 points de données par requête

.. raw:: html

   </div>

**Pipeline de Preprocessing**

.. code-block:: python

   def preprocess_data(btc_df, eth_df):
       # 1. Fusion des données sur timestamps
       df = pd.merge(btc_df[['time', 'close']], 
                     eth_df[['time', 'close']], 
                     on='time', suffixes=('_btc', '_eth'))
       
       # 2. Tri chronologique
       df = df.sort_values('time')
       
       # 3. Calcul des rendements (optionnel)
       df['btc_return'] = df['close_btc'].pct_change()
       df['eth_return'] = df['close_eth'].pct_change()
       
       # 4. Suppression des valeurs manquantes
       df.dropna(inplace=True)
       return df

**Étapes de Prétraitement**

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
      
      <div style="flex: 1; min-width: 200px; background: #d4edda; padding: 20px; border-radius: 10px; border-left: 4px solid #28a745;">
         <h4 style="margin: 0 0 10px 0; color: #155724;">1. Fusion Temporelle</h4>
         <p style="margin: 0; font-size: 0.95em;">Alignement BTC et ETH sur timestamps identiques</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #cce5ff; padding: 20px; border-radius: 10px; border-left: 4px solid #007bff;">
         <h4 style="margin: 0 0 10px 0; color: #004085;">2. Normalisation</h4>
         <p style="margin: 0; font-size: 0.95em;">MinMaxScaler pour stabiliser l'entraînement</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #fff3cd; padding: 20px; border-radius: 10px; border-left: 4px solid #ffc107;">
         <h4 style="margin: 0 0 10px 0; color: #856404;">3. Séquences Temporelles</h4>
         <p style="margin: 0; font-size: 0.95em;">Fenêtres glissantes de 32 jours</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #f8d7da; padding: 20px; border-radius: 10px; border-left: 4px solid #dc3545;">
         <h4 style="margin: 0 0 10px 0; color: #721c24;">4. Division Train/Test</h4>
         <p style="margin: 0; font-size: 0.95em;">80% entraînement / 20% test</p>
      </div>
      
   </div>

⚡ **Performance Temporelle et Ressources**
==========================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">

**Efficacité Computationnelle** :

.. raw:: html

   </div>

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">⏱️ Temps d'Entraînement</h3>
         <div style="font-size: 2em; font-weight: bold; margin: 10px 0;">~2 min</div>
         <p style="margin: 0; opacity: 0.8;">25 époques complètes</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🚀 Temps par Époque</h3>
         <div style="font-size: 2em; font-weight: bold; margin: 10px 0;">~3-4s</div>
         <p style="margin: 0; opacity: 0.8;">Processing efficace</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">⚡ Inférence</h3>
         <div style="font-size: 2em; font-weight: bold; margin: 10px 0;">&lt;1s</div>
         <p style="margin: 0; opacity: 0.8;">Ensemble de test complet</p>
      </div>
      
   </div>

**Utilisation des Ressources**

.. code-block:: text

   📊 Profil de Performance :
   ├── Mémoire        : Optimisée avec batch processing
   ├── CPU/GPU        : Compatible accélération matérielle  
   ├── Stockage       : Modèle sauvé "best_best_model.h5"
   └── Scalabilité    : Architecture légère et efficace

🎯 **Analyse Comparative et Avantages**
=======================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">

**Avantages du Modèle GRU** :

.. raw:: html

   </div>

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
      
      <div style="flex: 1; min-width: 200px; background: #d4edda; padding: 20px; border-radius: 10px; border-left: 4px solid #28a745;">
         <h4 style="margin: 0 0 10px 0; color: #155724;">✅ Efficacité</h4>
         <p style="margin: 0; font-size: 0.95em;">Plus rapide que LSTM classique</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #cce5ff; padding: 20px; border-radius: 10px; border-left: 4px solid #007bff;">
         <h4 style="margin: 0 0 10px 0; color: #004085;">🔄 Mémoire</h4>
         <p style="margin: 0; font-size: 0.95em;">Gestion efficace des dépendances temporelles</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #fff3cd; padding: 20px; border-radius: 10px; border-left: 4px solid #ffc107;">
         <h4 style="margin: 0 0 10px 0; color: #856404;">🛡️ Robustesse</h4>
         <p style="margin: 0; font-size: 0.95em;">Résistant au vanishing gradient</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #f8d7da; padding: 20px; border-radius: 10px; border-left: 4px solid #dc3545;">
         <h4 style="margin: 0 0 10px 0; color: #721c24;">⚙️ Simplicité</h4>
         <p style="margin: 0; font-size: 0.95em;">Architecture moins complexe que BiLSTM</p>
      </div>
      
   </div>

📊 **Visualisation et Validation**
==================================

**Graphique des Prédictions**

.. raw:: html

   <div style="background: #f8f9fa; padding: 25px; border-left: 5px solid #17a2b8; margin: 20px 0; border-radius: 0 10px 10px 0;">

Le modèle génère automatiquement une visualisation comparative :

- **Courbe bleue** : Prix Bitcoin réels (ground truth)
- **Courbe rouge pointillée** : Prix Bitcoin prédits par le modèle
- **Période d'affichage** : Ensemble de test (20% des données)
- **Qualité visuelle** : Superposition quasi-parfaite des courbes
- **Format** : Graphique 12x6 avec grid et légendes

.. raw:: html

   </div>

**Code de Visualisation**

.. code-block:: python

   # Visualisation automatique des résultats
   plt.figure(figsize=(12, 6))
   plt.plot(test_dates, y_test_inv, label='Prix BTC réel', color='blue')
   plt.plot(test_dates, y_pred_inv, label='Prix BTC prédit', 
            color='red', linestyle='--')
   plt.title('Prédiction du prix du Bitcoin avec GRU')
   plt.xlabel('Date')
   plt.ylabel('Prix BTC (USD)')
   plt.legend()
   plt.grid(True)
   plt.xticks(rotation=45)
   plt.tight_layout()
   plt.show()

🔬 **Validation et Mesures Anti-Surapprentissage**
==================================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">

**Stratégies de Validation Implementées** :

.. raw:: html

   </div>

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🛑 Early Stopping</h3>
         <p style="margin: 0; opacity: 0.8;">Patience=10, restore_best_weights=True</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🎯 Dropout</h3>
         <p style="margin: 0; opacity: 0.8;">Régularisation 10% pour éviter overfitting</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">📊 Validation Split</h3>
         <p style="margin: 0; opacity: 0.8;">20% données training pour monitoring</p>
      </div>
      
   </div>

**Configuration Anti-Surapprentissage**

.. code-block:: python

   # Callback Early Stopping
   early_stop = EarlyStopping(
       monitor='val_loss',           # Métrique surveillée
       patience=10,                  # Epochs sans amélioration
       restore_best_weights=True     # Retour aux meilleurs poids
   )
   
   # Entraînement avec validation
   model.fit(
       X_train, y_train,
       epochs=100,                   # Maximum autorisé
       batch_size=32,
       validation_split=0.2,         # 20% pour validation
       callbacks=[early_stop],       # Arrêt automatique
       verbose=1
   )

🏆 **Conclusion et Perspectives**
=================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; margin: 30px 0;">
      <h3 style="margin: 0 0 15px 0;">🚀 Succès du Modèle GRU</h3>
      <p style="margin: 0;">Performance exceptionnelle avec 98.53% de variance expliquée</p>
   </div>

**Points Forts Démontrés**

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
      
      <div style="flex: 1; min-width: 200px; background: #d4edda; padding: 20px; border-radius: 10px; border-left: 4px solid #28a745;">
         <h4 style="margin: 0 0 10px 0; color: #155724;">📈 R² Exceptionnel</h4>
         <p style="margin: 0; font-size: 0.95em;">98.53% de variance expliquée</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #cce5ff; padding: 20px; border-radius: 10px; border-left: 4px solid #007bff;">
         <h4 style="margin: 0 0 10px 0; color: #004085;">⚡ Convergence Rapide</h4>
         <p style="margin: 0; font-size: 0.95em;">Entraînement efficace en 25 époques</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #fff3cd; padding: 20px; border-radius: 10px;
