# Financial Planning App

This is a FastAPI-based application for financial planning.

## Setup and Installation

This project uses Poetry for dependency management. Make sure you have Poetry installed.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd financial-planning-app
    ```

2.  **Install dependencies:**
    ```bash
    poetry install
    ```

## Running the Local Development Server

To run the application locally, use the following command:

```bash
poetry run uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

### Running with Docker

Alternatively, you can run the application using Docker Compose:

```bash
docker-compose up --build
```

## Running Tests

To run the test suite, use `pytest`:

```bash
poetry run pytest
```

## Project Structure

-   `app/`: Main application directory.
    -   `main.py`: FastAPI application instance and root endpoint.
    -   `routers/`: Directory for modular API routers.
-   `tests/`: Test files.
-   `pyproject.toml`: Project metadata and dependencies.
-   `Dockerfile`: For containerizing the application.
-   `docker-compose.yml`: For local Docker-based development.
-   `.github/workflows/build-and-push.yml`: GitHub Actions workflow for CI/CD.
-   `README.md`: This file.

## Linting and Formatting

This project uses `ruff` for linting and `black` for code formatting.

-   **Check for linting errors:**
    ```bash
    poetry run ruff check .
    ```

-   **Fix linting errors:**
    ```bash
    poetry run ruff check . --fix
    ```

-   **Format code:**
    ```bash
    poetry run black .
    ```

## Deployment

This project includes a GitHub Actions workflow to automatically build and push a Docker image to the GitHub Container Registry (ghcr.io).

### How it Works

On every push to the `main` branch, the `.github/workflows/build-and-push.yml` workflow is triggered. It performs the following steps:

1.  **Checks out the code.**
2.  **Logs into `ghcr.io`:** Authenticates using a temporary `GITHUB_TOKEN`.
3.  **Builds and pushes the image:** Builds the Docker image and tags it with the Git SHA, then pushes it to `ghcr.io` under the repository's package namespace.

### Required GitHub Secrets

No secrets need to be set for this to work. The `GITHUB_TOKEN` is automatically provided by GitHub Actions.
