
# 📝 Simple ToDo App

A simple ToDo application built with a minimal frontend and a Django backend.  
This project is designed for **beginners** who want hands-on practice with Django, authentication, and basic CRUD operations.

## ✨ Features

- User signup and login
- Create new todos
- Mark todos as done
- Delete todos
- Home and profile pages
- Simple and clean UI

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django
- **Database:** SQLite
- **Containerization:** Docker & Docker Compose

## 🎯 Target Audience

This project is intended for:
- Beginners learning Django
- Developers practicing authentication and CRUD
- Training and educational purposes

## 🚀 Getting Started

You can run the project easily using **Docker Compose**.

### Prerequisites

Make sure you have the following installed:

- Docker
- Docker Compose

### Installation & Run

Clone the repository:

```bash
git clone https://github.com/MahdiLatifi/TodoApp.git
cd TodoApp
````

Build and run the project using Docker Compose:

```bash
docker-compose up --build
```

Once the containers are running, open your browser and go to:

```
http://localhost:8000
```

## 📂 Project Structure

```text
.
├── apps/
│   ├── todo/          # Todo app (models, views, urls)
│   └── user_auths/    # Authentication app (signup, login)
├── templates/         # HTML templates
├── static/            # CSS, JS, static files
├── todo_app/          # Main Django project settings
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── .gitignore
└── README.md

```

## 🔐 Environment Variables

No environment variables are required for this project.

## 📌 Roadmap (Optional Ideas)

* [ ] Improve UI styling
* [ ] Add due dates for todos
* [ ] Add categories or tags
* [ ] Add tests
* [ ] Deploy to production

## 🤝 Contributing

This is a beginner-friendly project, and contributions are welcome!

If you want to contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute this project.

## 👤 Author

**Mahdi Latifi**
GitHub: [@MahdiLatifi](https://github.com/MahdiLatifi)

