FROM python:3-alpine

COPY --link main.py /main.py
COPY --link requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENTRYPOINT ["python", "/main.py"]
