# Neural‑Engine‑Scratch

Minimal PyTorch prototype featuring GLUE activation, RMSNorm, RMSProp, L2 weight‑decay and gradient clipping.  
Suitable for low‑VRAM experimentation (≤ 6 GB GPUs).

## Usage
```bash
python -m venv .venv && .\.venv\Scripts\activate
pip install -r requirements.txt
python main.py     # train on synthetic data
pytest -q          # run smoke tests

