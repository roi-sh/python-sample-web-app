# Flask Task Manager

A simple, containerized task management web application built with Flask. This application allows users to add, complete, and delete tasks with a clean, responsive interface.

## Features

- **Task Management**: Add, complete, and delete tasks
- **Real-time Feedback**: Flash messages for user actions
- **Task Statistics**: View completion statistics
- **REST API**: JSON endpoint for task data
- **Responsive Design**: Clean, modern interface
- **Dockerized**: Ready for containerized deployment

## Project Structure

```
flask-task-manager/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── README.md             # Project documentation
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    ├── index.html        # Main task management page
    └── about.html        # About page
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Jinja2 templating
- **Containerization**: Docker
- **Data Storage**: In-memory (Python list)

## Docker Deployment

### Prerequisites

- Docker installed on your system
- Git (to clone the repository)

### Build the Docker Image

```bash
# Clone or navigate to the project directory
cd flask-task-manager

# Build the Docker image
docker build -t flask-task-manager .
```

### Run the Container

#### Basic Deployment (Development)
```bash
docker run -p 5000:5000 flask-task-manager
```

#### Production Deployment (with custom secret key)
```bash
docker run -p 5000:5000 -e SECRET_KEY="your-super-secure-production-key" flask-task-manager
```

#### Advanced Deployment Options

**Run in background:**
```bash
docker run -d -p 5000:5000 -e SECRET_KEY="your-secret-key" --name task-manager flask-task-manager
```

**Run with custom port:**
```bash
docker run -p 8080:5000 -e SECRET_KEY="your-secret-key" flask-task-manager
```

**Run with auto-generated secure key:**
```bash
docker run -p 5000:5000 -e SECRET_KEY="$(openssl rand -base64 32)" flask-task-manager
```

## Access the Application

Once the container is running, access the application at:

- **Web Interface**: http://localhost:5000
- **API Endpoint**: http://localhost:5000/api/tasks
- **About Page**: http://localhost:5000/about

## Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `SECRET_KEY` | Flask secret key for session security | Auto-generated | No |
| `PORT` | Application port | 5000 | No |
| `FLASK_ENV` | Flask environment | production | No |

## API Usage

### Get All Tasks
```bash
curl http://localhost:5000/api/tasks
```

**Response:**
```json
{
  "tasks": [
    {
      "id": 1,
      "text": "Sample task",
      "completed": false
    }
  ]
}
```

## Security Notes

### Secret Key
- **Development**: If no `SECRET_KEY` is provided, the app generates a random one
- **Production**: Always provide a secure `SECRET_KEY` environment variable
- **Generation**: Use `openssl rand -base64 32` to generate a secure key

### Production Considerations
- This app uses in-memory storage - data is lost when container restarts
- For production, consider integrating with a persistent database
- Implement proper authentication and authorization
- Use HTTPS in production
- Set up proper logging and monitoring

## Health Check

The Docker container includes a built-in health check that monitors the application status:

```bash
# Check container health
docker inspect --format='{{.State.Health.Status}}' task-manager
```

## Development

### File Structure Details

**app.py**: Main Flask application with routes and logic
- Home route (`/`) - displays task list
- Add task route (`/add_task`) - handles form submissions
- Complete/delete task routes - task management
- API route (`/api/tasks`) - JSON endpoint

**templates/**: Jinja2 HTML templates
- `base.html` - shared layout and styling
- `index.html` - main task interface
- `about.html` - application information

### Key Features Implementation

**Flash Messages**: User feedback system using Flask's session-based messaging

**Task Management**: CRUD operations with in-memory storage

**Responsive Design**: CSS grid and flexbox for mobile-friendly interface

**Security**: Environment-based configuration for sensitive data

## Troubleshooting

### Common Issues

**Port already in use:**
```bash
# Use different port
docker run -p 8080:5000 flask-task-manager
```

**Container won't start:**
```bash
# Check logs
docker logs flask-task-manager
```

**Permission denied:**
```bash
# Ensure Docker is running and you have permissions
sudo docker run -p 5000:5000 flask-task-manager
```

### Health Check Failed
If the health check fails, check:
1. Application is responding on port 5000
2. No errors in container logs
3. Container has sufficient resources

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker
5. Submit a pull request

## License

This project is open source and available under the MIT License.

---

**Quick Start Commands:**
```bash
# Build and run in one go
docker build -t flask-task-manager . && docker run -p 5000:5000 flask-task-manager

# Production deployment
docker run -d -p 5000:5000 -e SECRET_KEY="$(openssl rand -base64 32)" --name task-manager flask-task-manager
```
