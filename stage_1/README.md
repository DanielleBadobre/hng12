     ```markdown
     # Number Classification API

     ## Description
     This API classifies a number based on its mathematical properties and returns a fun fact.

     ## Endpoint
     `GET /api/classify-number?number=<number>`

     ## Example Request
     ```
     GET /api/classify-number?number=371
     ```

     ## Example Response
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

     ## Deployment
     This API is deployed on Render: [https://your-render-app.onrender.com](https://your-render-app.onrender.com)

     ## Setup
     To run locally:
     1. Clone the repository:
        ```bash
        git clone https://github.com/yourusername/your-repo.git
        ```
     2. Install dependencies:
        ```bash
        pip install -r requirements.txt
        ```
     3. Run the app:
        ```bash
        python app.py
        ```
     ```
