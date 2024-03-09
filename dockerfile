FROM python:3.12

# установка рабочей директории в контейнере
WORKDIR /code

# копирование файла зависимостей в рабочую директорию
COPY requirements.txt .

# установка зависимостей

# копирование содержимого локальной директории src в рабочую директорию
COPY main.py .
COPY db.py .
COPY parser.py .
COPY build.bash .
COPY run.bash .
COPY /habrParser ./habrParser

EXPOSE 8000

RUN sh build.bash

# команда, выполняемая при запуске контейнера
CMD sh run.bash