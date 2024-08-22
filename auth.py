import requests
import pandas as pd
from utils import handle_http_error

USSD_URL = 'https://ussdapi-vv2j.onrender.com'


def get_valid_student_id():
    df = pd.read_csv('indexes.csv')
    student_list = df['student_id'].tolist()

    while True:
        try:
            student_id = int(input('Student ID: '))
            if student_id in student_list:
                return student_id
            else:
                print('Student ID not found. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a numeric Student ID.')


def get_valid_password(student_id):
    while True:
        password = input('Password: ')
        data = {'username': student_id, 'password': password}
        try:
            response = requests.post(f'{USSD_URL}/', json=data)
            response.raise_for_status()
            return response.json().get('access_token')
        except requests.HTTPError as e:
            handle_http_error(e)
            print('Password is incorrect. Please try again.')


def authenticate_user():
    student_id = get_valid_student_id()
    return get_valid_password(student_id)
