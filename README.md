# jobtrack
In this reposetory we create an application build to connect people with the job best suited for there life. Working in diffrent offices withg diffrent people building a with span experience and score by diffrent organisation. Creating the future of working.
Opgave Herexamenproject
Voor het herexamenproject werk je wederom individueel een opdracht uit. Het thema mag je zelf kiezen. Je mag niet verder bouwen aan een project dat je in semester 1 gemaakt hebt, je begint dus met een volledig nieuw project!

# JobTrack API

For the final project in API development, the goal was to create a web application for job tracking and management. This application allows users to handle job listings efficiently, including operations such as creating, updating, and deleting job posts. 

Below is a summary of the project status, detailing what has been accomplished and what remains to be completed.

## 1. General Requirements & Documentation

### API Endpoints
- **GET Endpoints**:
  - **`/jobs`**: Retrieves a list of all job listings.
    ![GET Jobs](readme/get_jobs.png)
  - **`/jobs/{id}`**: Retrieves details of a specific job listing by ID.
    ![GET Job](readme/get_job.png)
  - **`/users`**: Retrieves a list of all users.
    ![GET Users](readme/get_users.png)
  - **`/users/{id}`**: Retrieves details of a specific user by ID.
    ![GET User](readme/get_user.png)
  - **`/profile`**: Retrieves the profile information of the currently authenticated user.
    ![GET Profile](readme/get_profile.png)

- **POST Endpoints**:
  - **`/jobs`**: Creates a new job listing.
    ![POST Job](readme/post_job.png)
  - **`/users`**: Creates a new user.
    ![POST User](readme/post_user.png)
  - **`/auth/login`**: Authenticates a user and returns a token.
    ![POST Auth](readme/post_auth.png)

- **PUT Endpoints**:
  - **`/jobs/{id}`**: Updates details of an existing job listing.
    ![PUT Job](readme/put_job.png)
  - **`/users/{id}`**: Updates details of an existing user.
    ![PUT User](readme/put_user.png)
  - **`/profile`**: Updates the profile information of the currently authenticated user.
    ![PUT Profile](readme/put_profile.png)

- **DELETE Endpoints**:
  - **`/jobs/{id}`**: Deletes a job listing by ID.
    ![DELETE Job](readme/delete_job.png)

    
### Entities and Database

- **SQLite Database**:
  - The API uses SQLite with entities such as jobs, users, and applications.

  ![Database Overview](readme/database_overview.png)

### Authentication and Security

- **Hashing and OAuth**:
  - Implemented in `auth.py`.

### Documentation and Hosting

- **Theme and API Description**:
  - The application enables users to manage job listings with full CRUD operations.
  - Hosted application can be accessed at [Live Deployment](https://python-service-tristan-project.cloud.okteto.net/static/index.html).

- **OpenAPI Documentation**:
  - Full documentation available [here](https://python-service-tristan-project.cloud.okteto.net/openapi.json).

- **GitHub Repository**:
  - [GitHub Repository](https://github.com/tristan-project/jobtrack)

### Docker and Deployment

- **Docker Container**:
  - Dockerfile created for the API.
  - Automated build via GitHub Actions.

  ![GitHub Actions](readme/github_actions.png)

- **Docker Compose Deployment**:
  - API container deployed using Docker Compose.

## 2. Additions: Functionality

### Testing

- **GET Endpoints**:
  - Tests using `requests` and `pytest` are pending implementation.

- **Non-GET Endpoints**:
  - Tests for POST, PUT, and DELETE endpoints have been completed.

- **GitHub Actions Testing**:
  - Test file runs during GitHub Actions.

## 3. Additions: Front-End

- **Front-End Development**:
  - Front-end interface supporting all GET and POST endpoints is complete.

- **Hosting**:
  - Front-end is not yet hosted on Netlify.

- **Styling**:
  - Styling has been completed.

- **JavaScript Framework**:
  - Currently using Alpine.js; considering integration of Vue, React, Angular, or Svelte.

## 4. Additions: Data

### MongoDB

- **MongoDB Atlas**:
  - A new version of the API using MongoDB Atlas is planned but not yet implemented.

- **MongoDB Container**:
  - Future plans include replacing MongoDB Atlas with a MongoDB container in the deployment.

### Messaging

- **ActiveMQ**:
  - Integration of ActiveMQ for message queuing is planned but not yet completed.

## 5. Additions: Monitoring

### Prometheus and Grafana

- **Prometheus and Grafana Setup**:
  - Plans to add Prometheus for metrics collection and Grafana for visualization are in progress but not yet completed.