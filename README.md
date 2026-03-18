# 🧠 NLP Insight Studio — Smart Text Analysis Tool

> **Turn raw text into structured intelligence — instantly.**  
> A desktop-grade NLP application that performs sentiment analysis, entity recognition, and emotion prediction through a clean, modern GUI.

<br>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TextBlob](https://img.shields.io/badge/TextBlob-NLP-brightgreen?style=for-the-badge)
![spaCy](https://img.shields.io/badge/spaCy-NER-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## 📌 Overview

**NLPApp** is a fully functional desktop application that brings the power of Natural Language Processing to your fingertips — no cloud, no API keys, no internet required. Built with Python and a responsive Tkinter GUI, it provides real-time text analysis including sentiment scoring, named entity recognition, emotion detection, and more.

Designed with **clean architecture**, **secure user authentication**, and **exportable results**, NLPApp is built to be production-ready — not just a prototype.

---

## ✨ Features

### 🔐 User Authentication
- Secure **login and registration** system backed by a local JSON database
- Per-user session management and isolated analysis history

### 💬 Sentiment Analysis
- Powered by **TextBlob** — returns polarity score (`-1.0` to `+1.0`) and confidence level
- Classifies text as **Positive**, **Negative**, or **Neutral** with visual indicators

### 🏷️ Named Entity Recognition (NER)
- Powered by **spaCy** — extracts and categorizes entities such as `PERSON`, `ORG`, `GPE`, `DATE`, and more
- Structured entity table rendered directly in the GUI

### 🎭 Emotion Prediction
- Keyword-based emotion engine with intelligent **sentiment fallback**
- Detects emotions like Joy, Anger, Fear, Sadness, Surprise, and Disgust

### 📜 Analysis History
- All analyses are **auto-saved with timestamps** in a structured JSON store
- History is user-specific and fully browsable within the app

### 📤 Export Results
- One-click export of any analysis result as a **formatted `.txt` file**
- Includes all metadata: timestamp, sentiment score, entities, and detected emotion

### 🔢 Word & Character Counter
- Live counter updates as you type — tracks **word count**, **character count**, and **sentence count**

### 🖥️ Modern GUI
- Clean, **dark-themed** interactive interface built with Tkinter
- Responsive layout with tabbed navigation and clear visual hierarchy

---

1. **Text is submitted** via the GUI input panel
2. **TextBlob** computes polarity and subjectivity for sentiment scoring
3. **spaCy** runs `en_core_web_sm` to extract named entities and their labels
4. **Emotion engine** scans for emotion-keyword matches; falls back to sentiment polarity if no match is found
5. Results are rendered in structured panels and **persisted to the user's JSON history**

---
## ⚙️ Installation

**Prerequisites:** Python 3.10 or higher

```bash
# 1. Clone the repository
git https://github.com/mahimarani866
cd NLPApp

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download the spaCy language model
python -m spacy download en_core_web_sm
```

**`requirements.txt`**
```
textblob
spacy
tk
```

---

## ▶️ Usage

```bash
python main.py
```

1. **Register** a new account or **log in** with existing credentials
2. Enter or paste any text into the input panel
3. Click **Analyse** to run the full NLP pipeline
4. View **Sentiment**, **Entities**, and **Emotion** results in their respective tabs
5. Browse **History** to revisit past analyses
6. Click **Export** to save results as a `.txt` file

---

## 🚀 Future Improvements

- [ ] **Multilingual support** — extend sentiment & NER to 10+ languages via spaCy models
- [ ] **ML-based emotion classification** — replace keyword engine with a fine-tuned transformer model (e.g., `distilbert-base-uncased`)
- [ ] **Interactive data visualizations** — sentiment trend charts and entity frequency graphs using Matplotlib / Plotly
- [ ] **Batch file analysis** — upload `.txt` or `.csv` files for bulk NLP processing
- [ ] **Cloud sync** — optional Firebase/Supabase backend to sync history across devices
- [ ] **REST API mode** — expose core NLP functions as a local Flask/FastAPI endpoint
- [ ] **Dark/Light theme toggle** — user-selectable UI themes

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
# Open a Pull Request
```

Please follow [PEP 8](https://peps.python.org/pep-0008/) coding standards and include meaningful commit messages.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

<table>
  <tr>
    <td align="center">
      <strong>M Mahima Rani</strong><br/>
      <sub>Data Analyst · NLP Enthusiast · Python Developer</sub><br/><br/>
      <a href="https://github.com/mahimarani866">🐙 GitHub</a> &nbsp;|&nbsp;
      <a href="https://www.linkedin.com/in/m-mahima-rani/">💼 LinkedIn</a> &nbsp;|&nbsp;
      <a href="m.mahimarani866@gmail.com">📧 Email</a>
    </td>
  </tr>
</table>

> _Built with curiosity, caffeine, and a genuine love for making data meaningful._

---

<div align="center">
  <sub>⭐ If you found this project useful, consider giving it a star — it helps more than you think.</sub>
</div>