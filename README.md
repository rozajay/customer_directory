
# Customer Directory

This project is a Django application integrated with PostgreSQL using Docker. It is a Graphql back end service exposing a list of people and their associated information.

## Prerequisites

Make sure you have the following installed on your system:

- Docker
- Docker Compose

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository:

   ```shell
   gh repo clone rozajay/customer_directory
   ```

2. Build and start the Docker containers:

   ```shell
   docker compose up --build
   ```

   This command will build the Docker images and start the containers for the Django application and PostgreSQL database.

3. Access the Django application:

   Once the containers are up and running, you can access the GraphiQL interface by opening a web browser and visiting `http://localhost:8000/graphql`.

![screen Recording](/assets/ScreenRecording.gif)

## Project Structure

Here's an overview of the project structure:

```
├── docker-compose.yml
├── dockerfile
├── README.md
├── requirements.txt
├── manage.py
├── assets/
│   └── ScreenRecording.gif
├── customer_directory/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── view_customers/
│   ├── migrations/
│   ├── models.py
│   ├── ...
│   └── ...
└── ...
```

- `docker-compose.yml`: Configuration file for Docker Compose, defining the services and their dependencies.
- `dockerfile`: Instructions to build the Docker image for the Django application.
- `README.md`: This file, providing an overview of the project and instructions on how to run it.
- `requirements.txt`: List of Python dependencies for the Django application.
- `manage.py`: Django project management script.
- `customer_directory/`: Django project directory.
- `view_customers/`: Django app directory.

## Possible Extensions

The project has potential for further extensions and enhancements to make it production-ready and provide additional features. Some possible extensions include:

- **Test Coverage**: Although only one test was written and running it locally was not possible due to time constraints, it is crucial to emphasize the importance of test coverage. 

- **Production-ready deployment**: Implement a production-ready deployment setup, such as using a web server like Nginx, configuring environment variables, and setting up a secure HTTPS connection with SSL/TLS certificates.
  
- **Pagination and total page count**: Extend the API endpoint to provide the total number of pages available. This enhancement would allow the Front-end Engineering team to implement a more user-friendly browsing experience, showing the total number of pages and enabling users to navigate through the data more efficiently.

- **Caching and performance optimization**: Utilize caching mechanisms to improve the performance of the API.

- **Error handling and logging**: Implement robust error handling and logging mechanisms to capture and handle exceptions effectively.
