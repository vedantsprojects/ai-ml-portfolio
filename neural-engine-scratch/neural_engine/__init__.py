"""
Neural‑Engine‑Scratch
Lightweight GLUE + RMSNorm prototype.
"""

from .core import GLUE, RMSNorm
from .model import DenseGLUERMSNN
from .train import train

__all__ = [
    "GLUE",
    "RMSNorm",
    "DenseGLUERMSNN",
    "train",
]

