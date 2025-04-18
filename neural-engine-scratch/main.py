import torch
from neural_engine.model import DenseGLUERMSNN
from neural_engine.train import train      # in main.py only

if __name__ == "__main__":
    torch.manual_seed(42)
    N, in_d, hid_d, out_d = 400, 3, 64, 1
    X = torch.rand(N, in_d)
    y = (X.sum(dim=1, keepdim=True) * 0.8).float()

    net = DenseGLUERMSNN(in_d, hid_d, out_d)
    train(net, X, y)

    net.eval()
    with torch.no_grad():
        print("\nSample preds:\n", net(X[:5]))
