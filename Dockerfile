FROM python:3.8-slim

COPY main.py main.py
ENTRYPOINT ["/main.py"]
