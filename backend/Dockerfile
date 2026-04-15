# Use a tiny, secure base image
FROM python:3.14-alpine

# Set working directory
WORKDIR /app

# Install dependencies (Security: No cache to keep image small)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Create a non-root user
# Hackers can't easily break out of the container if they aren't 'root'
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Port
EXPOSE 5000

CMD ["python", "app.py"]
