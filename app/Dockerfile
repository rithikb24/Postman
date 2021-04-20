FROM python:latest
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY products.csv products.csv
COPY app.py app.py
CMD ["python", "-u", "app.py"]
