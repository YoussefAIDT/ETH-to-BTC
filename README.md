# ETH-to-BTC

<div align="center">
  <img src="https://img.shields.io/badge/version-0.1.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8+-orange.svg" alt="Python">
  <img src="https://img.shields.io/badge/TensorFlow-2.0+-red.svg" alt="TensorFlow">
</div>

<div align="center">
  <h2>🚀 Prédiction Bitcoin avec Ethereum</h2>
  <p><em>Modèle prédictif avancé utilisant les corrélations temporelles ETH-BTC</em></p>
</div>

## 📋 Vue d'ensemble

Ce projet de recherche révolutionnaire explore la relation symbiotique entre **Ethereum** et **Bitcoin** pour développer un modèle prédictif de nouvelle génération. En combinant analyse statistique rigoureuse et techniques de deep learning avancées, nous dévoilons les patterns cachés qui régissent les mouvements de ces crypto-monnaies.

## 🎯 Objectif Principal

Notre hypothèse centrale repose sur le fait que le marché Ethereum, grâce à ses caractéristiques uniques (adoption massive des smart contracts, flexibilité applicative, évolution technologique rapide), agit comme un **indicateur avancé** pour le Bitcoin.

### 🔬 Caractéristiques Clés

| Aspect | Description |
|--------|-------------|
| 📊 **Analyse Statistique** | Corrélation de Pearson de 0,82 entre ETH et BTC, indiquant une forte dépendance linéaire positive |
| 🧠 **Deep Learning** | Architecture GRU avec couche Dropout, adaptée à la modélisation des séquences temporelles et à la réduction du surapprentissage |
| ⚡ **Prédiction** | Le modèle prédit le prix du BTC au jour J+1 à partir d'une séquence de 32 jours passés, combinant les données ETH et BTC |

## 🔬 Approche Méthodologique

Notre stratégie multi-dimensionnelle combine :

1. **📈 Analyse Statistique Approfondie** - Quantification des relations temporelles ETH-BTC
2. **📉 Modélisation ARIMA** - Établissement d'une baseline de référence robuste  
3. **🤖 Deep Learning Avancé** - Architecture GRU avec Dropout, efficace pour capturer les dépendances séquentielles des prix
4. **🎯 Validation Empirique** - Tests rigoureux sur données historiques étendues
5. **🖥️ Interface Streamlit** – Déploiement d'une application interactive pour visualiser les prédictions du modèle à partir de nouvelles données

## 🏗️ Architecture du Projet

```
ETH-to-BTC/
├── 📋 README.md                       # Documentation principale du projet
├── 📦 requirements.txt                # Fichier listant les dépendances Python
├── ⚙️ setup.py                        # Fichier de configuration pour le packaging
├── 🚀 app/
│   └── app.py                         # Application Streamlit (interface utilisateur)
├── 🤖 models/                         # Modèles entraînés
│   ├── best_best_model.h5
│   ├── model_gru_bitcoin_eth.h5
│   ├── model_lstm_bitcoin_eth.h5
│   └── model_rnn_simple_bitcoin_eth.h5
├── 📊 data/                           # Dossier pour les données brutes ou nettoyées
├── 📓 notebooks/                      # Notebooks d'analyse et d'expérimentation
│   ├── Analyse_Statistique_Corrélation_Choix_Modèle.ipynb
│   ├── BTC_to_ETH_Best_Model_Search.ipynb
│   ├── ETH-to-BTC_Streamlit.ipynb
│   └── pmdarima.ipynb
├── 💻 src/                            # Code source organisé par fonctionnalité
│   ├── 🎯 predict.py                  # Script principal pour la prédiction
│   ├── 🧠 train.py                    # Script pour entraîner les modèles
│   ├── data/
│   │   ├── __init__.py
│   │   └── collector.py              # Script de collecte des données
│   ├── features/
│   │   ├── __init__.py
│   │   └── preprocessing.py          # Fonctions de nettoyage & transformation
│   ├── models/
│   │   ├── __init__.py
│   │   └── model.py                  # Définition des architectures de modèles
│   └── utils/
│       ├── __init__.py
│       └── visualization.py          # Fonctions de visualisation
├── 📚 docs/                           # Fichiers de documentation
├── 🧪 .gitattributes                  # Fichier Git (gestion du texte/format)
└── 📖 .readthedocs.yml               # Configuration ReadTheDocs
```

## 🚀 Installation et Démarrage Rapide

### Prérequis

- Python 3.8+
- TensorFlow 2.0+

### Installation

```bash
# Cloner le repository
git clone https://github.com/votre-username/ETH-to-BTC.git
cd ETH-to-BTC

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application Streamlit
streamlit run app/app.py
```

## 💡 Points Clés

### 🔍 Innovation
Premier modèle exploitant systématiquement ETH comme prédicteur de BTC

### ⚡ Performance
Le modèle GRU atteint un **R² de 0,98**, indiquant une très forte capacité à expliquer la variance des prix réels du Bitcoin, ce qui confirme la qualité de la prédiction.

### 📊 Validation
Le modèle a été soumis à des tests statistiques rigoureux ainsi qu'à une validation croisée étendue, garantissant sa robustesse et sa fiabilité sur des données historiques variées.

## 📊 Utilisation

### Entraînement du modèle

```python
from src.models.model import build_gru_model
from src.data.collector import collect_data

# Collecter les données
data = collect_data()

# Entraîner le modèle
model = build_gru_model()
model.fit(X_train, y_train)
```

### Prédiction

```python
from src.predict import predict_btc_price

# Faire une prédiction
prediction = predict_btc_price(eth_data, btc_data)
print(f"Prix BTC prédit : ${prediction:.2f}")
```

## 📚 Documentation

Pour une documentation complète, consultez les notebooks suivants :

- **Analyse Statistique** : `notebooks/Analyse_Statistique_Corrélation_Choix_Modèle.ipynb`
- **Recherche du meilleur modèle** : `notebooks/BTC_to_ETH_Best_Model_Search.ipynb`
- **Application Streamlit** : `notebooks/ETH-to-BTC_Streamlit.ipynb`
- **Modélisation ARIMA** : `notebooks/pmdarima.ipynb`

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Auteurs

**Développé par :**
- **Youssef ES-SAAIDI** - [🐙 YoussefAIDT GitHub](https://github.com/YoussefAIDT)
- **Zakariae ZEMMAHI** - [🐙 zakariazemmahi GitHub](https://github.com/zakariazemmahi)

## 📞 Support

Pour toute question ou support, n'hésitez pas à ouvrir une issue sur GitHub ou à nous contacter directement.

---

> **Note:** Cette documentation est en développement actif. Pour les dernières mises à jour, consultez le repository GitHub.
