FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=src/app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]