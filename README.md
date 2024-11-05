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

## 📂 1. Repository Setup

### Clone the Repository
```bash
D:\Utilities\Git\Git\bin\git.exe -c http.sslVerify=false clone https://github.com/austinkangmusic/InterVox-0.2.git
```

### Navigate to the Project Directory
```bash
cd InterVox-0.2
```

---

## ⚙️ 2. Virtual Environment Setup

### Create Virtual Environment (No Activation Needed)
```bash
& "D:\Utilities\python310\python.exe" -m venv venv
```

### Verify Python Executable Path
Ensure the path points to your environment's Python executable:
```bash
Resolve-Path .\venv\Scripts\python.exe
```

### Check Python Version (Recommended: 3.10.0)
```bash
.\venv\Scripts\python.exe --version
```

### Activate Virtual Environment
```bash
# Windows
venv\Scripts\Activate

# Mac/Linux
source venv/bin/activate
```

---

## 📦 3. Install Dependencies

Install all required packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 🔽 4. Download Models

### Download Faster-Whisper Models
Run the following script to download Faster-Whisper models:
```bash
python download_faster_whisper_models.py
```

### Download XTTS-v2 Models
Run the script below to download XTTS-v2 models:
```bash
python download_XTTS-v2_models.py
```

---

## 🎬 5. Running the Main Script

Finally, start the main script to launch the project:
```bash
python main.py
```

---

## 📝 Additional Information

- **Troubleshooting**: If you encounter issues, refer to the Troubleshooting section below.
- **Contributing**: Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
- **License**: This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy Coding! 🚀
```

### Key Points for a Nice README
1. **Emojis for Icons**: Emojis add visual structure, making it easier to follow steps at a glance.
2. **Code Blocks**: Code snippets for each command allow easy copying and prevent formatting errors.
3. **Sections with Headers**: Organized sections like *Repository Setup* and *Virtual Environment Setup* help keep the document easy to navigate.
4. **Additional Information**: Including sections for troubleshooting, contribution guidelines, and license information at the end adds professionalism and utility.

This template should help make your README both informative and visually appealing!
