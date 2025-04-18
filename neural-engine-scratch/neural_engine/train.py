import torch
import torch.nn as nn
from torch.nn.utils import clip_grad_norm_

def train(model, X, y, *, epochs=800, lr=5e-3,
          weight_decay=1e-4, clip_norm=1.0, gamma=0.995,
          device=None):
    device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    X, y = X.to(device), y.to(device)

    criterion = nn.MSELoss()
    optim = torch.optim.RMSprop(model.parameters(), lr=lr,
                                alpha=0.99, eps=1e-8,
                                weight_decay=weight_decay)
    sched = torch.optim.lr_scheduler.ExponentialLR(optim, gamma=gamma)

    for epoch in range(1, epochs + 1):
        optim.zero_grad()
        loss = criterion(model(X), y)
        loss.backward()
        clip_grad_norm_(model.parameters(), clip_norm)
        optim.step()
        sched.step()
        if epoch % 100 == 0:
            print(f"[{epoch:04d}] loss={loss.item():.6f} lr={sched.get_last_lr()[0]:.5f}")
