Particle41

SimpleTimeService Application developed with python
This SimpleTimeService.py file has the code for sample application
A Dockerfile is a script that contains a set of instructions to build a Docker image. It automates the process of creating a containerized environment.

#command to build image
docker build -t simpleservice:latest .

#command to run the image
docker run -p 5000:5000 simpleservice:latest

#To upload the image to dockerhub
#Create a repo in dockerhub(ajithakalai/particle41)

#Tag the local image as same format of dockerhub repo
docker tag simpleservice ajithakalai/particle41:latest

#push the tagged image to dockerhub repo
docker push ajithakalai99/particle41:latest

#To use the image you have to pull the image from the dockerhub
docker pull ajithakalai99/particle41:latest

#Use docker run and the application will be launched
docker run -p 5000:5000 ajithakalai99/particle41:latest

#Hit the url received from output
Eg: http://127.0.0.1:5000
