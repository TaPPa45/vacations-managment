FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_vacations
WORKDIR /web_vacations
COPY requirements.txt /web_vacations/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /web_vacations/ 