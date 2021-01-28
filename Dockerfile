FROM python:3.8

WORKDIR /usr/src/app

ADD requirements.txt ./requirements.txt  
ADD app ./app

RUN pip install --upgrade pip; \
    pip install -r requirements.txt

 

ENTRYPOINT ["python3", "-u", "app/main.py"]
