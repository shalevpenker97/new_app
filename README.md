# new_app
This is a basic flask app

The goal is to check the CICD pipeline

# Instructions for adding a new instance

To add a new instance you will need to build the docker image and run this command

to start a new container 

docker container run --name app -d -p 5000:80 --mount type=bind,source="/home/for_jenkins/app.py",target=/app/app.py app

in addition you will need to add a new hostname to the ansible config
