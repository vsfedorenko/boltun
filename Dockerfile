FROM python:alpine

COPY dist/boltun-*.tar.gz /opt/boltun/dist/boltun.tar.gz

RUN pip install /opt/boltun/dist/boltun.tar.gz

ENTRYPOINT ["python", "-m", "boltun"]