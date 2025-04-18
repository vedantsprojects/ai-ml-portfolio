import torch.nn as nn
from .core import GLUE, RMSNorm

class DenseGLUERMSNN(nn.Module):
    """Linear → GLUE → RMSNorm → Linear (regression head)."""
    def __init__(self, in_dim: int, hidden_dim: int, out_dim: int):
        super().__init__()
        self.fc1  = nn.Linear(in_dim, hidden_dim)
        self.glu  = GLUE(hidden_dim)
        self.norm = RMSNorm(hidden_dim)
        self.fc2  = nn.Linear(hidden_dim, out_dim)

    def forward(self, x):
        return self.fc2(self.norm(self.glu(self.fc1(x))))
