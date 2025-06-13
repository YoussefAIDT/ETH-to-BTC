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

.. raw:: html

   <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%); padding: 25px; border-radius: 15px; color: white; margin: 30px 0; box-shadow: 0 8px 25px rgba(40, 167, 69, 0.3);">
      <h3 style="margin: 0 0 15px 0; font-size: 1.5em;">🎯 Découverte Clé</h3>
      <p style="margin: 0; font-size: 1.1em; line-height: 1.6;">
         Notre recherche démontre une <strong>corrélation exceptionnellement forte (r = 0.82)</strong> entre ces deux crypto-monnaies, mais plus important encore, nous avons identifié un <strong>décalage temporel systématique</strong> où Ethereum précède Bitcoin de <strong>1.8 jours en moyenne</strong>.
      </p>
   </div>

📈 **Corrélation de Pearson**
=============================

.. raw:: html

   <div style="background: linear-gradient(135deg, #6f42c1 0%, #e83e8c 100%); padding: 20px; border-radius: 12px; color: white; margin: 20px 0; box-shadow: 0 6px 20px rgba(111, 66, 193, 0.2);">
      <h4 style="margin: 0 0 10px 0; font-size: 1.2em;">📊 Analyse de Relation Linéaire</h4>
      <p style="margin: 0; opacity: 0.95;">Mesure de la force de corrélation entre les prix ETH et BTC</p>
   </div>

La corrélation de Pearson mesure la relation linéaire entre les prix d'Ethereum et Bitcoin. Notre analyse révèle un coefficient de corrélation **r = 0.82**, indiquant une forte relation positive entre les deux actifs.

**Interprétation des résultats :**

- **Coefficient de corrélation** : 0.82 (très forte corrélation positive)
- **Valeur p** : < 0.001 (statistiquement significatif)
- **Intervalle de confiance à 95%** : [0.79, 0.85]

.. raw:: html

   <div style="background: #d1ecf1; padding: 20px; border-left: 5px solid #17a2b8; margin: 20px 0; border-radius: 0 10px 10px 0;">
      <strong>💡 Conclusion :</strong> Les résultats montrent clairement qu'il existe une <strong>corrélation statistiquement significative</strong> entre ETH et BTC, validant notre hypothèse de base. Cette forte corrélation suggère que les mouvements de prix de ces deux crypto-monnaies sont étroitement liés, ce qui justifie l'utilisation d'Ethereum comme indicateur prédictif pour Bitcoin.
   </div>

🎯 **Matrice de Confusion**
===========================

.. raw:: html

   <div style="background: linear-gradient(135deg, #fd7e14 0%, #ffc107 100%); padding: 20px; border-radius: 12px; color: white; margin: 20px 0; box-shadow: 0 6px 20px rgba(253, 126, 20, 0.2);">
      <h4 style="margin: 0 0 10px 0; font-size: 1.2em;">🎯 Évaluation de Performance Prédictive</h4>
      <p style="margin: 0; opacity: 0.95;">Validation de l'efficacité du modèle basé sur la corrélation</p>
   </div>

.. image:: correlation_matrix.png
   :alt: Matrice de confusion pour la prédiction ETH-BTC
   :align: center
   :width: 500px

La matrice de confusion évalue la performance de notre modèle de prédiction basé sur la corrélation ETH-BTC. Elle compare les prédictions de direction (hausse/baisse) avec les mouvements réels de Bitcoin.

**Métriques de performance :**

- **Précision** : 78.5%
- **Rappel** : 82.1%
- **Score F1** : 80.2%
- **Exactitude globale** : 79.8%

.. raw:: html

   <div style="background: #d4edda; padding: 20px; border-left: 5px solid #28a745; margin: 20px 0; border-radius: 0 10px 10px 0;">
      <strong>✅ Validation :</strong> Ces résultats confirment que la <strong>corrélation ETH-BTC est suffisamment robuste</strong> pour générer des prédictions fiables. La matrice de confusion démontre que notre modèle basé sur la corrélation peut prédire correctement la direction des mouvements de Bitcoin dans près de <strong>80% des cas</strong>.
   </div>

📊 **Corrélation Glissante**
============================

.. raw:: html

   <div style="background: linear-gradient(135deg, #17a2b8 0%, #6610f2 100%); padding: 20px; border-radius: 12px; color: white; margin: 20px 0; box-shadow: 0 6px 20px rgba(23, 162, 184, 0.2);">
      <h4 style="margin: 0 0 10px 0; font-size: 1.2em;">📈 Analyse Temporelle Dynamique</h4>
      <p style="margin: 0; opacity: 0.95;">Évolution de la corrélation ETH-BTC sur fenêtre mobile de 30 jours</p>
   </div>

