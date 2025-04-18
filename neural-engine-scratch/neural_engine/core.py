import torch
import torch.nn as nn

class GLUE(nn.Module):
    """Gated Linear Unit with Sigmoid gate."""
    def __init__(self, dim: int):
        super().__init__()
        self.proj = nn.Linear(dim, dim * 2, bias=True)

    def forward(self, x):
        a, b = self.proj(x).chunk(2, dim=-1)
        return a * torch.sigmoid(b)


class RMSNorm(nn.Module):
    """Root‑Mean‑Square Normalisation (scale‑only)."""
    def __init__(self, dim: int, eps: float = 1e-8):
        super().__init__()
        self.eps, self.scale = eps, nn.Parameter(torch.ones(dim))

    def forward(self, x):
        rms = torch.sqrt(torch.mean(x ** 2, dim=-1, keepdim=True) + self.eps)
        return self.scale * (x / rms)
