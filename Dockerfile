ARG PYTHON_VERSION=3.12-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /main

WORKDIR /main

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY. /main

# Expose the port the app runs on
EXPOSE 5000

# Specify the command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
