# GCTU SIP USSD Application

## Overview

The GCTU SIP USSD Application is a Python-based command-line tool that allows students to interact with their academic records and perform actions such as checking account details, viewing results, and registering courses through a USSD interface. The application communicates with a backend API to fetch and update student information.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `requests` library
- `pandas` library

### Installation

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install requests pandas
   ```

### Running the Application

1. **Start the Application**

   Run the `main.py` script:

   ```bash
   python main.py
   ```

2. **Follow the Prompts**

   - **Login:** Enter your Student ID and Password.
   - **Navigate:** Choose from the following options:
     - View Account Details
     - Check Results
     - Register for Courses
     - View Academic Calendar
     - Log Out

     
**Login Credentials:**

- Student ID and Password:
    - 2124080958 
    - 2225080869 
    - 2326080869

## File Structure

- `main.py`: Entry point of the application. Handles user input and directs to appropriate functionality.
- `auth.py`: Manages user authentication and validation.
- `account.py`: Displays student account details.
- `results.py`: Displays academic results based on the student's level.
- `courses.py`: Handles course registration and displays available courses.
- `utils.py`: Contains utility functions for error handling and grading.

