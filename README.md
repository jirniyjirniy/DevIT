# DevIT — Incident Management System

DevIT — это backend-сервис на Django для отслеживания и анализа инцидентов. Он реализует API для регистрации, обработки и мониторинга возможных коллизий между объектами в реальном времени.

---

## ⚙️ Стек технологий

- Python 3.11+
- Django 5.2+
- PostgreSQL
- Docker / Docker Compose
- Django REST Framework
- drf-yasg — Swagger UI документация
- Gunicorn — WSGI для продакшена
- Nginx — прокси и раздача статики

---

## 🚀 Быстрый старт

### 1. Клонируй репозиторий

```bash
git clone https://github.com/jirniyjirniy/DevIT.git
cd DevIT
cp .env_example .env
```

### 2. Запусти проект

```bash
docker-compose up --build
```

Проект станет доступен на:

- `http://localhost:8000/swagger/` — Swagger UI
- `http://localhost:8000/admin/` — Django Admin

---

## 📁 Архитектура проекта

```
DevIT/
├── incidents/
│        └── api/
│            ├── serializers.py
│            ├── views.py
│            └── urls.py
│       ├── models
│       └── tests/
│            ├── test.py
├── incident_manager/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── docker/
│   └── nginx.conf
├── staticfiles/
├── templates/
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md
```

---

## 🧪 Тестирование

```bash
docker-compose exec web pytest
```

---

## 📚 Документация API

Swagger UI доступен по адресу:

```
http://localhost:8000/swagger/
```

---

## 🧩 Переменные окружения

Смотри `.env_example`:

```env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
POSTGRES_DB=incidents_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
```

---