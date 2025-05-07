# Reproducing and Extending UniXGen

This repository contains the code and scripts needed to reproduce and extend the UniXGen model from the paper "Vision-Language Generative Model for View-Specific Chest X-ray Generation":

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LoganCheng0525/CS598-DL4H.git

2. **Set up environment:**:
   ```bash
   pip install -r requirements.txt

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
