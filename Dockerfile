FROM python:3.8

ENV TARGET_PATH=/usr/src/pythonSem4Lab1

RUN mkdir -p "${TARGET_PATH}"

WORKDIR "${TARGET_PATH}"

COPY hello.py requirements.txt "${TARGET_PATH}"

RUN set -ex \ pip3 install —no-cache-dir -r requirements.txt \
&& rm requirements.txt

CMD ["python3", "hello.py"]
