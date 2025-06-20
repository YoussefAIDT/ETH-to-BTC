import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import requests
import time
from datetime import datetime, timedelta
import seaborn as sns
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="📈 ETH-to-BTC",
    page_icon="₿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS pour le style
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #f7931e, #4CAF50);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .prediction-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
.news-card {
    background: #cce5ff; /* bleu clair */
    color: #000;          /* texte noir */
    padding: 1rem;
    border-radius: 8px;
    border-left: 4px solid #007bff;
    margin: 0.5rem 0;
}



</style>
""", unsafe_allow_html=True)

# Titre principal
st.markdown('<h1 class="main-header">₿ Bitcoin Prediction Dashboard</h1>', unsafe_allow_html=True)

# Fonctions utilitaires
@st.cache_data(ttl=300)  # Cache pendant 5 minutes
def get_crypto_data(symbol, limit=100):
    """Récupérer les données crypto depuis CryptoCompare"""
    try:
        url = f'https://min-api.cryptocompare.com/data/v2/histoday'
        params = {
            'fsym': symbol,
            'tsym': 'USD',
            'limit': limit,
            'extraParams': 'streamlit_app'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()['Data']['Data']
            df = pd.DataFrame(data)
            df['time'] = pd.to_datetime(df['time'], unit='s')
            return df
        else:
            st.error(f"Erreur API: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Erreur lors de la récupération des données: {e}")
        return None

@st.cache_data(ttl=1800)  # Cache pendant 30 minutes
def get_crypto_news():
    """Récupérer les actualités crypto"""
    try:
        url = 'https://min-api.cryptocompare.com/data/v2/news/'
        params = {
            'lang': 'EN',
            'sortOrder': 'latest',
            'limit': 10
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()['Data']
        else:
            return []
    except Exception as e:
        st.error(f"Erreur lors de la récupération des actualités: {e}")
        return []

def calculate_correlation(btc_data, eth_data, window=30):
    """Calculer la corrélation glissante"""
    btc_prices = btc_data.set_index('time')['close']
    eth_prices = eth_data.set_index('time')['close']

    # Aligner les données
    common_dates = btc_prices.index.intersection(eth_prices.index)
    btc_aligned = btc_prices.loc[common_dates]
    eth_aligned = eth_prices.loc[common_dates]

    # Corrélation glissante
    correlation = btc_aligned.rolling(window=window).corr(eth_aligned)
    return correlation

def create_sequences_for_prediction(eth_prices, btc_prices, seq_length):
    """Créer des séquences pour la prédiction"""
    if len(eth_prices) < seq_length or len(btc_prices) < seq_length:
        return None

    # Prendre les dernières séquences
    eth_seq = eth_prices[-seq_length:]
    btc_seq = btc_prices[-seq_length:]

    return np.column_stack((eth_seq, btc_seq)).reshape(1, seq_length, 2)

# Sidebar pour la navigation
st.sidebar.title("🔍 Navigation")
section = st.sidebar.selectbox(
    "Choisir une section:",
    ["📊 Prix des Cryptomonnaies", "📈 Statistiques & Corrélation", "📰 Actualités Finance", "🔮 Prédictions Bitcoin"]
)

# Section 1: Prix des Cryptomonnaies
if section == "📊 Prix des Cryptomonnaies":
    st.header("📊 Prix des Cryptomonnaies en Temps Réel")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("₿ Bitcoin (BTC)")
        btc_data = get_crypto_data('BTC')
        if btc_data is not None:
            current_btc = btc_data.iloc[-1]
            prev_btc = btc_data.iloc[-2]
            change_btc = ((current_btc['close'] - prev_btc['close']) / prev_btc['close']) * 100

            st.metric(
                label="Prix Actuel (USD)",
                value=f"${current_btc['close']:,.2f}",
                delta=f"{change_btc:+.2f}%"
            )

            # Tableau des données récentes
            st.subheader("📋 Données Récentes BTC")
            display_data = btc_data.tail(10)[['time', 'close', 'high', 'low', 'volumeto']].copy()
            display_data['time'] = display_data['time'].dt.strftime('%Y-%m-%d')
            display_data.columns = ['Date', 'Clôture', 'Haut', 'Bas', 'Volume']
            st.dataframe(display_data, use_container_width=True)

    with col2:
        st.subheader("⟠ Ethereum (ETH)")
        eth_data = get_crypto_data('ETH')
        if eth_data is not None:
            current_eth = eth_data.iloc[-1]
            prev_eth = eth_data.iloc[-2]
            change_eth = ((current_eth['close'] - prev_eth['close']) / prev_eth['close']) * 100

            st.metric(
                label="Prix Actuel (USD)",
                value=f"${current_eth['close']:,.2f}",
                delta=f"{change_eth:+.2f}%"
            )

            # Tableau des données récentes
            st.subheader("📋 Données Récentes ETH")
            display_data = eth_data.tail(10)[['time', 'close', 'high', 'low', 'volumeto']].copy()
            display_data['time'] = display_data['time'].dt.strftime('%Y-%m-%d')
            display_data.columns = ['Date', 'Clôture', 'Haut', 'Bas', 'Volume']
            st.dataframe(display_data, use_container_width=True)

    # Graphiques individuels BTC et ETH côte à côte
    st.subheader("📈 Évolution des Prix")
    if btc_data is not None and eth_data is not None:
        col1_chart, col2_chart = st.columns(2)
        
        with col1_chart:
            # Graphique BTC individuel
            fig_btc = go.Figure()
            fig_btc.add_trace(go.Scatter(
                x=btc_data['time'],
                y=btc_data['close'],
                mode='lines',
                name='Prix BTC',
                line=dict(color='#f7931e', width=2)
            ))
            fig_btc.update_layout(
                title="Bitcoin (BTC)",
                xaxis_title="Date",
                yaxis_title="Prix (USD)",
                template="plotly_white",
                height=400
            )
            st.plotly_chart(fig_btc, use_container_width=True)
        
        with col2_chart:
            # Graphique ETH individuel
            fig_eth = go.Figure()
            fig_eth.add_trace(go.Scatter(
                x=eth_data['time'],
                y=eth_data['close'],
                mode='lines',
                name='Prix ETH',
                line=dict(color='#4CAF50', width=2)
            ))
            fig_eth.update_layout(
                title="Ethereum (ETH)",
                xaxis_title="Date",
                yaxis_title="Prix (USD)",
                template="plotly_white",
                height=400
            )
            st.plotly_chart(fig_eth, use_container_width=True)
        
        # Graphique combiné sur le même axe
        st.subheader("📊 Comparaison BTC vs ETH - Prix dans le même graphique")
        fig_combined = go.Figure()
        
        # BTC trace
        fig_combined.add_trace(go.Scatter(
            x=btc_data['time'],
            y=btc_data['close'],
            mode='lines',
            name='Bitcoin (BTC)',
            line=dict(color='#f7931e', width=2)
        ))
        
        # ETH trace
        fig_combined.add_trace(go.Scatter(
            x=eth_data['time'],
            y=eth_data['close'],
            mode='lines',
            name='Ethereum (ETH)',
            line=dict(color='#4CAF50', width=2)
        ))
        
        fig_combined.update_layout(
            title="Évolution des Prix BTC vs ETH (30 derniers jours)",
            xaxis_title="Date",
            yaxis_title="Prix (USD)",
            template="plotly_white",
            height=500,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )
        st.plotly_chart(fig_combined, use_container_width=True)

    # Section des autres cryptomonnaies
    st.subheader("💰 Autres Cryptomonnaies Populaires")
    
    # Liste des autres cryptos à afficher
    other_cryptos = [
        ('ADA', 'Cardano', '🔵'),
        ('DOT', 'Polkadot', '🔴'),
        ('LINK', 'Chainlink', '🔗'),
        ('XRP', 'Ripple', '💧'),
        ('LTC', 'Litecoin', '⚡'),
        ('BCH', 'Bitcoin Cash', '💚'),
        ('UNI', 'Uniswap', '🦄'),
        ('MATIC', 'Polygon', '🟣')
    ]
    
    # Créer des colonnes pour afficher les prix
    cols = st.columns(4)
    
    for idx, (symbol, name, emoji) in enumerate(other_cryptos):
        with cols[idx % 4]:
            crypto_data = get_crypto_data(symbol)
            if crypto_data is not None:
                current_price = crypto_data.iloc[-1]['close']
                prev_price = crypto_data.iloc[-2]['close']
                change = ((current_price - prev_price) / prev_price) * 100
                
                # Couleur selon la variation
                delta_color = "normal"
                if change > 0:
                    delta_color = "normal"
                elif change < 0:
                    delta_color = "inverse"
                
                st.metric(
                    label=f"{emoji} {name} ({symbol})",
                    value=f"${current_price:.4f}" if current_price < 1 else f"${current_price:,.2f}",
                    delta=f"{change:+.2f}%"
                )
            else:
                st.error(f"Erreur: Impossible de charger {name}")
    
    # Tableau récapitulatif
    st.subheader("📊 Tableau Récapitulatif")
    
    summary_data = []
    all_cryptos = [('BTC', 'Bitcoin')] + [('ETH', 'Ethereum')] + [(symbol, name) for symbol, name, _ in other_cryptos]
    
    for symbol, name in all_cryptos:
        crypto_data = get_crypto_data(symbol)
        if crypto_data is not None:
            current = crypto_data.iloc[-1]
            prev = crypto_data.iloc[-2]
            change = ((current['close'] - prev['close']) / prev['close']) * 100
            
            summary_data.append({
                'Cryptomonnaie': f"{name} ({symbol})",
                'Prix Actuel (USD)': f"${current['close']:,.4f}" if current['close'] < 1 else f"${current['close']:,.2f}",
                'Variation 24h (%)': f"{change:+.2f}%",
                'Volume 24h': f"${current['volumeto']:,.0f}",
                'Plus Haut 24h': f"${current['high']:,.4f}" if current['high'] < 1 else f"${current['high']:,.2f}",
                'Plus Bas 24h': f"${current['low']:,.4f}" if current['low'] < 1 else f"${current['low']:,.2f}"
            })
    
    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)
# Section 2: Statistiques & Corrélation
elif section == "📈 Statistiques & Corrélation":
    st.header("📈 Statistiques & Analyse de Corrélation")
    
    # Récupérer plus de données pour l'analyse
    btc_data = get_crypto_data('BTC', 365)
    eth_data = get_crypto_data('ETH', 365)
    
    if btc_data is not None and eth_data is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Statistiques Bitcoin")
            btc_stats = {
                'Prix Moyen': f"${btc_data['close'].mean():,.2f}",
                'Prix Médian': f"${btc_data['close'].median():,.2f}",
                'Écart-type': f"${btc_data['close'].std():,.2f}",
                'Volatilité (CV)': f"{(btc_data['close'].std()/btc_data['close'].mean()*100):.2f}%",
                'Prix Min': f"${btc_data['close'].min():,.2f}",
                'Prix Max': f"${btc_data['close'].max():,.2f}"
            }
            
            for key, value in btc_stats.items():
                st.metric(key, value)
        
        with col2:
            st.subheader("📊 Statistiques Ethereum")
            eth_stats = {
                'Prix Moyen': f"${eth_data['close'].mean():,.2f}",
                'Prix Médian': f"${eth_data['close'].median():,.2f}",
                'Écart-type': f"${eth_data['close'].std():,.2f}",
                'Volatilité (CV)': f"{(eth_data['close'].std()/eth_data['close'].mean()*100):.2f}%",
                'Prix Min': f"${eth_data['close'].min():,.2f}",
                'Prix Max': f"${eth_data['close'].max():,.2f}"
            }
            
            for key, value in eth_stats.items():
                st.metric(key, value)
        
        # Corrélation glissante
        st.subheader("🔗 Corrélation Glissante BTC-ETH")
        correlation_window = st.slider("Fenêtre de corrélation (jours)", 7, 90, 30)
        correlation = calculate_correlation(btc_data, eth_data, correlation_window)
        
        fig_corr = go.Figure()
        fig_corr.add_trace(go.Scatter(
            x=correlation.index,
            y=correlation.values,
            mode='lines',
            name=f'Corrélation ({correlation_window} jours)',
            line=dict(color='purple', width=2)
        ))
        fig_corr.add_hline(y=0.5, line_dash="dash", line_color="red",
                          annotation_text="Corrélation forte (0.5)")
        fig_corr.update_layout(
            title=f"Corrélation Glissante BTC-ETH ({correlation_window} jours)",
            xaxis_title="Date",
            yaxis_title="Coefficient de Corrélation",
            template="plotly_white",
            height=400
        )
        st.plotly_chart(fig_corr, use_container_width=True)

# Section 3: Actualités Finance
elif section == "📰 Actualités Finance":
    st.header("📰 Actualités Financières & Crypto")

    news_data = get_crypto_news()

    if news_data:
        for i, article in enumerate(news_data):
            with st.container():
                st.markdown(f"""
                <div class="news-card">
                    <h4>{article.get('title', 'Titre non disponible')}</h4>
                    <p><strong>Source:</strong> {article.get('source_info', {}).get('name', 'Source inconnue')}</p>
                    <p>{article.get('body', 'Contenu non disponible')[:300]}...</p>
                    <p><small>📅 {datetime.fromtimestamp(article.get('published_on', 0)).strftime('%Y-%m-%d %H:%M')}</small></p>
                </div>
                """, unsafe_allow_html=True)

                if article.get('url'):
                    st.markdown(f"[📖 Lire l'article complet]({article['url']})")

                st.divider()
    else:
        st.warning("Aucune actualité disponible pour le moment.")
        

# Section 5: Prédictions Bitcoin
elif section == "🔮 Prédictions Bitcoin":
    st.header("🔮 Prédictions Bitcoin avec IA")

    # Paramètres de prédiction
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("⚙️ Paramètres de Prédiction")

        model_choice = st.selectbox(
            "Choisir le modèle:",
            ["best_best_model.h5", "best_lstm_model.h5", "Modèle 3 (À venir)"]
        )

        days_to_predict = st.slider(
            "Nombre de jours à prédire:",
            min_value=1,
            max_value=30,
            value=7
        )

        risk_tolerance = st.selectbox(
            "Tolérance au risque:",
            ["Conservateur", "Modéré", "Agressif"],
            help="Conservateur: Seuils stricts, Modéré: Équilibré, Agressif: Seuils flexibles"
        )

        confidence_threshold = st.slider(
            "Seuil de confiance (%):",
            min_value=50,
            max_value=95,
            value=80,
            help="Plus élevé = recommandations plus prudentes"
        )

        # Nouveaux paramètres avancés
        with st.expander("🔧 Paramètres Avancés"):
            volatility_adjustment = st.checkbox(
                "Ajustement volatilité", 
                value=True,
                help="Ajuste les prédictions selon la volatilité récente"
            )
            
            ensemble_prediction = st.checkbox(
                "Prédiction d'ensemble",
                value=False,
                help="Combine plusieurs prédictions pour plus de robustesse"
            )

    with col2:
        st.subheader("📊 Résultats de Prédiction")

        if st.button("🚀 Générer Prédiction", type="primary"):
            try:
                # Charger le modèle
                if model_choice == "best_best_model.h5":
                    try:
                        model = load_model("best_best_model.h5", compile=False)
                        model.compile(optimizer='adam', loss='mse')
                        st.success("✅ Modèle best_best_model.h5 chargé avec succès!")
                    except:
                        st.error("❌ Impossible de charger le modèle best_best_model.h5. Vérifiez que le fichier existe.")
                        st.stop()
                elif model_choice == "best_lstm_model.h5":
                    try:
                        model = load_model("best_lstm_modele.h5", compile=False)
                        model.compile(optimizer='adam', loss='mse')
                        st.success("✅ Modèle best_lstm_model.h5 chargé avec succès!")
                    except:
                        st.error("❌ Impossible de charger le modèle best_lstm_model.h5. Vérifiez que le fichier existe.")
                        st.stop()
                else:
                    st.warning("⚠️ Le troisième modèle n'est pas encore disponible.")
                    st.stop()

                # Récupérer les données récentes
                btc_data = get_crypto_data('BTC', 100)
                eth_data = get_crypto_data('ETH', 100)

                if btc_data is not None and eth_data is not None:
                    eth_scaler = MinMaxScaler()
                    btc_scaler = MinMaxScaler()

                    eth_scaled = eth_scaler.fit_transform(eth_data[['close']])
                    btc_scaled = btc_scaler.fit_transform(btc_data[['close']])

                    # Calculer la volatilité récente
                    recent_returns = btc_data['close'].pct_change().tail(14)
                    volatility = recent_returns.std() * np.sqrt(365)  # Volatilité annualisée
                    
                    seq_length = 32
                    if len(eth_scaled) >= seq_length and len(btc_scaled) >= seq_length:
                        sequence = create_sequences_for_prediction(
                            eth_scaled.flatten(),
                            btc_scaled.flatten(),
                            seq_length
                        )

                        if sequence is not None:
                            # Générer plusieurs prédictions si ensemble_prediction est activé
                            num_predictions = 5 if ensemble_prediction else 1
                            all_predictions = []
                            
                            for run in range(num_predictions):
                                predictions = []
                                current_btc = btc_data['close'].iloc[-1]
                                temp_sequence = sequence.copy()

                                for day in range(days_to_predict):
                                    pred_scaled = model.predict(temp_sequence, verbose=0)
                                    pred_price = btc_scaler.inverse_transform(pred_scaled)[0][0]
                                    
                                    # Ajouter du bruit basé sur la volatilité si ensemble
                                    if ensemble_prediction and run > 0:
                                        noise = np.random.normal(0, volatility * pred_price * 0.1)
                                        pred_price += noise
                                    
                                    predictions.append(pred_price)

                                    new_eth = eth_scaled[-1]
                                    new_btc = pred_scaled[0]

                                    temp_sequence = np.roll(temp_sequence, -1, axis=1)
                                    temp_sequence[0, -1, 0] = new_eth
                                    temp_sequence[0, -1, 1] = new_btc

                                all_predictions.append(predictions)
                            
                            # Calculer la prédiction finale (moyenne si ensemble)
                            if ensemble_prediction:
                                final_predictions = np.mean(all_predictions, axis=0)
                                prediction_std = np.std(all_predictions, axis=0)
                            else:
                                final_predictions = all_predictions[0]
                                prediction_std = np.zeros_like(final_predictions)

                            current_btc = btc_data['close'].iloc[-1]
                            last_date = btc_data['time'].iloc[-1]
                            future_dates = [last_date + timedelta(days=i+1) for i in range(days_to_predict)]

                            # Calculer la confiance basée sur la volatilité et l'écart-type
                            base_confidence = 90 - (volatility * 100)  # Plus volatile = moins confiant
                            if ensemble_prediction:
                                confidence_adjustment = 10 - (np.mean(prediction_std) / current_btc * 100)
                            else:
                                confidence_adjustment = 0
                            
                            actual_confidence = max(50, min(95, base_confidence + confidence_adjustment))

                            # Ajuster les prédictions selon la tolérance au risque
                            risk_multipliers = {
                                "Conservateur": 0.7,  # Prédictions plus prudentes
                                "Modéré": 1.0,        # Prédictions normales
                                "Agressif": 1.3       # Prédictions plus optimistes
                            }
                            
                            risk_multiplier = risk_multipliers[risk_tolerance]
                            change_pct = (final_predictions[-1] - current_btc) / current_btc * 100
                            adjusted_change_pct = change_pct * risk_multiplier

                            # Afficher les résultats
                            model_name = model_choice.replace('.h5', '').replace('_', ' ').title()
                            
                            # Indicateur de confiance coloré
                            confidence_color = "green" if actual_confidence >= confidence_threshold else "orange" if actual_confidence >= 70 else "red"
                            
                            st.markdown(f"""
                            <div class="prediction-card">
                                <h3>🔮 Prédictions pour les {days_to_predict} prochains jours</h3>
                                <p><strong>Modèle utilisé:</strong> {model_name}</p>
                                <p><strong>Prix actuel BTC:</strong> ${current_btc:,.2f}</p>
                                <p><strong>Prix prédit (J+{days_to_predict}):</strong> ${final_predictions[-1]:,.2f}</p>
                                <p><strong>Variation prévue:</strong> {change_pct:+.2f}% (ajustée: {adjusted_change_pct:+.2f}%)</p>
                                <p><strong>Confiance du modèle:</strong> <span style="color:{confidence_color}; font-weight:bold;">{actual_confidence:.1f}%</span></p>
                                <p><strong>Volatilité récente:</strong> {volatility*100:.1f}% (annualisée)</p>
                            </div>
                            """, unsafe_allow_html=True)

                            # Graphique avec bandes de confiance
                            fig_pred = go.Figure()
                            
                            fig_pred.add_trace(go.Scatter(
                                x=btc_data['time'].tail(30),
                                y=btc_data['close'].tail(30),
                                mode='lines',
                                name='Prix Historique',
                                line=dict(color='blue')
                            ))
                            
                            fig_pred.add_trace(go.Scatter(
                                x=future_dates,
                                y=final_predictions,
                                mode='lines+markers',
                                name=f'Prédictions ({model_name})',
                                line=dict(color='red', dash='dash'),
                                marker=dict(size=8)
                            ))
                            
                            # Ajouter bandes de confiance si prédiction d'ensemble
                            if ensemble_prediction:
                                upper_bound = final_predictions + prediction_std
                                lower_bound = final_predictions - prediction_std
                                
                                fig_pred.add_trace(go.Scatter(
                                    x=future_dates + future_dates[::-1],
                                    y=list(upper_bound) + list(lower_bound[::-1]),
                                    fill='toself',
                                    fillcolor='rgba(255,0,0,0.2)',
                                    line=dict(color='rgba(255,255,255,0)'),
                                    name='Intervalle de confiance',
                                    showlegend=True
                                ))
                            
                            fig_pred.update_layout(
                                title=f"Prédiction Bitcoin - {days_to_predict} jours ({model_name})",
                                xaxis_title="Date",
                                yaxis_title="Prix (USD)",
                                template="plotly_white",
                                height=500
                            )
                            st.plotly_chart(fig_pred, use_container_width=True)

                            # Recommandations intelligentes basées sur tous les paramètres
                            st.subheader("💡 Recommandations Intelligentes")

                            # Ajuster les seuils selon la tolérance au risque et la confiance
                            confidence_factor = actual_confidence / 100
                            
                            if risk_tolerance == "Conservateur":
                                buy_threshold = 3 / confidence_factor
                                sell_threshold = -2 / confidence_factor
                            elif risk_tolerance == "Modéré":
                                buy_threshold = 2 / confidence_factor
                                sell_threshold = -3 / confidence_factor
                            else:  # Agressif
                                buy_threshold = 1 / confidence_factor
                                sell_threshold = -5 / confidence_factor

                            # Prendre en compte la confiance du modèle
                            if actual_confidence < confidence_threshold:
                                recommendation = "⚪ HOLD (Confiance insuffisante)"
                                reason = f"Confiance {actual_confidence:.1f}% < seuil {confidence_threshold}%"
                                risk_level = "Élevé"
                            elif adjusted_change_pct > buy_threshold:
                                if volatility > 0.8:  # Haute volatilité
                                    recommendation = "🟡 ACHETER (Prudent - Volatilité élevée)"
                                    reason = "Tendance haussière mais marché volatil"
                                    risk_level = "Élevé"
                                else:
                                    recommendation = "🟢 ACHETER"
                                    reason = "Tendance haussière forte prévue"
                                    risk_level = "Faible" if risk_tolerance == "Agressif" else "Modéré"
                            elif adjusted_change_pct < sell_threshold:
                                recommendation = "🔴 VENDRE (Partiel)"
                                reason = "Tendance baissière prévue"
                                risk_level = "Élevé"
                            else:
                                recommendation = "⚪ HOLD"
                                reason = "Mouvement latéral prévu"
                                risk_level = "Faible"

                            # Ajustements spéciaux selon la tolérance au risque
                            if risk_tolerance == "Conservateur" and risk_level == "Élevé":
                                recommendation = "⚪ HOLD (Trop risqué pour profil conservateur)"
                                reason = "Risque incompatible avec profil conservateur"

                            col3, col4 = st.columns(2)
                            with col3:
                                st.metric("Recommandation", recommendation)
                                st.metric("Raison", reason)

                            with col4:
                                st.metric("Niveau de Risque", risk_level)
                                st.metric("Confiance Effective", f"{actual_confidence:.1f}%")

                            # Indicateurs de qualité de prédiction
                            st.subheader("🎯 Qualité de la Prédiction")
                            
                            col5, col6, col7 = st.columns(3)
                            with col5:
                                conf_score = "🟢 Excellente" if actual_confidence >= 85 else "🟡 Bonne" if actual_confidence >= 70 else "🔴 Faible"
                                st.metric("Confiance", conf_score)
                            
                            with col6:
                                vol_score = "🟢 Faible" if volatility < 0.5 else "🟡 Modérée" if volatility < 1.0 else "🔴 Élevée"
                                st.metric("Volatilité", vol_score)
                            
                            with col7:
                                match_score = "🟢 Conforme" if actual_confidence >= confidence_threshold else "🔴 Non conforme"
                                st.metric("Seuil Atteint", match_score)

                            st.subheader("📋 Prédictions Détaillées")
                            pred_df = pd.DataFrame({
                                'Date': [date.strftime('%Y-%m-%d') for date in future_dates],
                                'Prix Prédit (USD)': [f"${price:,.2f}" for price in final_predictions],
                                'Variation (%)': [f"{((price - current_btc) / current_btc * 100):+.2f}%" for price in final_predictions],
                                'Incertitude': [f"±${std:.2f}" if ensemble_prediction else "N/A" for std in prediction_std]
                            })
                            st.dataframe(pred_df, use_container_width=True)

                            # Explication des paramètres utilisés
                            with st.expander("ℹ️ Explication des Paramètres"):
                                st.write(f"""
                                **Impact de vos paramètres sur cette prédiction :**
                                
                                - **Tolérance au risque ({risk_tolerance})** : 
                                  - Multiplicateur appliqué : {risk_multiplier}x
                                  - Seuils d'achat/vente ajustés selon votre profil
                                
                                - **Seuil de confiance ({confidence_threshold}%)** : 
                                  - Confiance effective du modèle : {actual_confidence:.1f}%
                                  - {"✅ Seuil atteint" if actual_confidence >= confidence_threshold else "❌ Seuil non atteint"}
                                
                                - **Volatilité récente** : {volatility*100:.1f}% (annualisée)
                                  - Impact sur la confiance et les recommandations
                                
                                {"- **Prédiction d'ensemble** : Activée - Moyenne de 5 prédictions" if ensemble_prediction else ""}
                                """)

                        else:
                            st.error("❌ Impossible de créer la séquence de prédiction.")
                    else:
                        st.error("❌ Pas assez de données pour faire une prédiction.")
                else:
                    st.error("❌ Impossible de récupérer les données nécessaires.")

            except Exception as e:
                st.error(f"❌ Erreur lors de la génération des prédictions: {e}")

        st.warning("""
        ⚠️ **Avertissement Important:**

        Ces prédictions sont générées par un modèle d'IA et ne constituent pas des conseils financiers.
        Les paramètres de tolérance au risque et de confiance influencent les recommandations mais ne garantissent pas leur exactitude.
        Les marchés des cryptomonnaies sont extrêmement volatils et imprévisibles.
        Investissez toujours de manière responsable et ne risquez que ce que vous pouvez vous permettre de perdre.
        """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666;">
        <p>💡 Développé avec Streamlit | Données via CryptoCompare API</p>
        <p>⚠️ Cette application est à des fins éducatives uniquement</p>
    </div>
    """,
    unsafe_allow_html=True
)
