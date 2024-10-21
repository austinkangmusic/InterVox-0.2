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

### Step 6: Download faster-whisper models
```bash
python download_faster_whisper_models.py
```

### Step 7: Download XTTS models
```bash
python download_models.py
```

### Step 8: Run the Main Script
```bash
python main.py
```
