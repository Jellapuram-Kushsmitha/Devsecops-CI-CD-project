# Step 1: Base Image
FROM python:3.9-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy files
COPY . /app

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port
EXPOSE 5000

# Step 6: Run app
CMD ["python", "app.py"]