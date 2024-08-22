import requests
from utils import go_home, handle_http_error

USSD_URL = 'https://ussdapi-vv2j.onrender.com'


def display_account(api_token):
    try:
        response = requests.get(f'{USSD_URL}/account', headers={'Authorization': f'Bearer {api_token}'})
        response.raise_for_status()
        account_details = response.json()

        name = f"{account_details.get('first_name', '')} {account_details.get('last_name', '')}"
        if account_details.get('other_name'):
            name += f" {account_details.get('other_name')}"
        status = 'Registered' if account_details.get('registration_status') else 'Unregistered'
        print(
            f"Name: {name}\n"
            f"Student ID: {account_details.get('student_id')}\n"
            f"Programme: {account_details.get('degree_programmes')}\n"
            f"Level: {account_details.get('level')}\n"
            f"Email: {account_details.get('email')}\n"
            f"Phone: {account_details.get('phone')}\n"
            f"Student's Email: {account_details.get('student_email')}\n"
            f"Date of Birth: {account_details.get('date_of_birth')}\n"
            f"Gender: {account_details.get('gender')}\n"
            f"Enrollment Date: {account_details.get('enrollment_date')}\n"
            f"Graduation Date: {account_details.get('graduation_date')}\n"
            f"Student Type: {account_details.get('student_type')}\n"
            f"Registration Status: {status}\n"
        )

    except requests.HTTPError as e:
        handle_http_error(e)

    go_home(api_token)
