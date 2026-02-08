# 1. Start with a lightweight Python OS
FROM python:3.9-slim

# 2. Create a folder inside the image
WORKDIR /app

# 3. Copy only the requirements first (for caching)
COPY requirements.txt .

# 4. Install dependencies inside the image
RUN pip install -r requirements.txt

# 5. Copy the rest of the app code
COPY . .

# 6. Run the app when container starts
CMD ["python", "app.py"]