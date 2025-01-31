# HNG12 API

## Description

This is a simple API that returns my registered email address, the current datetime in ISO 8601 format, and the GitHub URL of the project's codebase.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/DanielleBadobre/hng12.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## API Documentation

### Endpoint: `GET /api`

#### Response Format:

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

### Example Usage:

```bash
curl -X GET https://hng12-api-uxzy.onrender.com/api
```

## Backlink

https\://hng.tech/hire/python-developers

