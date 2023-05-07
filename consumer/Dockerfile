FROM python:3.9

CMD mkdir /home/app
WORKDIR /home/app

COPY requirements.txt /home/app/requirements.txt
COPY fraud_detection_consumer.py /home/app/fraud_detection_consumer.py 
COPY requirements.txt /home/app/requirements.txt
RUN pip3 install -r requirements.txt
CMD ["faust","-A","fraud_detection_consumer","worker","l","info"]

