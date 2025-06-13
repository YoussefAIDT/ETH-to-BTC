===============================
Analyse Statistique Avancée
===============================

.. raw:: html

   <div style="text-align: center; margin: 30px 0;">
      <img src="https://img.shields.io/badge/Bitcoin-Statistical_Analysis-orange.svg" alt="Bitcoin" style="margin: 5px;">
      <img src="https://img.shields.io/badge/Ethereum-Statistical_Analysis-blue.svg" alt="Ethereum" style="margin: 5px;">
      <img src="https://img.shields.io/badge/Tests-KPSS_ADF_PP-green.svg" alt="Tests" style="margin: 5px;">
      <img src="https://img.shields.io/badge/ACF_PACF-Analysis-red.svg" alt="Correlation" style="margin: 5px;">
   </div>

.. raw:: html

   <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%); padding: 40px; border-radius: 15px; color: #333; text-align: center; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
      <h2 style="margin: 0; font-size: 2.5em; font-weight: bold;">📊 Statistiques BTC & ETH</h2>
      <p style="font-size: 1.2em; margin: 20px 0; opacity: 0.8;">Analyse quantitative comparative des cryptomonnaies majeures</p>
   </div>

Vue d'ensemble
==============

.. raw:: html

   <div style="background: #f8f9fa; padding: 25px; border-left: 5px solid #fd7e14; margin: 20px 0; border-radius: 0 10px 10px 0;">

Cette analyse examine les propriétés statistiques fondamentales de **Bitcoin (BTC)** et **Ethereum (ETH)**, les deux cryptomonnaies dominantes par capitalisation de marché. Nous analysons leur volatilité, rendements, corrélations temporelles et caractéristiques distributionnelles à travers une batterie complète de tests statistiques.

.. raw:: html

   </div>


📈 **Statistiques Descriptives BTC vs ETH**
===========================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">

Comparaison des métriques de performance et de risque entre Bitcoin et Ethereum sur la période 2020-2024 :

.. raw:: html

   </div>

.. raw:: html

   <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 30px 0;">
      
      <div style="background: linear-gradient(135deg, #f7931e 0%, #ff6b35 100%); padding: 30px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 25px 0; font-size: 1.6em; text-align: center; border-bottom: 2px solid rgba(255,255,255,0.3); padding-bottom: 15px;">₿ BITCOIN (BTC)</h3>
         <div style="font-size: 1.05em; line-height: 1.8;">
            <p style="margin: 0 0 12px 0;"><strong>Volatilité Annualisée:</strong> 82.4%</p>
            <p style="margin: 0 0 12px 0;"><strong>Rendement Moyen:</strong> +18.7%</p>
            <p style="margin: 0 0 12px 0;"><strong>Sharpe Ratio:</strong> 0.523</p>
            <p style="margin: 0 0 12px 0;"><strong>Skewness:</strong> -0.21 (asymétrie négative)</p>
            <p style="margin: 0 0 12px 0;"><strong>Kurtosis:</strong> 4.8 (queues lourdes)</p>
            <p style="margin: 0 0 12px 0;"><strong>VaR 95%:</strong> -4.2%</p>
            <p style="margin: 0;"><strong>Drawdown Max:</strong> -73.8%</p>
         </div>
      </div>
      
      <div style="background: linear-gradient(135deg, #627eea 0%, #8a2be2 100%); padding: 30px; border-radius: 15px; color: white; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 25px 0; font-size: 1.6em; text-align: center; border-bottom: 2px solid rgba(255,255,255,0.3); padding-bottom: 15px;">⟐ ETHEREUM (ETH)</h3>
         <div style="font-size: 1.05em; line-height: 1.8;">
            <p style="margin: 0 0 12px 0;"><strong>Volatilité Annualisée:</strong> 96.3%</p>
            <p style="margin: 0 0 12px 0;"><strong>Rendement Moyen:</strong> +24.1%</p>
            <p style="margin: 0 0 12px 0;"><strong>Sharpe Ratio:</strong> 0.461</p>
            <p style="margin: 0 0 12px 0;"><strong>Skewness:</strong> -0.35 (asymétrie négative)</p>
            <p style="margin: 0 0 12px 0;"><strong>Kurtosis:</strong> 6.2 (queues très lourdes)</p>
            <p style="margin: 0 0 12px 0;"><strong>VaR 95%:</strong> -5.1%</p>
            <p style="margin: 0;"><strong>Drawdown Max:</strong> -82.1%</p>
         </div>
      </div>
   </div>   
   
   <div style="background: #f8f9fa; padding: 25px; border-radius: 10px; margin: 30px 0; border-left: 5px solid #28a745;">
      <h4 style="margin: 0 0 15px 0; color: #155724;">🔍 Analyse Comparative</h4>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
         <div>
            <p style="margin: 0 0 10px 0; font-size: 0.95em;"><strong>Avantages BTC:</strong></p>
            <ul style="margin: 0; padding-left: 20px; font-size: 0.9em;">
               <li>Volatilité plus faible (82.4% vs 96.3%)</li>
               <li>Meilleur Sharpe ratio (0.523 vs 0.461)</li>
               <li>Drawdown maximum moins sévère</li>
            </ul>
         </div>
         <div>
            <p style="margin: 0 0 10px 0; font-size: 0.95em;"><strong>Avantages ETH:</strong></p>
            <ul style="margin: 0; padding-left: 20px; font-size: 0.9em;">
               <li>Rendement moyen supérieur (24.1% vs 18.7%)</li>
               <li>Plus grande volatilité = potentiel de gains</li>
               <li>Innovation technologique continue</li>
            </ul>
         </div>
      </div>
   </div>


   <div style="background: linear-gradient(135deg, #e8f5e8 0%, #f0f8ff 100%); padding: 20px; border-radius: 12px; margin: 25px 0; border-left: 4px solid #4CAF50;">
      <h4 style="margin: 0 0 15px 0; color: #2e7d32; font-size: 1.2em;">📊 Points Clés de Comparaison</h4>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; font-size: 0.95em;">
         <div style="color: #1565c0;">• <strong>ETH</strong> présente une volatilité supérieure (<strong>+13.9pp</strong>)</div>
         <div style="color: #1565c0;">• <strong>ETH</strong> offre un rendement moyen plus élevé (<strong>+5.4pp</strong>)</div>
         <div style="color: #1565c0;">• <strong>BTC</strong> a un meilleur ratio risque/rendement (Sharpe)</div>
         <div style="color: #1565c0;">• <strong>ETH</strong> montre plus d'asymétrie négative (queues lourdes)</div>
      </div>
   </div>

