FROM python:3
LABEL AUTHOR=tttriplicate@gmail.com

WORKDIR /usr/src/app
COPY ./dijkstra ./

RUN pip install -r requirements.txt

CMD ["python", "./dijkstra.py"]