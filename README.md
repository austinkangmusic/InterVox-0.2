<img src="photo.png" width="500" style="float: left; margin-right: 20px;"/>
<p style="font-size: 16px;">
  This system is a cutting-edge implementation of both Text-to-Speech (TTS) and Speech-to-Text (STT) technologies, designed to allow natural, fluid conversation between users and machines. The system supports a seamless, two-way interaction, where you can both interrupt and be interrupted, creating a more dynamic and responsive communication flow.
</p>

<p style="font-size: 16px;">
  For the Speech-to-Text (STT) functionality, the system employs <strong>faster-whisper</strong>, an advanced, open-source model known for its high accuracy and rapid transcription. This enables the system to quickly and accurately convert spoken words into text, even in real-time conversations. Its ability to handle background noise and accents makes it highly adaptable to different environments and speakers.
</p>

<p style="font-size: 16px;">
  On the Text-to-Speech (TTS) side, the system uses <strong>Coqui-TTS</strong>, another open-source solution renowned for its high-quality, natural-sounding voices. Coqui-TTS can generate speech in various tones and styles, making the interaction feel more human-like and engaging. This combination of faster-whisper for STT and Coqui-TTS for TTS ensures an advanced, real-time conversational experience.
</p>

<p style="font-size: 16px;">
  Together, these technologies enable a highly interactive environment where the user can not only speak to the system but also engage in dynamic conversations. Whether you want to ask questions, give commands, or interrupt the system, the interaction feels smooth and natural, breaking the barrier between humans and machines.
</p>

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
