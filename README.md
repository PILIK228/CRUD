# CRUD with SQL
- The fouth CRUD version presents possibilities of interactions with data in SQL
- Was created a container with PostgreSQL in Docker
- Added registration and authorisation system
- Added roles (admin/moderator/user) system, where each role has it's own possibilities
## Setup
#### Run a Docker container
To restore a database dump into your local Docker container, first ensure your container is currently running.  
- You can use `docker container ls` to check if it's on already 
- If it's not, simply start it by running `docker start postgres`
####  Restoring the data into your Docker container
Assuming you have the Docker container running and a data dump file ready, you can run the following command to import all dat.     
Be sure to substitute `./latest.dump` to where your dump file is located, if it's not in the current working directory and called latest.dump.  
`docker exec -i postgres pg_restore --verbose --clean --no-acl --no-owner -h localhost -U postgres -d <your-db-name> < ./latest.dump
` 
#### Install requirements in Python
For correct work you also need to install module 'psycopg2-binary':  
`pip install psycopg2-binary`
and check your ve requirements with:    
`pip freeze`