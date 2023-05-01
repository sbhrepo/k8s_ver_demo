FROM python:3.8.16-alpine as base

# COPY ./requirements.txt .

# RUN apt update && \
    # pip install --upgrade pip && \
    # pip install -r requirements.txt

# RUN rm requirements.txt

FROM base
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

CMD [ "python3", "main.py" ]
