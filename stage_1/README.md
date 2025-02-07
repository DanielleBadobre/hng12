```markdown
# Number Classification API

## Description
This is a backend API that classifies a number based on its mathematical properties (e.g., prime, perfect, Armstrong, odd/even) and returns a fun fact about the number using the [Numbers API](http://numbersapi.com).

## Features
- Classifies a number based on its properties.
- Returns a fun fact about the number.
- Handles invalid inputs gracefully.
- Deployed to a publicly accessible endpoint.

## API Endpoint
### Request
```
GET /api/classify-number?number=<number>
```

### Parameters
- `number` (required): The number to classify. Must be a valid integer.

### Example Request
```
GET /api/classify-number?number=371
```

### Response (200 OK)
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Response (400 Bad Request)
```json
{
  "number": "alphabet",
  "error": true
}
```

## Deployment
The API is deployed on **Render** and can be accessed at:
```
https://number-classification-api.onrender.com/api/classify-number?number=<number>
```

## Setup Instructions
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/number-classification-api.git
   cd number-classification-api
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**:
   ```bash
   python app.py
   ```

4. **Test the API**:
   Open your browser or use a tool like Postman to test the API:
   ```
   http://127.0.0.1:5000/api/classify-number?number=371
   ```

## Dependencies
- Flask: A lightweight WSGI web application framework.
- Flask-CORS: Handles Cross-Origin Resource Sharing (CORS).
- Requests: Makes HTTP requests to the Numbers API.

## Code Structure
```
stage_1/
├── app.py                # Main Flask application
├── requirements.txt      # List of dependencies
├── Procfile              # Specifies the command to run the app
├── README.md             # Project documentation
└── .gitignore            # Specifies files to ignore in Git
```

## Technologies Used
- **Programming Language**: Python
- **Framework**: Flask
- **Deployment Platform**: Render
- **Version Control**: GitHub

## Contributing
Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Example Usage
### Valid Input
```
GET /api/classify-number?number=28
```

**Response**:
```json
{
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": ["even"],
  "digit_sum": 10,
  "fun_fact": "28 is a perfect number."
}
```

### Invalid Input
```
GET /api/classify-number?number=alphabet
```

**Response**:
```json
{
  "number": "alphabet",
  "error": true
}
```

---

## Additional Notes
- The API uses the **math** type from the Numbers API to fetch fun facts.
- The `properties` field in the response can have the following combinations:
  - `["armstrong", "odd"]`: If the number is both an Armstrong number and odd.
  - `["armstrong", "even"]`: If the number is an Armstrong number and even.
  - `["odd"]`: If the number is not an Armstrong number but is odd.
  - `["even"]`: If the number is not an Armstrong number but is even.

---

Enjoy using the Number Classification API! 🚀
```
