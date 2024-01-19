FROM ubuntu:22.04
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
RUN pip3 install -r setup.txt
EXPOSE 12345
CMD [ "python3", "test_FashionMnist.py" ]
