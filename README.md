---

### **1. 🚀 Repository Setup:**
   **Clone the Repository**  
   ```bash
   git clone https://github.com/austinkangmusic/InterVox-0.2.git
   ```

2. **Navigate to the Project Directory**  
   ```bash
   cd InterVox-0.2
   ```

---

### **⚙️ Virtual Environment Setup:**
3. **Set Up Virtual Environment (No Activation)**  
   ```bash
   & "D:\Private Server\Apps\PYTHON VERSIONS\python310\python.exe" -m venv venv
   ```

4. **Verify Python Executable Path**  
   ```bash
   Resolve-Path .\venv\Scripts\python.exe
   ```

5. **Check Python Version (Should be 3.10.0)**  
   ```bash
   .\venv\Scripts\python.exe --version
   ```

6. **Find Python Executable in VS Code**  
   In VS Code, select the interpreter from `venv/Scripts/python.exe`.

7. **Activate Virtual Environment**  
   ```bash
   venv/Scripts/Activate
   ```

---

### **📦 Dependencies Installation:**
8. **Install Required Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

### **🔽 Model Downloads:**
9. **Download Faster-Whisper Models**  
   ```bash
   python download_faster_whisper_models.py
   ```

10. **Download XTTS Models**  
    ```bash
    python download_models.py
    ```

---

### **🎬 Running the Main Script:**
11. **Run the Main Script**  
    ```bash
    python main.py
    ```

---
