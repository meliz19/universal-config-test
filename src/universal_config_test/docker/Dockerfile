FROM python:3.12

RUN pip install krausening

ENV KRAUSENING_BASE=/app/krausening/base

WORKDIR /app/config
COPY src/universal_config_test/config/ /app/config/

WORKDIR /app/krausening/base
COPY src/universal_config_test/krausening/base/ /app/krausening/base/

WORKDIR /app
COPY src/universal_config_test/config-test.py /app/config-test.py

ENTRYPOINT ["python3", "config-test.py"]
