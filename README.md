Steps followed to make a Azure REST API:
1. Install flask - pip3 install flask

2. Write Code

3. Build docker image

4. Run docker and Map 5000 ports

5. Browse https::127.0.0.1:5000/

6. (alternate) Deploy it on Azure
   a. Push the docker image to docker hub
   b. Give the path of Docker hub in Azure.
   c. Deploy
6. Instead of putting it on Docker hub, you can alteratively put on Azure registry. This allows easy injecting of env variables into the container. Useful to inject database URL. Keeping it in Dockerfile would expose the secret keys used to access database.

7. Connect to DB
   Create an azure cosmos db, put in some dummy values. Get the secret keys and add it to the App service application variables. 
   These variables are injected into the docker container environment. Use these inside the python script to read/write from DB.
   




   



References: 
1. https://pythonspeed.com/articles/docker-connection-refused/