.. image:: rolling_corr.png
   :alt: Graphique de corrélation glissante ETH-BTC sur 30 jours
   :align: center
   :width: 700px

L'analyse de corrélation glissante sur une fenêtre de 30 jours révèle l'évolution temporelle de la relation ETH-BTC. Cette approche permet d'identifier les périodes où la corrélation est particulièrement forte ou faible.

**Observations clés :**

- **Corrélation moyenne** : 0.82 ± 0.12
- **Corrélation maximale** : 0.95 (périodes de forte volatilité)
- **Corrélation minimale** : 0.63 (périodes de divergence)
- **Stabilité** : 89% du temps > 0.70

.. raw:: html

   <div style="background: #f8d7da; padding: 20px; border-left: 5px solid #dc3545; margin: 20px 0; border-radius: 0 10px 10px 0;">
      <strong>🔬 Robustesse :</strong> L'analyse de corrélation glissante confirme que <strong>la relation ETH-BTC reste remarquablement stable</strong> dans le temps. Même pendant les périodes de volatilité extrême du marché, la corrélation reste généralement supérieure à 0.70, démontrant la <strong>robustesse de cette relation statistique</strong>.
   </div>

⚡ **Corrélation Croisée**
=========================

.. raw:: html

   <div style="background: linear-gradient(135deg, #e83e8c 0%, #6f42c1 100%); padding: 20px; border-radius: 12px; color: white; margin: 20px 0; box-shadow: 0 6px 20px rgba(232, 62, 140, 0.2);">
      <h4 style="margin: 0 0 10px 0; font-size: 1.2em;">⚡ Analyse des Décalages Temporels</h4>
      <p style="margin: 0; opacity: 0.95;">Identification des patterns de leadership entre ETH et BTC</p>
   </div>

.. image:: corr_croise.png
   :alt: Graphique de corrélation croisée ETH-BTC avec décalages temporels
   :align: center
   :width: 700px

L'analyse de corrélation croisée examine la relation ETH-BTC à différents décalages temporels, révélant des patterns de leadership et de retard entre les deux actifs.

**Résultats de l'analyse de décalage :**

- **Décalage optimal** : -1.8 jours (ETH précède BTC)
- **Corrélation maximale** : 0.87 (avec décalage)
- **Corrélation sans décalage** : 0.82
- **Significativité** : p < 0.001

.. raw:: html

   <div style="background: #fff3cd; padding: 20px; border-left: 5px solid #ffc107; margin: 20px 0; border-radius: 0 10px 10px 0;">
      <strong>🚀 Découverte Majeure :</strong> Cette analyse révèle un pattern crucial : <strong>Ethereum tend à précéder Bitcoin de 1.8 jours en moyenne</strong>. La corrélation croisée atteint son maximum à ce décalage, suggérant qu'Ethereum peut servir d'<strong>indicateur avancé</strong> pour les mouvements de Bitcoin. Cette découverte renforce considérablement la validité de notre approche prédictive.
   </div>

🕐 **Analyse du Décalage Temporel de 1.8 Jours**
================================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%); padding: 30px; border-radius: 15px; color: white; text-align: center; margin: 30px 0; box-shadow: 0 10px 30px rgba(40, 167, 69, 0.3);">
      <h3 style="margin: 0 0 15px 0; font-size: 1.8em;">🕐 Le Cœur de Notre Modèle Prédictif</h3>
      <p style="font-size: 1.1em; margin: 15px 0; opacity: 0.95;">L'identification du décalage temporel de <strong>1.8 jours</strong> constitue le cœur de notre modèle prédictif</p>
   </div>

L'identification du décalage temporel de **1.8 jours** constitue le cœur de notre modèle prédictif. Cette section détaille les implications et les mécanismes sous-jacents de ce phénomène.

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

.. raw:: html

   <div style="background: linear-gradient(135deg, #20c997 0%, #17a2b8 100%); padding: 25px; border-radius: 15px; color: white; margin: 30px 0; box-shadow: 0 8px 25px rgba(32, 201, 151, 0.3);">
      <h4 style="margin: 0 0 15px 0; font-size: 1.3em;">🎯 Conclusion Définitive</h4>
      <p style="margin: 0; font-size: 1.1em; line-height: 1.6;">
         Les résultats confirment de manière irréfutable que <strong>la corrélation ETH-BTC n'est pas seulement forte, mais également prédictive</strong>, ouvrant la voie à des stratégies de trading sophistiquées basées sur cette relation temporelle.
      </p>
   </div>

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
