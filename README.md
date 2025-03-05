# ToDo-API
This is a To-Do List API built using Django REST Framework (DRF) with JWT authentication. Users can sign up, log in, and manage their to-do tasks securely.
# 📋 To-Do App Backend (Django REST Framework)

This is a **To-Do List API** built using **Django REST Framework (DRF)** with **JWT authentication**. Users can **sign up, log in, and manage** their to-do tasks securely.

## 🔹 Features
- ✅ **User Authentication** (Signup, Login, Logout with JWT)
- 🔐 **JWT Token-based Authentication** (Access & Refresh Tokens)
- ✏️ **CRUD Operations for To-Dos** (Create, Read, Update, Delete)
- 🚪 **Token Blacklisting for Secure Logout**
- 🔑 **Permissions & Access Control** (Only authenticated users can manage their tasks)

## 🚀 Tech Stack
- **Django** & **Django REST Framework**
- **Simple JWT for Authentication**
- **SQLite/PostgreSQL (Configurable)**

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/todo-backend.git
cd todo-backend
```

### 2️⃣ Create a Virtual Environment and Activate It
```bash
python -m venv venv
```

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create a Superuser (Optional for Admin Access)
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server
```bash
python manage.py runserver
```

---





