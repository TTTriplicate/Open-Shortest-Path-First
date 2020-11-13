FROM python:3
LABEL AUTHOR=tttriplicate@gmail.com

WORKDIR /usr/src/app
COPY ./djikstra ./

RUN pip install -r requirements.txt

CMD ["python", "./djikstra.py"]