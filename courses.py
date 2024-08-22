import requests
from utils import go_home, handle_http_error

USSD_URL = 'https://ussdapi-vv2j.onrender.com'


def register_courses(api_token):
    try:
        account_response = requests.get(f'{USSD_URL}/account', headers={'Authorization': f'Bearer {api_token}'})
        account_response.raise_for_status()
        registration_status = account_response.json().get('registration_status')

        courses_response = requests.get(f'{USSD_URL}/courses', headers={'Authorization': f'Bearer {api_token}'})
        courses_response.raise_for_status()
        courses_details = courses_response.json()

        display_courses(courses_details)

        choice = int(input('Press 1 to register all courses: '))

        if choice == 1 and registration_status == 0:
            registration_response = requests.patch(f'{USSD_URL}/complete_registration', headers={'Authorization': f'Bearer {api_token}'})
            registration_response.raise_for_status()
            print("Course Registration successful.")
        else:
            print('You have been registered already')

    except requests.HTTPError as e:
        handle_http_error(e)

    go_home(api_token)


def display_courses(courses_details):
    for index, course in enumerate(courses_details, 1):
        print(f"{index}. {course['course_code']} - {course['course_title']}")
