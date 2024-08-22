import requests
from auth import authenticate_user
from account import display_account
from results import display_results
from courses import register_courses

USSD_SHORTCODE = '*123*112#'
USSD_URL = 'https://ussdapi-vv2j.onrender.com'


def home(api_token):
    response = requests.get(f'{USSD_URL}/home', headers={'Authorization': f'Bearer {api_token}'})
    response.raise_for_status()
    user_name = response.json().get('first_name')
    print(f"Welcome {user_name}! What would you like to do today?")

    user_response = int(input('1. My Account\n2. Check Results\n3. Register Courses\n4. Academic Calnedar\n'
                              '5. Log Out\nEnter an option to proceed: '))

    if user_response == 1:
        display_account(api_token)
    elif user_response == 2:
        display_results(api_token)
    elif user_response == 3:
        register_courses(api_token)
    else:
        print("Logging out... Goodbye!")
        exit()


def main():
    short_code = '*123*112#'
    if short_code == USSD_SHORTCODE:
        print("Welcome to GCTU SIP USSD.\nLogin with your credentials to proceed")
        api_token = authenticate_user()

        if api_token:
            home(api_token)
        else:
            print("Authentication failed. Exiting...")


if __name__ == "__main__":
    main()
