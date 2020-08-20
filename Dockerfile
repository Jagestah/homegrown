FROM python:3.7.9-stretch
COPY ./week2/requirements.txt ./week2/requirements.txt
RUN pip install -r week2/requirements.txt
COPY . .
CMD python3 ./week2/spoiler.py
