FROM jupyter/pyspark-notebook:latest

USER root
RUN pip install psycopg2-binary
USER jovyan

RUN pip install minio sqlalchemy pandas psycopg2-binary
