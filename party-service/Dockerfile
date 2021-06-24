FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 5050
CMD ["python3", "-m", "flask", "run", "-p", "5050", "--host=0.0.0.0"]
