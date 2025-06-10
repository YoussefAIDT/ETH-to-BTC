===============================
Analyse Statistique Avancée
===============================

.. raw:: html

   <div style="text-align: center; margin: 30px 0;">
      <img src="https://img.shields.io/badge/Analyse-Statistique-blue.svg" alt="Statistique" style="margin: 5px;">
      <img src="https://img.shields.io/badge/Tests-Rigoureux-green.svg" alt="Tests" style="margin: 5px;">
      <img src="https://img.shields.io/badge/SciPy-1.8+-orange.svg" alt="SciPy" style="margin: 5px;">
      <img src="https://img.shields.io/badge/StatsModels-0.13+-red.svg" alt="StatsModels" style="margin: 5px;">
   </div>

.. raw:: html

   <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%); padding: 40px; border-radius: 15px; color: #333; text-align: center; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
      <h2 style="margin: 0; font-size: 2.5em; font-weight: bold;">📊 Fondements Statistiques</h2>
      <p style="font-size: 1.2em; margin: 20px 0; opacity: 0.8;">Analyse quantitative rigoureuse des séries temporelles cryptographiques</p>
   </div>

Vue d'ensemble
==============

.. raw:: html

   <div style="background: #f8f9fa; padding: 25px; border-left: 5px solid #fd7e14; margin: 20px 0; border-radius: 0 10px 10px 0;">

L'analyse statistique constitue le socle théorique de notre approche prédictive. Nous appliquons une batterie complète de tests statistiques pour valider les hypothèses fondamentales et caractériser les propriétés des séries temporelles **Bitcoin** et **Ethereum**.

.. raw:: html

   </div>

🔍 **Tests de Stationnarité**
=============================

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">

La stationnarité est cruciale pour la modélisation prédictive. Nous appliquons plusieurs tests complémentaires :

.. raw:: html

   </div>

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🎯 Test ADF</h3>
         <p style="margin: 0; opacity: 0.9;">Augmented Dickey-Fuller pour détecter les racines unitaires</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">📈 Test KPSS</h3>
         <p style="margin: 0; opacity: 0.9;">Kwiatkowski-Phillips-Schmidt-Shin pour la stationnarité de tendance</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🔄 Test PP</h3>
         <p style="margin: 0; opacity: 0.9;">Phillips-Perron pour robustesse aux corrélations sérielles</p>
      </div>
      
   </div>

**Méthodologie des Tests**

.. code-block:: python

   from statsmodels.tsa.stattools import adfuller, kpss
   from arch.unitroot import PhillipsPerron
   
   def stationarity_tests(series, name):
       """
       Batterie complète de tests de stationnarité
       """
       # Test ADF
       adf_stat, adf_pvalue = adfuller(series)[:2]
       
       # Test KPSS  
       kpss_stat, kpss_pvalue = kpss(series)[:2]
       
       # Test Phillips-Perron
       pp = PhillipsPerron(series)
       pp_stat, pp_pvalue = pp.stat, pp.pvalue
       
       return {
           'ADF': {'statistic': adf_stat, 'p_value': adf_pvalue},
           'KPSS': {'statistic': kpss_stat, 'p_value': kpss_pvalue}, 
           'PP': {'statistic': pp_stat, 'p_value': pp_pvalue}
       }

📊 **Analyse de Distribution**
==============================

.. raw:: html

   <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; margin: 30px 0;">

L'étude des distributions nous révèle les caractéristiques fondamentales des rendements crypto :

.. raw:: html

   </div>

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
      
      <div style="flex: 1; min-width: 200px; background: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 4px solid #2196f3;">
         <h4 style="margin: 0 0 10px 0; color: #1976d2;">📈 Asymétrie</h4>
         <p style="margin: 0; font-size: 0.95em;">Test de skewness pour mesurer l'asymétrie des distributions</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #f3e5f5; padding: 20px; border-radius: 10px; border-left: 4px solid #9c27b0;">
         <h4 style="margin: 0 0 10px 0; color: #7b1fa2;">📊 Kurtosis</h4>
         <p style="margin: 0; font-size: 0.95em;">Analyse de l'aplatissement et des queues lourdes</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #e8f5e8; padding: 20px; border-radius: 10px; border-left: 4px solid #4caf50;">
         <h4 style="margin: 0 0 10px 0; color: #388e3c;">🎯 Normalité</h4>
         <p style="margin: 0; font-size: 0.95em;">Tests de Jarque-Bera et Shapiro-Wilk</p>
      </div>
      
   </div>

**Tests de Normalité**

.. code-block:: python

   from scipy.stats import jarque_bera, shapiro, skew, kurtosis
   
   def distribution_analysis(returns):
       """
       Analyse complète de la distribution des rendements
       """
       # Statistiques descriptives
       skewness = skew(returns)
       kurt = kurtosis(returns, fisher=True)
       
       # Tests de normalité
       jb_stat, jb_pvalue = jarque_bera(returns)
       sw_stat, sw_pvalue = shapiro(returns)
       
       return {
           'skewness': skewness,
           'kurtosis': kurt,
           'jarque_bera': {'statistic': jb_stat, 'p_value': jb_pvalue},
           'shapiro_wilk': {'statistic': sw_stat, 'p_value': sw_pvalue}
       }

