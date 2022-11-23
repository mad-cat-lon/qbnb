FROM python:3.10.4
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
ADD wait-for-it.sh /app
RUN chmod +x /app/wait-for-it.sh