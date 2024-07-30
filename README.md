# poke-random

This project is a simple Flask-based API that returns the name and abilities of a random Pokémon. The project runs in a Docker container and uses Redis for caching API calls. The project also includes necessary tests that are run using the `pytest` framework.

## Requirements

- Docker
- Docker Compose
- Task

## Project Structure

```
poke-random/
│
├── app/
│ ├── init.py
│ ├── app.py
│
├── tests/
│ ├── init.py
│ ├── test_app.py
│
├── Dockerfile
├── docker-compose.yml
├── Taskfile.yml
├── README.md
```

## Installation and Running

Follow the steps below to set up and run the project:

1. **Build the Docker images:**

`task build`

2. **Start the application:**

`task up`

3. **Run the tests:**

`task test`

5. **Stop the application:**

`task down`

5. **Clean up the environment**

`task cleanup`

### Check the running containers

Make sure your Docker containers are running.

`docker-compose ps`

Communication with HTTP requests.

**Browser:** Open a browser and visit the following URL

`http://localhost:5000/pokemon`

This will return the name and abilities of a random Pokémon.

**cURL command:** You can use cURL in the terminal

`curl http://localhost:5000/pokemon`

This will return a JSON response about the Pokémon's name and abilities.

**Postman:** If you have Postman installed, you can send a GET request to the following URL.

`http://localhost:5000/pokemon`

The response contains the data of the randomly selected Pokémon in JSON format.

### Troubleshooting

**Container status:** if something is not working, check the status of the containers.

`docker-compose logs`

This will show you the logs of the containers, which can help you in troubleshooting.

**Redis connectivity problems:** if Redis is not working properly, check if the cache container is running:

`docker-compose ps`

**Flask application errors:** if the Flask application does not respond, check the logs of the api container:

`docker-compose logs poke-random-api`

With these steps and tools, you can effectively communicate with the running Flask application and troubleshoot if something is not working properly.

## API Endpoint

Once the application is started, the API can be accessed at http://localhost:5000/pokemon. This endpoint returns the name and abilities of a random Pokémon.

Example response:

```
{
  "name": "ditto",
  "abilities": [
    "limber",
    "imposter"
  ]
}
```

## Detailed Description

### Dockerfile

The Dockerfile installs the necessary Python packages, copies the project code into the container, sets the working directory, and starts the application.

### docker-compose.yml

The docker-compose.yml file defines the API and Redis services. The API service is available on port 5000, while Redis is available on port 6379.

### Taskfile.yml

The Taskfile.yml file defines the tasks for building, starting, stopping, and testing the project using Docker Compose.
The cleanup task removes the images and prunes the docker sytem.

### Flask Application

The app.py file contains the Flask application code, which handles the API requests and Redis caching.

### Testing

The test_app.py file contains the API tests, which are run using the pytest framework.

## Maintenance and Development

For further maintenance and development of the project, it is recommended to write additional tests, integrate CI/CD, and set up monitoring and logging. Breaking down the application into different services and managing them with Docker Compose or Kubernetes can also be beneficial.

## Contribution

If you have any questions or would like to contribute to the project, feel free to open an issue or create a pull request.

Thank you for using my project!