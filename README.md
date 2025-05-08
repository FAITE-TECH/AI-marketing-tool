# AI-marketing-tool

## Authentication Backend API

This repository contains the backend authentication API for the AI Marketing Tool. The API provides user authentication, authorization, and other backend services for the marketing platform.

## Deployment Instructions

### Prerequisites
- Docker and Docker Compose installed on the host machine
- Git for cloning the repository

### Deployment Steps

1. Clone the repository:
   ```
   git clone <repository-url>
   cd AI-marketing-tool
   ```

2. Environment Variables (optional):
   Create a `.env` file in the root directory with the following variables:
   ```
   SECRET_KEY=your-secure-secret-key
   OPENAI_API_KEY=your-openai-api-key
   ```

3. Build and start the services:
   ```
   docker-compose up -d
   ```

4. The API will be available at:
   ```
   http://localhost:8000
   ```

5. API Documentation available at:
   ```
   http://localhost:8000/docs
   ```

### Integration with Frontend

For frontend developers, the API is now available at `http://localhost:8000/api/v1`. The following endpoints are available for authentication:

- **Register**: `POST /api/v1/auth/register`
- **Login**: `POST /api/v1/auth/login`
- **Get Current User**: `GET /api/v1/users/me`

Check the API documentation at `/docs` for full details and request/response schemas.

## Development

For local development without Docker, follow these steps:

1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Navigate to the backend directory: `cd backend`
4. Run the application: `python -m src.app.main`

## Troubleshooting

If you encounter issues with database connections, ensure that:
1. PostgreSQL is running (check with `docker-compose ps`)
2. The database credentials in the environment match those in `docker-compose.yml`