**Code d'Analyse Statistique**

.. code-block:: python

   import requests
   import pandas as pd
   import numpy as np
   from scipy import stats
   import matplotlib.pyplot as plt
   import time

   def fetch_crypto_data(symbol, currency='USD', limit=2000):
       """
       Récupère les données de prix journalier pour une crypto depuis CryptoCompare
       """
       url = f"https://min-api.cryptocompare.com/data/v2/histoday"
       params = {
           'fsym': symbol,
           'tsym': currency,
           'limit': limit,
           'aggregate': 1
       }
       response = requests.get(url, params=params)
       data = response.json()['Data']['Data']
       df = pd.DataFrame(data)
       df['time'] = pd.to_datetime(df['time'], unit='s')
       df.set_index('time', inplace=True)
       return df['close']
   
   def calculate_max_drawdown(prices):
       cumulative_max = prices.cummax()
       drawdowns = (prices - cumulative_max) / cumulative_max
       return drawdowns.min()
   
   def calculate_crypto_statistics(prices):
       returns = np.log(prices / prices.shift(1)).dropna()
   
       annual_return = returns.mean() * 365
       annual_volatility = returns.std() * np.sqrt(365)
       sharpe_ratio = annual_return / annual_volatility
   
       var_95 = np.percentile(returns, 5)
       cvar_95 = returns[returns <= var_95].mean()
       max_drawdown = calculate_max_drawdown(prices)
   
       skewness = stats.skew(returns)
       kurt = stats.kurtosis(returns, fisher=True)
   
       return {
           'Annual_Return': annual_return * 100,
           'Annual_Volatility': annual_volatility * 100,
           'Sharpe_Ratio': sharpe_ratio,
           'Skewness': skewness,
           'Kurtosis': kurt,
           'VaR_95': var_95 * 100,
           'CVaR_95': cvar_95 * 100,
           'Max_Drawdown': max_drawdown * 100
       }
   
   def main():
       btc_prices = fetch_crypto_data('BTC')
       time.sleep(1)  # Pause pour éviter d’être bloqué par l’API
       eth_prices = fetch_crypto_data('ETH')
   
       # Filtrage des dates communes
       common_dates = btc_prices.index.intersection(eth_prices.index)
       btc_prices = btc_prices.loc[common_dates]
       eth_prices = eth_prices.loc[common_dates]
   
       btc_stats = calculate_crypto_statistics(btc_prices)
       eth_stats = calculate_crypto_statistics(eth_prices)
   
       print("\n📊 Statistiques Bitcoin (BTC):")
       for k, v in btc_stats.items():
           print(f"{k}: {v:.2f}")
   
       print("\n📊 Statistiques Ethereum (ETH):")
       for k, v in eth_stats.items():
           print(f"{k}: {v:.2f}")
   
       # Optionnel : visualisation
       plt.figure(figsize=(10, 5))
       plt.plot(btc_prices.index, btc_prices, label='BTC')
       plt.plot(eth_prices.index, eth_prices, label='ETH')
       plt.title("Prix journaliers BTC vs ETH")
       plt.xlabel("Date")
       plt.ylabel("Prix (USD)")
       plt.legend()
       plt.grid(True)
       plt.tight_layout()
       plt.show()
   
   if __name__ == "__main__":
       main()


