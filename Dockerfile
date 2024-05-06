FROM python:3.11-slim-bookworm
EXPOSE 8501

# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file
ENV PYTHONUNBUFFERED TRUE
ENV PYTHONFAULTHANDLER TRUE

RUN echo "Europe/London" > /etc/timezone

RUN pip install --upgrade pip
RUN pip install poetry
RUN apt update
RUN apt install gcc git -y

RUN mkdir -p /home/app
ENV HOME=/home/app
RUN mkdir -p /home/app/static
WORKDIR $HOME/

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry config virtualenvs.create false

COPY src .
RUN poetry install --no-dev --no-interaction

CMD streamlit run streamlit_app.py
