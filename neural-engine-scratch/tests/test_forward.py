import torch
from neural_engine.model import DenseGLUERMSNN

def test_forward():
    X = torch.rand(8, 3)
    assert DenseGLUERMSNN(3, 8, 1)(X).shape == (8, 1)

