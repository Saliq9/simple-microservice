#base image 
FROM python:3.7-alpine

#working directory
WORKDIR /usr/src/app

#adding the files to the working directory
ADD app.py /usr/src/app/
ADD userdata.py /usr/src/app/
ADD requirements.txt /usr/src/app/

#set the environment variables used by flask command
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

#install the requirements
RUN pip install -r requirements.txt

#expose the port
EXPOSE 5000

#set default command for the container to flask run
CMD ["flask", "run"]
