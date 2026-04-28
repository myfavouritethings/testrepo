# Full-Stack Budgeting Application

This repository contains the foundational structure for a full-stack budgeting web application. It includes a React frontend, a Python (FastAPI) backend, and a complete development and deployment setup using Docker and GitHub Actions.

## Project Structure

```
.
├── .github/workflows/      # GitHub Actions CI/CD pipelines
│   └── build-and-push.yml
├── backend/                # FastAPI backend application
│   ├── main.py
│   ├── test_main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/               # React frontend application
│   ├── src/
│   ├── package.json
│   └── vite.config.js
├── .agent-config.yml       # Agent configuration (do not modify)
├── Dockerfile              # Production multi-stage Dockerfile
├── docker-compose.yml      # Docker Compose for local development
└── README.md
```

## Local Development

To run this application locally, you need to have Docker and Docker Compose installed.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/<your-username>/<your-repository>.git
    cd <your-repository>
    ```

2.  **Run the application using Docker Compose:**
    ```bash
    docker-compose up --build
    ```

    This command will build the Docker images for both the frontend and backend services and start the containers.

3.  **Access the application:**
    *   The frontend will be available at [http://localhost:5173](http://localhost:5173).
    *   The backend API will be available at [http://localhost:8000](http://localhost:8000).

The frontend is configured with hot-reloading, so any changes you make to the code in the `frontend/` directory will be reflected in your browser immediately. The backend also supports hot-reloading.

### Running Tests

**Backend:**

To run the backend tests, you can execute them inside the running `backend` container:

```bash
docker-compose exec backend pytest
```

**Frontend:**

To run the frontend tests, you can execute them inside the running `frontend` container:

```bash
docker-compose exec frontend npm test
```

## CI/CD Pipeline

This project is configured with a GitHub Actions workflow (`.github/workflows/build-and-push.yml`) that automatically builds and pushes a production-ready Docker image to the GitHub Container Registry (ghcr.io).

### How it Works

1.  **Trigger:** The workflow is triggered on every push to the `main` branch.
2.  **Login:** It logs into `ghcr.io` using a temporary `GITHUB_TOKEN`.
3.  **Build & Push:** It builds the multi-stage production `Dockerfile` and pushes the resulting image to `ghcr.io`.
4.  **Tagging:** The image is tagged with two tags:
    *   The git commit SHA (e.g., `ghcr.io/user/repo:a1b2c3d`) for immutability.
    *   `latest` for easy access to the most recent version.

### Required GitHub Secrets

The workflow uses the standard `GITHUB_TOKEN`, which is automatically provided by GitHub. **No additional secrets need to be configured** for the build-and-push pipeline to work. Your container images will be private to your repository by default.

To make the package public, go to your repository's main page, find the "Packages" section on the right-hand side, click on your container image, go to "Package settings", and change the visibility to "Public".
