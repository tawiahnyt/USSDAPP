import json
import requests
from utils import grader, go_home, handle_http_error

USSD_URL = 'https://ussdapi-vv2j.onrender.com'


def display_results(api_token):
    try:
        response = requests.get(f'{USSD_URL}/results', headers={'Authorization': f'Bearer {api_token}'})
        response.raise_for_status()
        result_details = response.json()

        with open('courses.json') as file:
            data = json.load(file)

        level = result_details.get('level')

        if level == 100:
            print('No results to show')
        else:
            display_level_results(data, result_details, level)
    except requests.HTTPError as e:
        handle_http_error(e)

    go_home(api_token)


def display_level_results(data, result_details, level):
    courses = {
        200: [('100', 'first_semester'), ('100', 'second_semester'), ('200', 'first_semester'),
              ('200', 'second_semester')],
        300: [('100', 'first_semester'), ('100', 'second_semester'), ('200', 'first_semester'),
              ('200', 'second_semester')],
        400: [('100', 'first_semester'), ('100', 'second_semester'), ('200', 'first_semester'),
              ('200', 'second_semester'), ('300', 'first_semester'), ('300', 'second_semester')]
    }

    if level in courses:
        for index, (lvl, sem) in enumerate(courses[level], 1):
            print(f'{index}. Level {lvl} {sem.replace("_", " ").capitalize()} Results')
            for course in data['BSc. Information Technology'][lvl][sem]:
                course_code = course['course_code']
                print(f"{course_code} - {course['course_title']} - {grader(result_details.get(course_code.replace('-', '_')))}")
