# Reminder Me Later API

The Reminder Me Later API is a simple Django API endpoint that allows users to create reminders with a message. It provides a convenient way to store reminder data in the database for future reference.

## API Endpoints

### Get CSRF Token

- **URL:** `/get_csrf_token/`
- **Method:** GET
- **Description:** This endpoint returns the CSRF token required for making POST requests to other endpoints.

#### Example Request
GET /get_csrf_token/


#### Example Response
{
  "X-CSRFToken": "ABCD1234EFGH5678IJKL90MNOP"
}

## Create Reminder

- **URL:** `/api/create_reminder/`
- **Method:** POST

#### Example Request
{
  "date": "2024-03-20",
  "time": "10:00:00",
  "message": "Don't forget the meeting!",
  "reminder_type": "Email"
}

#### Example Response (Success)
{
  "message": "Reminder saved successfully!"
}

#### Example Response (Error)
{
  "error": "Invalid request data"
}

## Setup

- Clone the repository to your local machine.
- Install Python and Django if not already installed.
- Create a virtual environment and activate it.
- Install the required dependencies using pip install -r requirements.txt.
- Run the Django development server using python manage.py runserver.

## Usage

- Send a GET request to the /api/get_csrf_token/ endpoint to obtain the CSRF token.
- Use the obtained CSRF token in the request headers for POST requests to other endpoints like /api/create_reminder/.
- Send a POST request to the /api/create_reminder/ endpoint with the required data as JSON in the request body.
- Receive a response indicating the success or failure of the reminder creation.
  


