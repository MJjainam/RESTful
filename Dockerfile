FROM ubuntu:20.04
RUN apt update && \
    apt install python3 \
    python3-pip -y \
    nano \
    curl

RUN pip3 install flask
RUN pip3 install pymongo


RUN mkdir -p /opt/RESTful
COPY main.py /opt/RESTful
RUN chmod +x /opt/RESTful/main.py
EXPOSE 5000
# RUN cd /opt/RESTful && python3 main.py
CMD ["/opt/RESTful/main.py"]