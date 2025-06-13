"""
Module des modèles de machine learning
"""
from .cnn_bilstm import build_gru_model, build_cnn_bilstm_model

__all__ = ['build_gru_model', 'build_cnn_bilstm_model']
