<h1 align="center">🎙️ Interview Practice App</h1>

<p align="center">
  <b>A Flask-powered mock interview platform where you pick a subject, answer by voice, and get a score with feedback.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.1.0-000000?logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue" alt="License">
</p>

---

## 📌 Overview

**Interview Practice App** is a full-stack web application that helps students and job seekers rehearse interviews. Choose a subject, receive an interview question, record your spoken answer, submit it, and view a score with feedback and areas of improvement.

The backend is a lightweight **Flask REST API**, and the frontend is built with **HTML, CSS, and vanilla JavaScript**. This project was built as part of my **Decode Labs Internship**.

<!-- Add a screenshot or demo GIF here: ![Interview Practice App](screenshot.png) -->

---

## ✨ Features

- 🎯 **Six practice subjects:** Self Introduction, Generative AI, Python, English, HTML, and CSS
- ❓ **Subject-based questions** served by the API when the interview starts
- 🎙️ **Voice answers:** record in the browser and upload to the server
- 🔁 **Follow-up question flow** after every submitted answer
- 📊 **Feedback screen** with an animated circular score ring, written feedback, and areas of improvement
- 🌙 **Clean dark UI** with a responsive subject grid
- 🔌 **REST API** with CORS enabled

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask 3.1.0, Flask-CORS 5.0.0 |
| Frontend | HTML5, CSS3, JavaScript |
| Storage | Local `uploads/` folder for recorded audio |
| License | Apache-2.0 |

---

## ⚙️ How It Works

1. **Choose a subject** on the welcome screen.
2. **Start the interview.** The app calls `POST /start-interview` and shows the question.
3. **Record your answer** using your microphone.
4. **Submit.** The audio goes to `POST /submit-answer`, is saved on the server, and the next question comes back.
5. **End the interview and click Get Feedback.** The app calls `POST /get-feedback` and shows your score, feedback, and improvement tips.

---

## 📁 Project Structure

```
DecodeLabs-Internship-1/
├── app.py             # Flask backend and API routes
├── index.html         # Frontend UI and styling
├── index.js           # Frontend logic
├── requirements.txt   # Python dependencies
├── LICENSE            # Apache-2.0 license
└── README.md          # Project documentation
```

> The `uploads/` folder is created automatically when the app runs.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- A modern browser with microphone access

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/tejvarmaa-9458/DecodeLabs-Internship-1.git
cd DecodeLabs-Internship-1

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Open **http://127.0.0.1:5000** in your browser and allow microphone access when asked.

---

## 🔌 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serves the web app |
| `POST` | `/start-interview` | Takes a `subject` in JSON and returns an interview question |
| `POST` | `/submit-answer` | Takes an `audio` file (multipart form), saves it, and returns the next question |
| `POST` | `/get-feedback` | Returns the score, feedback, and areas of improvement |

**Example: `POST /start-interview`**

```json
// Request
{ "subject": "Python" }

// Response
{ "question": "Please introduce yourself and share your experience in Python." }
```

**Example: `POST /get-feedback`**

```json
{
  "success": true,
  "feedback": {
    "subject": "Python",
    "candidate_score": 4.5,
    "feedback": "You explained your ideas clearly and stayed relevant to the topic.",
    "areas_of_improvement": "Try speaking a little more confidently and give a few more practical examples."
  }
}
```

---

## 🔮 Future Improvements

- 🤖 Add speech-to-text and an AI model to evaluate answers (feedback is currently sample data)
- 👤 Add user accounts and interview history
- 📈 Track progress and scores over time
- 📚 Add more subjects, difficulty levels, and larger question banks
- 🌐 Deploy online so anyone can try it live

---

## 📜 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Mudunuri Tej Varma**
B.Tech 2nd Year, NIAT | Decode Labs Intern

- GitHub: [@tejvarmaa-9458](https://github.com/tejvarmaa-9458)
- LinkedIn: [Add your LinkedIn profile link here](https://www.linkedin.com/in/your-profile)

---

<p align="center">⭐ If you found this project helpful, please give it a star! ⭐</p>
