FROM python:3.11.3-slim-buster

WORKDIR /app

RUN apt -y install wget
RUN wget https://download.oracle.com/otn_software/linux/instantclient/1918000/oracle-instantclient19.18-basic-19.18.0.0.0-2.x86_64.rpm
RUN apt -y install oracle-instantclient19.18-basic-19.18.0.0.0-2.x86_64.rpm

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY oracleconn.py . 

ENTRYPOINT [ "python", "oracleconn.py" ]