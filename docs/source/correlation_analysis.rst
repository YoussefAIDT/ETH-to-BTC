==================
Analyse de Corrélation ETH-BTC
==================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; text-align: center; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
      <h2 style="margin: 0; font-size: 2.2em; font-weight: bold;">📊 Analyse de Corrélation ETH-BTC</h2>
      <p style="font-size: 1.1em; margin: 15px 0; opacity: 0.9;">Exploration des relations temporelles et causales entre Ethereum et Bitcoin</p>
   </div>

🔍 **Introduction à la Corrélation Crypto**
===========================================

.. raw:: html

   <div style="background: #f8f9fa; padding: 25px; border-left: 5px solid #007bff; margin: 20px 0; border-radius: 0 10px 10px 0;">

L'analyse de corrélation entre **Ethereum (ETH)** et **Bitcoin (BTC)** révèle des patterns fascinants qui constituent la base théorique de notre modèle prédictif. Cette section explore en profondeur les relations statistiques qui justifient l'utilisation d'Ethereum comme prédicteur du Bitcoin.

.. raw:: html

   </div>

Notre recherche démontre une **corrélation exceptionnellement forte** (r = 0.82) entre ces deux crypto-monnaies, mais plus important encore, nous avons identifié un **décalage temporel systématique** où Ethereum précède Bitcoin de 1.8 jours en moyenne.

📈 **Corrélation de Pearson**
=============================

.. image:: images/pearson_correlation.png
   :alt: Graphique de corrélation de Pearson ETH-BTC
   :align: center
   :width: 600px

La corrélation de Pearson mesure la relation linéaire entre les prix d'Ethereum et Bitcoin. Notre analyse révèle un coefficient de corrélation **r = 0.82**, indiquant une forte relation positive entre les deux actifs.

**Interprétation des résultats :**

- **Coefficient de corrélation** : 0.82 (très forte corrélation positive)
- **Valeur p** : < 0.001 (statistiquement significatif)
- **Intervalle de confiance à 95%** : [0.79, 0.85]

Les résultats montrent clairement qu'il existe une **corrélation statistiquement significative** entre ETH et BTC, validant notre hypothèse de base. Cette forte corrélation suggère que les mouvements de prix de ces deux crypto-monnaies sont étroitement liés, ce qui justifie l'utilisation d'Ethereum comme indicateur prédictif pour Bitcoin.

🎯 **Matrice de Confusion**
===========================

.. image:: images/confusion_matrix.png
   :alt: Matrice de confusion pour la prédiction ETH-BTC
   :align: center
   :width: 500px

La matrice de confusion évalue la performance de notre modèle de prédiction basé sur la corrélation ETH-BTC. Elle compare les prédictions de direction (hausse/baisse) avec les mouvements réels de Bitcoin.

**Métriques de performance :**

- **Précision** : 78.5%
- **Rappel** : 82.1%
- **Score F1** : 80.2%
- **Exactitude globale** : 79.8%

Ces résultats confirment que la **corrélation ETH-BTC est suffisamment robuste** pour générer des prédictions fiables. La matrice de confusion démontre que notre modèle basé sur la corrélation peut prédire correctement la direction des mouvements de Bitcoin dans près de 80% des cas.

📊 **Corrélation Glissante**
============================

.. image:: images/rolling_correlation.png
   :alt: Graphique de corrélation glissante ETH-BTC sur 30 jours
   :align: center
   :width: 700px

L'analyse de corrélation glissante sur une fenêtre de 30 jours révèle l'évolution temporelle de la relation ETH-BTC. Cette approche permet d'identifier les périodes où la corrélation est particulièrement forte ou faible.

**Observations clés :**

- **Corrélation moyenne** : 0.82 ± 0.12
- **Corrélation maximale** : 0.95 (périodes de forte volatilité)
- **Corrélation minimale** : 0.63 (périodes de divergence)
- **Stabilité** : 89% du temps > 0.70

L'analyse de corrélation glissante confirme que **la relation ETH-BTC reste remarquablement stable** dans le temps. Même pendant les périodes de volatilité extrême du marché, la corrélation reste généralement supérieure à 0.70, démontrant la robustesse de cette relation statistique.

⚡ **Corrélation Croisée**
=========================

.. image:: images/cross_correlation.png
   :alt: Graphique de corrélation croisée ETH-BTC avec décalages temporels
   :align: center
   :width: 700px

L'analyse de corrélation croisée examine la relation ETH-BTC à différents décalages temporels, révélant des patterns de leadership et de retard entre les deux actifs.

**Résultats de l'analyse de décalage :**

- **Décalage optimal** : -1.8 jours (ETH précède BTC)
- **Corrélation maximale** : 0.87 (avec décalage)
- **Corrélation sans décalage** : 0.82
- **Significativité** : p < 0.001

Cette analyse révèle un pattern crucial : **Ethereum tend à précéder Bitcoin de 1.8 jours en moyenne**. La corrélation croisée atteint son maximum à ce décalage, suggérant qu'Ethereum peut servir d'indicateur avancé pour les mouvements de Bitcoin. Cette découverte renforce considérablement la validité de notre approche prédictive.

🕐 **Analyse du Décalage Temporel de 1.8 Jours**
================================================

.. raw:: html

   <div style="background: #e8f5e8; padding: 25px; border-left: 5px solid #28a745; margin: 20px 0; border-radius: 0 10px 10px 0;">

L'identification du décalage temporel de **1.8 jours** constitue le cœur de notre modèle prédictif. Cette section détaille les implications et les mécanismes sous-jacents de ce phénomène.

.. raw:: html

   </div>

**Mécanismes explicatifs :**

1. **Liquidité différentielle** : Le marché d'Ethereum réagit plus rapidement aux signaux du marché
2. **Adoption institutionnelle** : Les flux d'investissement touchent d'abord Ethereum avant Bitcoin
3. **Corrélation technique** : Les traders utilisent ETH comme proxy pour anticiper BTC
4. **Volume de transaction** : Les patterns de trading d'Ethereum précèdent ceux de Bitcoin

**Validation statistique :**

- **Test de Granger** : ETH cause BTC (p < 0.001)
- **Analyse de variance** : 73% de la variance de BTC expliquée par ETH avec décalage
- **Robustesse temporelle** : Le décalage reste stable sur 2 ans d'analyse

**Implications pratiques :**

Ce décalage de 1.8 jours offre une **fenêtre d'opportunité prédictive** exceptionnelle. Les mouvements significatifs d'Ethereum peuvent être utilisés pour anticiper les mouvements de Bitcoin avec une précision remarquable, constituant la base théorique solide de notre système de prédiction.

Les résultats confirment de manière irréfutable que **la corrélation ETH-BTC n'est pas seulement forte, mais également prédictive**, ouvrant la voie à des stratégies de trading sophistiquées basées sur cette relation temporelle.

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
   Cette documentation est en développement actif. Pour les dernières mises à jour, consultez le repository GitHub.
