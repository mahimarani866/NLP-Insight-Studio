# NLP Insight Studio 🧠

A Python desktop application that analyzes text using NLP techniques — built with Tkinter, TextBlob, and spaCy.

---

## Features

- 🔐 **User Authentication** — Login and registration stored in a local JSON database
- 💬 **Sentiment Analysis** — Detects positive, negative, or neutral tone using TextBlob
- 🏷️ **Named Entity Recognition** — Extracts people, places, and organizations using spaCy
- 🎭 **Emotion Prediction** — Identifies emotions via keyword-based logic
- 📜 **Analysis History** — Saves past results with timestamps in a JSON file
- 📤 **Export Results** — Save any analysis output as a `.txt` file
- 🔢 **Word & Character Counter** — Live count as you type

---

## Project Structure

```
NLP-Insight-Studio/
│
├── app.py              # Main GUI (Tkinter)
├── myapi.py            # NLP logic (sentiment, NER, emotion)
├── mydb.py             # User auth and history (JSON)
├── requirements.txt    # Dependencies
└── README.md
```

---

## Installation

**Requirements:** Python 3.8 or above

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/NLP-Insight-Studio.git
cd NLP-Insight-Studio

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download the spaCy language model
python -m spacy download en_core_web_sm
```

**`requirements.txt`**
```
textblob
spacy
```

---

## How to Run

```bash
python app.py
```

1. Register a new account or log in
2. Type or paste any text into the input box
3. Click **Analyze** to see results
4. View history or export the output as needed

---

## Technologies Used

| Tool | Purpose |
|---|---|
| Python + Tkinter | GUI application |
| TextBlob | Sentiment analysis |
| spaCy | Named entity recognition |
| JSON | User data and history storage |

---

## Author

** M Mahima Rani**
🎓 Student · Python Developer
[GitHub](https://github.com/mahimarani866) · [LinkedIn](https://linkedin.com/in/m-mahima-rani/)

---

> Made with Python as a personal NLP project.
