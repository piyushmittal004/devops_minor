FROM tensorflow/tensorflow:1.14.0-py3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip3 install --upgrade pip
#RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#RUN python3 get-pip.py
#RUN pip3 install rasa
RUN ["apt-get", "install", "-y", "libsm6", "libxext6", "libxrender-dev"]
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

# copy project
COPY . /usr/src/app/

EXPOSE 8000
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

#To Run this container
# docker build -t img .
# docker run -dp 8000:8000 --name containername img