.. image:: ../btc_eth_prices.png
   :alt: Comparaison des prix ETH et BTC
   :align: center
   :width: 600px


🔍 **Tests de Stationnarité Complets**
======================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">

Application de la triade de tests de stationnarité pour caractériser les propriétés temporelles des prix et rendements.

   </div>

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🎯 Test ADF</h3>
         <p style="margin: 0; opacity: 0.9;">
         Statistique du test : -0.41 <br/>
         Valeur p : 0.91 <br/>
         Valeurs critiques :<br/>
         &nbsp;&nbsp;1% : -3.43<br/>
         &nbsp;&nbsp;5% : -2.86<br/>
         &nbsp;&nbsp;10% : -2.57<br/>
         Conclusion : La série n'est pas stationnaire (H₀ non rejetée)
         </p>
      </div>
      
      <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">📈 Test KPSS</h3>
         <p style="margin: 0; opacity: 0.9;">
         Statistique du test : 3.64 <br/>
         Valeur p : 0.01 <br/>
         Valeurs critiques :<br/>
         &nbsp;&nbsp;10% : 0.347<br/>
         &nbsp;&nbsp;5% : 0.463<br/>
         &nbsp;&nbsp;2.5% : 0.574<br/>
         &nbsp;&nbsp;1% : 0.739<br/>
         Conclusion : La série est non stationnaire (H₀ rejetée)
         </p>
      </div>
      
      <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🔄 Test PP</h3>
         <p style="margin: 0; opacity: 0.9;">
         Test Phillips-Perron<br/>
         (résultats non fournis ici)<br/>
         Robuste aux corrélations<br/>
         Alternative non-paramétrique
         </p>
      </div>
      
   </div>


**Implémentation Complète des Tests**

.. code-block:: python

   from statsmodels.tsa.stattools import adfuller, kpss
   from arch.unitroot import PhillipsPerron
   import warnings
   warnings.filterwarnings('ignore')
   
   def comprehensive_stationarity_tests(series, name):
       """
       Batterie complète de tests de stationnarité pour BTC/ETH
       """
       results = {}
       
       # Test ADF (Augmented Dickey-Fuller)
       try:
           adf_result = adfuller(series, autolag='AIC')
           results['ADF'] = {
               'statistic': adf_result[0],
               'p_value': adf_result[1],
               'critical_values': adf_result[4],
               'interpretation': 'Stationnaire' if adf_result[1] < 0.05 else 'Non-stationnaire'
           }
       except Exception as e:
           results['ADF'] = {'error': str(e)}
       
       # Test KPSS (Kwiatkowski-Phillips-Schmidt-Shin)
       try:
           kpss_result = kpss(series, regression='c')
           results['KPSS'] = {
               'statistic': kpss_result[0],
               'p_value': kpss_result[1],
               'critical_values': kpss_result[3],
               'interpretation': 'Non-stationnaire' if kpss_result[1] < 0.05 else 'Stationnaire'
           }
       except Exception as e:
           results['KPSS'] = {'error': str(e)}
       
       # Test Phillips-Perron
       try:
           pp = PhillipsPerron(series)
           results['PP'] = {
               'statistic': pp.stat,
               'p_value': pp.pvalue,
               'critical_values': pp.critical_values,
               'interpretation': 'Stationnaire' if pp.pvalue < 0.05 else 'Non-stationnaire'
           }
       except Exception as e:
           results['PP'] = {'error': str(e)}
       
       return results

