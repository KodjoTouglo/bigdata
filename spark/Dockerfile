FROM amhhaggag/spark-3.5.1:1.1

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip && \
    apt-get clean \

RUN pip install pyspark

COPY process.py /opt/spark-apps/
