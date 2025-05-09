import os, torch, pathlib, sys
print("CWD :", pathlib.Path('.').resolve())
print("img dir exists:", pathlib.Path('data/raw/p10').exists())
print("report dir exists:", pathlib.Path('data/raw/p10_report').exists())
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
