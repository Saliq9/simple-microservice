Simple Microservice
----------------------
A simple REST microservice example.
It implements basic REST routes for a given user resource:

        GET / : Welcome Message, 
        GET /users : Retrieve all users and
        GET /users/<user_id> : Retrieve a single user
              
Dockerize
--------
Clone the repository : 

        git clone https://github.com/kriti242/simple-microservice

Build the image :

        docker image build -t $IMAGE-NAME .
        
Run the container (port 5000): 

        docker container run -it --name $NAME -d -p 5000:5000 $IMAGE-NAME

Visit the link in browser : 

        http://localhost:5000/
        http://localhost:5000/users
        http://localhost:5000/users/<user_id>
