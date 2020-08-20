FROM python:3.7.9-stretch
COPY . .
RUN pip install -r week2/requirements.txt
CMD python3 ./week2/spoiler.py
