FROM python:alpine

ARG BOLTUN_DIR="/opt/boltun"

ARG WHL_DIR=${BOLTUN_DIR}/dist
COPY dist/*.whl ${WHL_DIR}/
RUN pip install ${WHL_DIR}/*.whl

ENTRYPOINT ["python", "-m", "boltun"]