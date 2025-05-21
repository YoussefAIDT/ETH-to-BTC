Utilisation
===========

Pour entraîner un modèle :

.. code-block:: bash

    python -m src.train --days 730 --seq_length 30 --epochs 100 --predict_future

Pour faire des prédictions :

.. code-block:: bash

    python predict.py --model_path models/model_lstm_bitcoin_eth.h5 --days_ahead 30
