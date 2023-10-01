FROM tiangolo/uwsgi-nginx-flask:python3.11

# Установка зависимостей и конфигурация virtualenv в Poetry
RUN pip install --upgrade pip "poetry==1.5.1"
RUN poetry config virtualenvs.create false --local

# Копирование файла зависимостей в контейнер
COPY pyproject.toml poetry.lock ./

# Установка зависимостей
RUN poetry install --no-ansi --no-dev

# Копирование исходного кода приложения в контейнер
COPY . /app

# Удаление файла конфигурации Nginx, поскольку будем использовать свой собственный
#RUN rm /etc/nginx/conf.d/nginx.conf

# Копирование настроек Nginx в контейнер
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Устанавливаем переменные окружения
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Открываем порт 80
EXPOSE 80

# Запуск Nginx и uWSGI сервера
CMD ["/bin/bash", "-c", "/app/start.sh"]