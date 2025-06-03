FROM apache/superset:latest

USER root

# Installer les outils système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    libkrb5-dev \
    libsasl2-dev \
    python3-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Installer les drivers supplémentaires
RUN pip install \
    pyhive[hive] \
    thrift \
    sasl \
    trino \
    sqlalchemy-trino \
    psycopg2-binary

USER superset
