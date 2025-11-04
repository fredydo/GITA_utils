# 🎙️ DisVoice Feature Extraction Utilities

This repository provides utility scripts to extract speech features using the [DisVoice](https://github.com/jcvasquezc/disvoice) toolkit.
It supports extracting **prosody**, **articulation**, **phonation**, and **glottal** features from `.wav` files.

---

## 🧩 Requirements

* **Python 3.8.10**
* `pip`, `venv` (or `conda`)
* Windows, macOS, or Linux

---

## ⚙️ Environment Setup

You can create a clean environment using either **Conda** or **Pyenv**.

### Option 1 — Conda (recommended)

```bash
conda create -n disvoice python=3.8.10
conda activate disvoice
```

### Option 2 — Pyenv

```bash
pyenv install 3.8.10
pyenv virtualenv 3.8.10 disvoice
pyenv activate disvoice
```

---

## 📦 Installation

You can install all the necessary packages with:

```bash
pip install -r requirements.txt
```

Alternatively, if you prefer manual installation, you can run the key steps individually:

```bash
pip install praat-parselmouth
python -m pip install --upgrade pip setuptools wheel
pip install disvoice
```

## 🧠 Usage

Run the feature extraction script:

```bash
python scripts/feature_extraction/extract_features.py \
  --wav-dir ./audios/ \
  --output-dir ./features/
```

The script will:

* Process all `.wav` files in `--wav-dir`
* Extract **prosody**, **articulation**, **phonation**, and **glottal** features
* Save outputs as compressed `.npz` files under `features/disvoice/`

If extraction for a file fails, an error report will be saved, and processing will continue with the next file.

---