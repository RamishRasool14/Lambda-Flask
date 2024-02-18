# AWS Lambda API Documentation

## Introduction

This is a guide for a FAST API designed to identify pairs of numbers within an array of integers whose sum matches a given input number. It invokes a AWS Lambda Function exposed via an API Gateway. This document will guide you through the process of setting up the project, interacting with the API, and understanding the available endpoints.

## Getting Started

Follow these steps to get started with the project:

1. **Clone the Project:**
   ```bash
   git clone https://github.com/RamishRasool14/Lambda-Flask
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd Lambda-Flask
   ```

3. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - For Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

5. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Project:**
   ```bash
   python app.py
   ```

Now, the project should be up and running on `http://127.0.0.1:5000`.

## Interacting with the API

You can use Postman or CURL to interact with the API. The following section provides details about the available endpoints, request format, and response format.

### Endpoint

- **URL:** `http://127.0.0.1:5000`
- **Method:** POST

### Request Format

- **Payload:**
  ```json
  {
    "arr": [2, 7, 4, 5, 11, 15],
    "sum": 7
  }
  ```

- **Headers:**
  - `Content-Type`: application/json

- **Example Request:**
  ```python
  import requests
  import json

  url = "http://127.0.0.1:5000"

  payload = json.dumps({
    "arr": [2, 7, 4, 5, 11, 15],
    "sum": 7
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
  ```

- **Curl Command:**
  ```bash
  curl -X POST "http://127.0.0.1:5000" -H "Content-Type: application/json" -d '{"arr": [2, 7, 4, 5, 11, 15], "sum": 7}'
  ```

### Response Format

- **Success Response:**
  - HTTP Status Code: 200 OK
  - Example:
    ```json
    {
      "result": true,
      "pairs": [[2, 5], [4, 3]]
    }
    ```

- **Error Response:**
  - HTTP Status Code: 400 Bad Request
  - Example:
    ```json
    {
      "error": "Invalid input. Please provide a valid array and sum."
    }
    ```

## Conclusion

You have successfully set up the project, and now you can interact with the API using the provided endpoints. If you encounter any issues or have questions, feel free to refer to this documentation or reach out for support.