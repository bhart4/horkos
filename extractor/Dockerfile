FROM python:3.6

ADD extractor/horkos-extractor /horkos-extractor
ADD extractor/requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /horkos-extractor

CMD ["python", "app.py"]
