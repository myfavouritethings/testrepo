# Stage 1: Build the frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json* ./
# Use ci instead of install for reproducible builds
RUN npm ci
COPY frontend/ ./
RUN npm run build

# Stage 2: Install backend dependencies
FROM python:3.11-slim AS backend-builder
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 3: Final production image
FROM python:3.11-slim
WORKDIR /app

# Copy backend code and dependencies
COPY --from=backend-builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY backend/ ./

# Copy built frontend to the 'static' directory
COPY --from=frontend-builder /app/frontend/dist /app/static

EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
