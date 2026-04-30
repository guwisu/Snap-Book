# Snap-Book ![GitHub License](https://img.shields.io/github/license/guwisu/Snap-Book)

<div>
  <img height="60" alt="fastapi-logo" src="https://github.com/user-attachments/assets/24ce8412-0134-4e04-b318-2ffdbd089783" />
  <img height="60" alt="postgres" src="https://github.com/user-attachments/assets/50d93513-e2e4-4b64-870c-ea685607616c" />
  <img height="60" alt="sql-alchemy" src="https://github.com/user-attachments/assets/3171fa47-ef65-4ba3-aca2-4f179f7b9147" />
  <img height="50" alt="docker-mark-ocean-blue" src="https://github.com/user-attachments/assets/80906a73-2fe6-46ac-a94a-51448f6e40c6" />
</div>



Snap-Book is a backend service for hotel room reservations. The service provides user authentication and authorization, hotel and room management, booking functionality, and facilities catalog. The project includes database migration management, background task processing, containerized deployment, automated testing, and CI/CD pipeline.


## Features

- User registration, login, and logout
- Create, update, and delete hotels and rooms
- Create and view bookings
- View and add facilities
- Asynchronous background task processing
- RESTful API built with FastAPI
- Database migrations support
- Containerized environment with Docker
- Automated testing with Pytest
- CI/CD pipeline


## Tech Stack

- Python  
- FastAPI  
- PostgreSQL  
- SQLAlchemy  
- Alembic  
- Celery  
- Redis  
- Docker / Docker Compose  
- Pytest  
- GitLab CI/CD  
- Poetry

## Project Structure
```
Snap-Book/
├── src/
│   ├── api/
│   ├── connectors/
│   ├── migrations/
│   ├── models/
│   ├── repositories/
│       └── mappers/
│   ├── schemas/
│   ├── services/
│   ├── tasks/
│   └── utils/
├── tests/
│   ├── integration_tests/
│   └── unit_tests/
└── docs/
```

## Installation

1. Clone the repository.
```bash
git clone https://github.com/guwisu/Snap-Book.git
cd Snap-Book
```
2. Copy environment variables file.
```bash
cp .env.example .env
```
3. Build containers with Docker.
```bash
docker-compose build
docker-compose up -d
```
4. Access the API.
```bash
http://localhost:8000/docs
```

## Interactive API Documentation

The project includes automatic API documentation via FastAPI's Swagger UI.

<img width="1919" height="915" alt="Snap-Book_1" src="https://github.com/user-attachments/assets/d306aee8-abed-4b35-b7c5-0d1e91a74208" />
<img width="1919" height="802" alt="Snap-Book_2" src="https://github.com/user-attachments/assets/d0fde3ca-7397-4840-a286-76e23d72d546" />

## License

This project is under the MIT license.
