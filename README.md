
# Multi-container-docker-setup
This is a multi-container simple hello world program by integrating flask, nginx and postgresql in a docker environment

# Components
- helloapp : python flask app which return a json format "Hello World" which rertrive from the postgresql database
- postgres : postgresql database which hold the messages table 
- nginx: exposing the hello app output to the public using reverse proxy

# To Start the application 
$sudo docker compose up -d

# To test the application
curl --request GET 'http://[nginx server IP]/hello'

# signed by nwn722
