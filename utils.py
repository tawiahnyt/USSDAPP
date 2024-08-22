def go_home(api_token):
    choice = int(input('\nPress 0 to go to the main menu: '))
    if choice == 0:
        from main import home
        home(api_token)


def handle_http_error(error):
    print(f"HTTP error occurred: {error}")


def grader(score):
    if score is None:
        return 'N/A'
    elif score >= 80:
        return 'A'
    elif score >= 75:
        return 'A-'
    elif score >= 70:
        return 'B+'
    elif score >= 65:
        return 'B'
    elif score >= 60:
        return 'B-'
    elif score >= 55:
        return 'C+'
    elif score >= 50:
        return 'C'
    elif score >= 45:
        return 'C-'
    elif score >= 40:
        return 'D'
    else:
        return 'F'
