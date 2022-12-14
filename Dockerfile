FROM python:3.9

ENV PYTHONUNBUFFERED 1

MAINTAINER zmh-program

RUN mkdir /opt/Zh-Website
WORKDIR /opt/Zh-Website
ADD . /opt/Zh-Website

RUN apt-get update \
  && apt-get install ffmpeg libsm6 libxext6  -y

RUN  python3 -m pip install --upgrade pip \
  && pip3 install opencv-python-headless \
  && pip3 install -r requirements.txt -i https://pypi.douban.com/simple/ \
  && python3 manage.py collectstatic --noinput \
  && python3 manage.py migrate

EXPOSE 8000 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
