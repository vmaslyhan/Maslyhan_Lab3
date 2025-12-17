FROM python:3.12-slim

WORKDIR /maslyhan

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /maslyhan

CMD ["python", "gtrans3.py"]