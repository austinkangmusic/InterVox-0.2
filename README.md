<h1 style="font-size: 36px; text-align: center;">InterVox</h1>
<img src="photo.png" width="500" style="float: left; margin-right: 20px;"/>
<p style="font-size: 16px;">
  InterVox is a cutting-edge system that combines advanced TTS, STT, and LLM technologies for a highly interactive and dynamic conversation experience. It allows both user and system interruptions, creating a fluid interaction.
</p>

<ul style="font-size: 16px;">
  <li><strong>STT:</strong> Powered by <strong>faster-whisper</strong>, an efficient model for real-time transcription.</li>
  <li><strong>TTS:</strong> Uses <strong>Coqui-TTS</strong> to deliver natural, human-like speech.</li>
  <li><strong>LLM:</strong> Integrated with platforms like <strong>Ollama</strong>, <strong>Groq</strong>, and <strong>OpenAI's GPT</strong> for intelligent, context-aware conversation handling.</li>
  <li>Enables immersive interaction with the ability to interrupt and be interrupted smoothly in a natural flow.</li>
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
