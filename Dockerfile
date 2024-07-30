FROM python:3.9-slim
RUN pip install requests flask redis pytest
COPY app /app
WORKDIR /app
CMD ["python", "app.py"]
