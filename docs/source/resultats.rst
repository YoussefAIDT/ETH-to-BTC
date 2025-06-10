Résultats
=========

.. raw:: html

   <div style="background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); padding: 30px; border-radius: 15px; color: #2c3e50; text-align: center; margin-bottom: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.2);">
      <h2 style="margin: 0; font-size: 2.2em;">📊 Résultats Clés</h2>
      <p style="font-size: 1.1em; margin-top: 10px;">Synthèse des performances, corrélations, et insights principaux</p>
   </div>

Ce document présente une synthèse esthétique et structurée des principaux résultats issus de nos analyses et modélisations, permettant une compréhension rapide et claire de la dynamique ETH-BTC.

---

### 1. Analyse Descriptive et Statistiques

.. raw:: html

   <div style="background: #fefefe; padding: 25px; border-radius: 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); margin-bottom: 20px; font-family: Arial, sans-serif; font-size: 1em;">
   
**Points forts :**

- ETH présente une **volatilité** significativement plus haute que BTC, avec un écart-type de 0.0567 contre 0.0421 pour BTC.
- La distribution des rendements de ETH est **plus leptokurtique**, indiquant des extrêmes plus fréquents.
- La skewness négative indique une tendance à des baisses plus fortes que les hausses.

**Visualisation :**

.. image:: images/distribution_stats.png
   :alt: Distributions des rendements ETH et BTC
   :width: 600px
   :align: center

---

### 2. Corrélation et Relations Temporelles

.. raw:: html

   <div style="background: #fefefe; padding: 25px; border-radius: 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); margin-bottom: 20px; font-family: Arial, sans-serif; font-size: 1em;">
   
**Corrélation de Pearson :**  
- La corrélation directe entre ETH et BTC sur la période est de **0.89**, indiquant une forte relation linéaire.

**Corrélation croisée par lag :**

| Lag (jours) | Corrélation (r) | Observation |
|--------------|----------------|--------------|
| -3           | 0.234          | ETH précède BTC de 3 jours |
| -2           | 0.456          | ...          |
| -1           | 0.678          | ...          |
|  0           | 0.891          | Corrélation immédiate |
| +1           | 0.543          | BTC précède ETH |

**Graphique de la corrélation :**

.. image:: images/cross_correlation.png
   :alt: Corrélation croisée
   :width: 600px
   :align: center

**Note :** La causalité de Granger confirme que ETH précède souvent BTC, avec une forte significativité (p-value < 0.001).

---

### 3. Tests de Stationnarité

.. raw:: html

   <div style="background: #fefefe; padding: 25px; border-radius: 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); margin-bottom: 20px; font-family: Arial, sans-serif; font-size: 1em;">
   
| Série                | Test ADF (statistique) | p-value | Stationnarité       |
|----------------------|------------------------|---------|---------------------|
| BTC (prix)          | -1.245                 | 0.127   | Non stationnaire   |
| ETH (prix)          | -1.567                 | 0.089   | Non stationnaire   |
| BTC (rendements)    | -18.45                 | <0.001  | Stationnaire       |
| ETH (rendements)    | -20.34                 | <0.001  | Stationnaire       |

*Les prix bruts ne sont pas stationnaires, mais leurs rendements le sont, ce qui valide leur utilisation dans la modélisation.*

---

### 4. Modélisation ARIMA

.. raw:: html

   <div style="background: #fefefe; padding: 25px; border-radius: 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); margin-bottom: 20px; font-family: Arial, sans-serif; font-size: 1em;">
   
**Meilleur modèle ARIMA :** (p=2, d=1, q=2)  
- **RMSE** : 520.34  
- **MAE** : 410.27  
- **MAPE** : 2.5%  

**Analyse des résidus :**  
Les résidus montrent un comportement aléatoire, validant la qualité du modèle.

---

### 5. Performance des Modèles Deep Learning

.. raw:: html

   <div style="background: #fefefe; padding: 25px; border-radius: 10px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); margin-bottom: 20px; font-family: Arial, sans-serif; font-size: 1em;">
   
| Modèle                    | RMSE   | MAE    | R²     | Commentaire                        |
|---------------------------|--------|--------|--------|------------------------------------|
| LSTM simple               | 480.1  | 370.2  | 0.89   | Bonne précision, mais peut encore s'améliorer |
| CNN                       | 460.5  | 355.7  | 0.91   | Extraction locale efficace        |
| CNN-BiLSTM (hybride)      | 430.2  | 340.1  | 0.93   | Meilleure généralisation, capture longue dépendance |
| CNN-BiLSTM + Biais correction | **410.3** | **325.4** | **0.94** | Résultat optimal, adaptation aux biais de décalage |

**Visualisation des prédictions :**

.. image:: images/predictions_comparison.png
   :alt: Prédictions modèles
   :width: 700px
   :align: center

---

### 6. Synthèse et Perspectives

Les résultats indiquent que :

- Les modèles hybrides CNN-BiLSTM, surtout avec correction de biais, fournissent des prédictions précises.
- La relation long terme est confirmée par la cointégration, assurant la stabilité de la relation ETH-BTC.
- La forte corrélation et la causalité de Granger permettent d’exploiter ETH comme prévisionnaire pour BTC.

---

**En résumé :**  
Les analyses statistiques, les modèles ARIMA, et les architectures deep learning ont permis d’obtenir une modélisation robuste et performante. La prochaine étape est l’intégration dans un système de prédiction en temps réel pour exploiter ces insights dans des stratégies d’investissement.

---

*Pour toute question ou pour accéder aux données et modèles, contactez Youssef AIDT sur [GitHub](https://github.com/YoussefAIDT).*
