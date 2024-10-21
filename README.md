My bad! Here's the updated version with the `mkdir` step included:

---

# 🚀 **InterVox-0.2 Installation Guide**

### Step 1: Clone the **InterVox-0.2** Repository
```bash
git clone https://github.com/austinkangmusic/InterVox-0.2.git
```

### Step 2: Navigate to the Project Directory
```bash
cd InterVox-0.2
```

### Step 3: Set Up and Activate Virtual Environment
```bash
& "D:\Private Server\Apps\PYTHON VERSIONS\python310\python.exe" -m venv venv
venv/Scripts/Activate
```

### Step 4: Verify Python Executable Path
```bash
Resolve-Path .\venv\Scripts\python.exe
```

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

---

# 🌐 **Download Whisper Models**

### Step 1: Create a Directory for Whisper Models
```bash
mkdir faster_whisper_models
```

<details>
  <summary>Whisper Tiny.en</summary>

  ```bash
  git clone https://huggingface.co/Systran/faster-whisper-tiny.en faster_whisper_models/tiny
  ```
</details>

<details>
  <summary>Whisper Base.en</summary>

  ```bash
  git clone https://huggingface.co/Systran/faster-whisper-base.en faster_whisper_models/base.en
  ```
</details>

<details>
  <summary>Whisper Small.en</summary>

  ```bash
  git clone https://huggingface.co/Systran/faster-whisper-small.en faster_whisper_models/small.en
  ```
</details>

<details>
  <summary>Whisper Medium.en</summary>

  ```bash
  git clone https://huggingface.co/Systran/faster-whisper-medium.en faster_whisper_models/medium.en
  ```
</details>

<details>
  <summary>Whisper Large.en</summary>

  ```bash
  git clone https://huggingface.co/Systran/faster-whisper-large-v2 faster_whisper_models/large.en
  ```
</details>

---

### Step 6: Download XTTS models
```bash
python download_models.py
```

### Step 6: Run the Main Script
```bash
python main.py
```
