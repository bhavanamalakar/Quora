# 🧠 Quora Clone - Django Based Q&A Platform

This is a simple **Quora-like web app** built using **Django** and **PostgreSQL**. Users can register, post questions, answer others' questions, like answers, and view content with original formatting (line breaks, indentation, etc.).

---

## 🚀 Features

- ✅ User Registration & Login
- ✅ Post & View Questions
- ✅ Answer Questions
- ✅ Like/Unlike Answers
- ✅ Answers Keep Formatting (spaces, newlines)
- ✅ Logout Functionality

---

## 🛠 Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, Bootstrap
- **Database**: PostgreSQL

---

## 🧑‍💻 Getting Started

### Clone the repository
```bash
git clone https://github.com/your-username/quora-clone.git
cd quora-clone

python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
