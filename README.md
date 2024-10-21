<h1 style="font-size: 36px; text-align: center;">InterVox</h1>
<img src="photo.png" width="500" style="float: left; margin-right: 20px;"/>
<p style="font-size: 16px;">
  This system combines advanced TTS and STT technologies for a smooth, interactive experience. It allows both interruptions from the user and the system, creating a dynamic conversation flow.
</p>

<ul style="font-size: 16px;">
  <li><strong>STT:</strong> Powered by <strong>faster-whisper</strong>, known for fast, accurate transcription in real time.</li>
  <li><strong>TTS:</strong> Uses <strong>Coqui-TTS</strong> for natural, human-like speech output.</li>
  <li>Enables immersive interaction with the ability to interrupt and be interrupted in conversation.</li>
</ul>

---

### **🚀 1. Repository Setup:**
- **Clone the Repository**  
   ```bash
   git clone https://github.com/austinkangmusic/InterVox-0.2.git
   ```

- **Navigate to the Project Directory**  
   ```bash
   cd InterVox-0.2
   ```

---

### **⚙️ 2. Virtual Environment Setup:**
- **Set Up Virtual Environment (No Activation)**  
   ```bash
   & "D:\Private Server\Apps\PYTHON VERSIONS\python310\python.exe" -m venv venv
   ```

- **Verify Python Executable Path**  
   ```bash
   Resolve-Path .\venv\Scripts\python.exe
   ```

- **Check Python Version (Should be 3.10.0)**  
   ```bash
   .\venv\Scripts\python.exe --version
   ```

- **Activate Virtual Environment**  
   ```bash
   venv/Scripts/Activate
   ```

---

### **📦 3. Dependencies Installation:**
- **Install Required Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

### **🔽 4. Model Downloads:**
- **Download Faster-Whisper Models**  
   ```bash
   python download_faster_whisper_models.py
   ```

- **Download XTTS-v2 Models**  
   ```bash
   python download_XTTS-v2_models.py
   ```

---

### **🎬 5. Running the Main Script:**
- **Run the Main Script**  
   ```bash
   python main.py
   ```