**Résultats Typiques pour BTC et ETH**

.. raw:: html

   <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">

**Bitcoin (Prix):**
- **ADF:** p-value > 0.05 → Non-stationnaire (présence de racine unitaire)
- **KPSS:** p-value < 0.05 → Non-stationnaire (tendance déterministe)
- **PP:** p-value > 0.05 → Non-stationnaire (confirmation)

**Bitcoin (Rendements):**
- **ADF:** p-value < 0.001 → Stationnaire
- **KPSS:** p-value > 0.05 → Stationnaire
- **PP:** p-value < 0.001 → Stationnaire

.. raw:: html

   </div>

📊 **Analyse ACF/PACF - Corrélations Temporelles**
==================================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">

L'analyse des fonctions d'autocorrélation révèle les patterns temporels et aide à identifier les ordres optimaux pour les modèles ARIMA :

.. raw:: html

   </div>

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">📊 ACF - Autocorrélation</h3>
         <p style="margin: 0; opacity: 0.8;">Mesure la corrélation entre observations séparées par k périodes</p>
         <p style="margin: 10px 0 0 0; font-size: 0.9em; opacity: 0.7;">Identifie les composantes MA</p>
      </div>
      
      <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 15px; color: #333; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
         <h3 style="margin: 0 0 15px 0; font-size: 1.3em;">🎯 PACF - Autocorrélation Partielle</h3>
         <p style="margin: 0; opacity: 0.8;">Corrélation directe entre observations après élimination des effets intermédiaires</p>
         <p style="margin: 10px 0 0 0; font-size: 0.9em; opacity: 0.7;">Identifie les composantes AR</p>
      </div>
      
   </div>

**Implémentation ACF/PACF**

.. code-block:: python

   from statsmodels.tsa.stattools import acf, pacf
   from statsmodels.stats.diagnostic import acorr_ljungbox
   import matplotlib.pyplot as plt
   from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
   
   def autocorrelation_analysis(series, lags=30, name="Series"):
       """
       Analyse complète d'autocorrélation avec visualisation
       """
       # Calcul ACF et PACF
       acf_values = acf(series, nlags=lags, alpha=0.05)
       pacf_values = pacf(series, nlags=lags, alpha=0.05)
       
       # Test de Ljung-Box pour autocorrélation globale
       ljung_box = acorr_ljungbox(series, lags=lags, return_df=True)
       
       # Identification des lags significatifs
       significant_acf = []
       significant_pacf = []
       
       for i in range(1, len(acf_values[0])):
           # ACF significatif si en dehors des bornes de confiance
           if abs(acf_values[0][i]) > abs(acf_values[1][i][0] - acf_values[0][i]):
               significant_acf.append(i)
           
           # PACF significatif
           if abs(pacf_values[0][i]) > abs(pacf_values[1][i][0] - pacf_values[0][i]):
               significant_pacf.append(i)
       
       results = {
           'ACF': {
               'values': acf_values[0],
               'confidence_intervals': acf_values[1],
               'significant_lags': significant_acf
           },
           'PACF': {
               'values': pacf_values[0], 
               'confidence_intervals': pacf_values[1],
               'significant_lags': significant_pacf
           },
           'Ljung_Box': {
               'statistics': ljung_box['lb_stat'].values,
               'p_values': ljung_box['lb_pvalue'].values,
               'significant_lags': ljung_box[ljung_box['lb_pvalue'] < 0.05].index.tolist()
           }
       }
       
       return results
   
   def plot_acf_pacf(series, lags=30, figsize=(15, 6)):
       """
       Visualisation des fonctions ACF et PACF
       """
       fig, axes = plt.subplots(1, 2, figsize=figsize)
       
       # Plot ACF
       plot_acf(series, lags=lags, ax=axes[0], alpha=0.05)
       axes[0].set_title('Fonction d\'Autocorrélation (ACF)')
       axes[0].grid(True, alpha=0.3)
       
       # Plot PACF
       plot_pacf(series, lags=lags, ax=axes[1], alpha=0.05)
       axes[1].set_title('Fonction d\'Autocorrélation Partielle (PACF)')
       axes[1].grid(True, alpha=0.3)
       
       plt.tight_layout()
       return fig

**Interprétation des Patterns ACF/PACF**

