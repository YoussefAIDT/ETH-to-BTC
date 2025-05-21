from setuptools import setup, find_packages

setup(
    name="btc-eth-prediction",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
        "tensorflow>=2.6.0",
        "requests",
    ],
    author="Votre Nom",
    author_email="votre.email@example.com",
    description="Modèle de prédiction du prix Bitcoin basé sur Ethereum",
    keywords="bitcoin, ethereum, prediction, deep learning, lstm",
    url="https://github.com/username/btc-eth-prediction",
)