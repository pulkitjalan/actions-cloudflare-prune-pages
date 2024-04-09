FROM python:alpine

COPY main.py /main.py

RUN pip install cloudflare

ENTRYPOINT ["python", "/main.py"]
