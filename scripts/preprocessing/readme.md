# Audio Segment Cutter

This script automates cutting audio segments based on a CSV file that defines start and end times. It uses **FFmpeg** for fast, lossless trimming.

---

## 🧩 1. Requirements

Before running the script, make sure you have:

* **Python 3.8+**
* **FFmpeg** installed and accessible from your system path
  (you can verify with `ffmpeg -version`)
* The following Python packages:

```bash
pip install pandas ffmpeg-python
```

---

## ⚙️ 2. Usage

Run the script from the command line:

```bash
python cut_audios.py \
    --csv "AtHome segments.csv" \
    --base-dir "AtHome to share" \
    --output-folder "segmented" \
    --sep ";" \
    --decimal ","
```

### Arguments

| Argument          | Description                                             | Default                   |
| ----------------- | ------------------------------------------------------- | ------------------------- |
| `--csv`           | Path to the CSV file containing audio segment info      | `"AtHome segments.csv"`   |
| `--base-dir`      | Base directory for the audio files                      | current working directory |
| `--output-folder` | Folder name for output (replaces `"original"` in paths) | `"segmented"`             |
| `--sep`           | CSV separator                                           | `";"`                     |
| `--decimal`       | Decimal separator                                       | `","`                     |

---

## 🧾 3. CSV Format

The input CSV should include at least the following columns:

| Column  | Description                                 |
| ------- | ------------------------------------------- |
| `Path`  | Relative path to the input `.wav` file      |
| `Start` | Start time in seconds                       |
| `End`   | End time in seconds                         |
| `Task`  | Segment task name (used in output filename) |

Example:

| Path                                                 | Start | End  | Task |
| ---------------------------------------------------- | ----- | ---- | ---- |
| `Database/AtHome/Session4/original/049PD_AHS4_3.wav` | 1.23  | 3.45 | DDK1 |

---

## 🧪 4. Example Output

```
[3/120] Cutting 049PD_AHS4_3.wav: 1.23 - 3.45s → 049PD_AHS4_3_DDK1.wav
Saved: AtHome to share/Database/AtHome/Session4/segmented/049PD_AHS4_3_DDK1.wav
```

---

## ⚠️ 5. Error Handling

If a file cannot be found or FFmpeg fails, the script will print a warning but continue processing the remaining rows.

Example:

```
[5/120] File not found: Database/AtHome/Session5/original/missing.wav
ffmpeg error for 049PD_AHS5_1.wav
------------------------------------------------------------
```

---

## 🎧 6. Copy Selected Audios

This utility copies all `.wav` files whose filenames contain one or more given **keywords**.
It is useful for organizing subsets of recordings, such as tasks like *Fugu*, *Phonological*, or *Semantic*.

---

### 🧩 Requirements

* **Python 3.8+**

No extra libraries are needed (uses only Python standard library).

---

### ⚙️ Usage

```bash
python copy_selected_audios.py \
    --source "AtHome to share" \
    --dest "AtHome to share/All_Selected_Audios" \
    --keywords fugu phonological1 phonological2 semantic1 semantic2 \
    --preserve-structure
```

### Arguments

| Argument               | Description                                                 | Default  |
| ---------------------- | ----------------------------------------------------------- | -------- |
| `--source`             | Source directory to search recursively for `.wav` files     | Required |
| `--dest`               | Destination folder for copied files                         | Required |
| `--keywords`           | One or more case-insensitive keywords to match in filenames | Required |
| `--preserve-structure` | If set, preserves original folder hierarchy in destination  | `False`  |

---

### 🧪 Example Output

```
Found 1086 .wav files in AtHome to share

[1] Copied: Database/AtHome/Session4/segmented/049PD_AHS4_3_Fugu.wav → All_Selected_Audios/049PD_AHS4_3_Fugu.wav
[2] Copied: Database/AtHome/Session5/segmented/050HC_AHS5_1_semantic1.wav → All_Selected_Audios/050HC_AHS5_1_semantic1.wav

Done! Copied 25 files matching ['fugu', 'phonological1', 'phonological2', 'semantic1', 'semantic2'].
```

---

### ⚠️ Notes

* Matching is **case-insensitive** (e.g., `Fugu`, `fugu`, `FUGU` are all valid).
* If `--preserve-structure` is used, the original directory structure under the source folder will be recreated in the destination.
* Files that do not match any of the provided keywords are ignored.