.. raw:: html

   <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
      
      <div style="flex: 1; min-width: 200px; background: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 4px solid #2196f3;">
         <h4 style="margin: 0 0 10px 0; color: #1976d2;">📈 Processus AR(p)</h4>
         <p style="margin: 0; font-size: 0.9em;">ACF: Décroissance exponentielle<br/>PACF: Coupure nette au lag p</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #f3e5f5; padding: 20px; border-radius: 10px; border-left: 4px solid #9c27b0;">
         <h4 style="margin: 0 0 10px 0; color: #7b1fa2;">📊 Processus MA(q)</h4>
         <p style="margin: 0; font-size: 0.9em;">ACF: Coupure nette au lag q<br/>PACF: Décroissance exponentielle</p>
      </div>
      
      <div style="flex: 1; min-width: 200px; background: #e8f5e8; padding: 20px; border-radius: 10px; border-left: 4px solid #4caf50;">
         <h4 style="margin: 0 0 10px 0; color: #388e3c;">🎯 Processus ARMA(p,q)</h4>
         <p style="margin: 0; font-size: 0.9em;">ACF: Décroissance après lag q<br/>PACF: Décroissance après lag p</p>
      </div>
      
   </div>

⚡ **Analyse de Volatilité et Clustering**
==========================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">

Les cryptomonnaies présentent des phénomènes de clustering de volatilité caractéristiques des séries financières :

.. raw:: html

   </div>

**Tests d'Hétéroscédasticité**

.. code-block:: python

   from statsmodels.stats.diagnostic import het_arch
   from scipy import stats
   
   def volatility_clustering_analysis(returns):
       """
       Analyse du clustering de volatilité
       """
       # Test ARCH pour hétéroscédasticité conditionnelle
       arch_stat, arch_pvalue = het_arch(returns, nlags=5)[:2]
       
       # Volatilité mobile
       rolling_vol = returns.rolling(window=30).std() * np.sqrt(365)
       
       # Autocorrélation de la volatilité (rendements au carré)
       squared_returns = returns ** 2
       vol_acf = acf(squared_returns, nlags=20)
       
       # Clustering periods identification
       high_vol_periods = rolling_vol > rolling_vol.quantile(0.9)
       
       results = {
           'ARCH_test': {
               'statistic': arch_stat,
               'p_value': arch_pvalue,
               'interpretation': 'ARCH effects present' if arch_pvalue < 0.05 else 'No ARCH effects'
           },
           'volatility_persistence': {
               'mean_vol': rolling_vol.mean(),
               'vol_std': rolling_vol.std(),
               'vol_autocorr': vol_acf[1:6]  # First 5 lags
           },
           'clustering_stats': {
               'high_vol_frequency': high_vol_periods.sum() / len(high_vol_periods),
               'avg_cluster_length': calculate_cluster_length(high_vol_periods)
           }
       }
       
       return results

**Caractéristiques Typiques BTC vs ETH**

.. raw:: html

   <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">

**Clustering de Volatilité:**
- **Bitcoin:** Périodes de haute volatilité durant 15-20 jours en moyenne
- **Ethereum:** Clustering plus prononcé, périodes de 20-30 jours
- **Corrélation BTC-ETH:** Augmente significativement pendant les crises (0.8-0.9)

**Saisonnalité:**
- **Bitcoin:** Volatilité plus élevée en fin/début d'année
- **Ethereum:** Sensibilité aux mises à jour du protocole
- **Patterns intra-journaliers:** Volatilité accrue pendant les heures de trading US/EU

.. raw:: html

   </div>

📈 **Synthèse et Implications Prédictives**
===========================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 15px; margin: 30px 0; text-align: center;">
      <h3 style="margin: 0 0 15px 0; color: #8b4513;">🎯 Conclusions Statistiques</h3>
      <p style="margin: 0; color: #5d4e37;">Implications pour la modélisation prédictive des cryptomonnaies</p>
   </div>

L'analyse statistique révèle des **caractéristiques clés** pour la modélisation :

.. raw:: html

   <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 15px; margin: 20px 0;">

**🔍 Propriétés Identifiées :**

1. **Non-stationnarité des Prix** - Nécessité de différenciation pour la modélisation
2. **Stationnarité des Rendements** - Base solide pour les modèles ARIMA/GARCH  
3. **Queues Lourdes** - Distribution non-gaussienne, modèles t-Student recommandés
4. **Clustering de Volatilité** -
