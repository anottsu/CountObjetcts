FROM python:3.10

WORKDIR /app

COPY requirements.txt .
COPY script.py .
COPY imagens ./imagens

RUN apt-get update && apt-get install -y libgl1-mesa-glx libxcb-xinerama0


RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "Python", "script.py" ]