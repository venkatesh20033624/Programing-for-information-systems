# Programing-for-information-systems
# 💸Expenses Tracker

A lightweight Django-based web application that helps users track their personal expenses. The system supports full CRUD functionality and secure user authentication.

---

## 🚀 Features

- 👤 **User Registration & Login**
  - Secure password hashing
  - Session-based authentication

- 🧾 **Expense Management**
  - ✅ Create: Add new expenses with category, amount, and description
  - 📄 Read: View a list of your own past expenses
  - ✏️ Update: Edit expense details
  - ❌ Delete: Remove an expense permanently

- 🛡️ **User Isolation**
  - Each user only sees and manages **their own** expenses

---

## 📂 Tech Stack

- **Backend**: Python (Django)
- **Database**: SQLite (default for development)
- **Frontend**: HTML (Django templates), CSS
- **Auth**: Session-based

---

## 📌 Project Structure

smart_expenses/ ├── app.py # Main Django app logic ├── templates/ # HTML templates ├── static/ # Static assets ├── db.sqlite3 # SQLite database └── venv/ # Virtual environment


---

## 🔜 Deployment

This application will soon be deployed on an **AWS EC2 instance** for live access and testing.

---

## 🧑‍💻 Setup Instructions

1. Clone the repository
2. Create a virtual environment
3. Install required packages (`pip install django`)
4. Run the server:  
   ```bash
   python app.py runserver 0.0.0.0:8000

   