🔍 **Tests d'Autocorrélation**
==============================

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">

L'analyse d'autocorrélation révèle les patterns temporels cachés dans nos séries :

.. raw:: html

   </div>

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">📊 Test de Ljung-Box</h3>
         <p style="margin: 0; opacity: 0.8;">Détection de l'autocorrélation sérielle dans les résidus</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🎯 ACF/PACF</h3>
         <p style="margin: 0; opacity: 0.8;">Fonctions d'autocorrélation pour identifier les patterns</p>
      </div>
      
   </div>

**Implémentation des Tests**

.. code-block:: python

   from statsmodels.stats.diagnostic import acorr_ljungbox
   from statsmodels.tsa.stattools import acf, pacf
   
   def autocorrelation_analysis(series, lags=20):
       """
       Analyse d'autocorrélation complète
       """
       # Test de Ljung-Box
       lb_stat, lb_pvalue = acorr_ljungbox(series, lags=lags, return_df=False)
       
       # ACF et PACF
       acf_values = acf(series, nlags=lags)
       pacf_values = pacf(series, nlags=lags)
       
       return {
           'ljung_box': {'statistic': lb_stat, 'p_value': lb_pvalue},
           'acf': acf_values,
           'pacf': pacf_values
       }

⚡ **Tests d'Hétéroscédasticité**
=================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">

L'hétéroscédasticité est cruciale dans l'analyse des séries financières. Nous appliquons des tests spécialisés :

.. raw:: html

   </div>

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
      
      <div style="flex: 1; min-width: 200px; background: #fff3cd; padding: 20px; border-radius: 10px; border-left: 4px solid #ffc107;">
         <h4 style="margin: 0 0 10px 0; color: #856404;">🔍 Test ARCH</h4>
         <p style="margin: 0; font-size: 0.95em;">Détection des effets ARCH dans les résidus</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #d1ecf1; padding: 20px; border-radius: 10px; border-left: 4px solid #17a2b8;">
         <h4 style="margin: 0 0 10px 0; color: #0c5460;">📊 Test de Breusch-Pagan</h4>
         <p style="margin: 0; font-size: 0.95em;">Test général d'hétéroscédasticité</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #f8d7da; padding: 20px; border-radius: 10px; border-left: 4px solid #dc3545;">
         <h4 style="margin: 0 0 10px 0; color: #721c24;">⚡ Test de White</h4>
         <p style="margin: 0; font-size: 0.95em;">Robuste aux formes non-linéaires</p>
      </div>
      
   </div>

**Code d'Implémentation**

.. code-block:: python

   from statsmodels.stats.diagnostic import het_arch, het_breuschpagan, het_white
   from statsmodels.regression.linear_model import OLS
   
   def heteroskedasticity_tests(residuals, exog):
       """
       Batterie de tests d'hétéroscédasticité
       """
       # Test ARCH
       arch_stat, arch_pvalue = het_arch(residuals)[:2]
       
       # Test de Breusch-Pagan
       bp_stat, bp_pvalue = het_breuschpagan(residuals, exog)[:2]
       
       # Test de White
       white_stat, white_pvalue = het_white(residuals, exog)[:2]
       
       return {
           'ARCH': {'statistic': arch_stat, 'p_value': arch_pvalue},
           'Breusch_Pagan': {'statistic': bp_stat, 'p_value': bp_pvalue},
           'White': {'statistic': white_stat, 'p_value': white_pvalue}
       }

📈 **Synthèse Méthodologique**
==============================

.. raw:: html

   <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; margin: 30px 0; text-align: center;">
      <h3 style="margin: 0 0 15px 0; color: #8b4513;">🎯 Pipeline d'Analyse</h3>
      <p style="margin: 0; color: #5d4e37;">Notre approche systématique garantit la robustesse statistique des modèles prédictifs</p>
   </div>

L'analyse statistique suit un protocole rigoureux en **quatre étapes** :

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">

1. **🔍 Caractérisation des Séries** - Tests de stationnarité et transformations nécessaires
2. **📊 Analyse Distributionnelle** - Identification des propriétés statistiques fondamentales  
3. **⚡ Détection des Patterns** - Tests d'autocorrélation et structure temporelle
4. **🎯 Validation des Hypothèses** - Tests d'hétéroscédasticité et robustesse

.. raw:: html

   </div>

.. note::
   **Seuil de Significativité** : Tous les tests utilisent α = 0.05 avec correction de Bonferroni pour les tests multiples.

.. warning::
   Les séries financières présentent souvent des **queues lourdes** et de l'**hétéroscédasticité conditionnelle**. Ces caractéristiques sont intégrées dans nos modèles prédictifs.
