FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.4.2

RUN apt-get update && apt-get install -y gcc python-dev

COPY poetry.lock pyproject.toml README.md /app/

WORKDIR app

COPY . /app

RUN pip install -U pip
RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
RUN poetry install



# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run streamlit when the container launches
CMD ["streamlit", "run", "ui/main.py"]
