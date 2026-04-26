# Financial Planning App

A FastAPI application for financial planning.

## How to start this project locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/financial-planning-app.git
    cd financial-planning-app
    ```

2.  **Install dependencies:**
    Make sure you have Python 3.11+ and Poetry installed.
    ```bash
    poetry install
    ```

3.  **Run the application:**
    ```bash
    poetry run uvicorn app.main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

4.  **Run tests:**
    ```bash
    poetry run pytest
    ```

### Running with Docker

Alternatively, you can use Docker to run the application.

1.  **Build and run the Docker container:**
    ```bash
    docker-compose up --build
    ```
    The application will be available at `http://127.0.0.1:8000`.

## CI/CD Pipeline

This project uses GitHub Actions for CI/CD. The pipeline is configured to build and push a Docker image to the GitHub Container Registry (ghcr.io) on every push to the `main` branch.

### How it works

The workflow is defined in `.github/workflows/build-and-push.yml`. It performs the following steps:

1.  **Checks out the repository.**
2.  **Sets up Docker Buildx.**
3.  **Logs in to ghcr.io** using a `GITHUB_TOKEN`.
4.  **Builds the Docker image** using the `Dockerfile` in the root of the repository.
5.  **Pushes the image** to `ghcr.io/${{ github.repository }}:${{ github.sha }}`.

### Required GitHub Secrets

To enable the CI/CD pipeline, you need to ensure that your repository has the necessary permissions. No secrets are required for this pipeline to run, as it uses the default `GITHUB_TOKEN`. However, you need to ensure that your repository has package write permissions enabled.
