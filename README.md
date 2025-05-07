# Reproducing and Extending UniXGen

This repository contains the code and scripts needed to reproduce and extend the UniXGen model from the paper "Vision-Language Generative Model for View-Specific Chest X-ray Generation":

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LoganCheng0525/CS598-DL4H.git

2. **Set up environment:**:
   ```bash
   pip install -r requirements.txt

3. **Dependencies/packages needed:**:

| Library / Package                   | Version                      |
|-------------------------------------|------------------------------|
| torch, torchvision                  | 1.7.1+cu110, 0.8.2+cu110     |
| pytorch-lightning                   | 1.4.0                        |
| transformers                        | 4.9.1                        |
| tokenizers                          | 0.10.3                       |
| taming-transformers-rom1504         | 0.0.6                        |
| omegaconf                           | 2.1.0                        |
| numpy, pandas                       | 1.23.4, 1.5.1                |
| scikit-image, scipy                 | 0.19.3, 1.9.3                |
| matplotlib                          | 3.6.2                        |
| tqdm                                | 4.64.1                       |
| torchxrayvision                     | 0.0.39                       |
| wandb                               | 0.13.5                       |
| CUDA Toolkit                        | 11.0                         |

## Dataset
Download MIMIC-CXR-JPG images & reports.
You must be a credential user defined in PhysioNet to access the data.
Download chest X-rays from MIMIC-CXR-JPG.
Download reports from MIMIC-CXR Database.

## Train Models
```python unified_main.py```

## Test Models
Run unified_run.py.
The generated discrete code sequences are saved as files.
```python unified_run.py```

#### For decoding chest X-rays
Run decode_cxr.py.
```python decode_cxr.py```

#### For decoding chest X-rays
Run decode_report.py.
```python decode_report.py```
