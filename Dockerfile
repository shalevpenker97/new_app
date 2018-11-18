FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
        python \
        python-pip

RUN  pip install flask

EXPOSE 80

CMD ["python","/app/app.py"]
