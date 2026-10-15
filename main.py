# Member checker
from pyscript import display, document


def view_user(e):
    document.getElementById('result').innerHTML = ''

    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()
    member_input = f'{first_name} {last_name}'.title()

    spiderman_club = [
        'Peter Parker', 'Miles Morales', 'Gwen Stacy', 'Mary Jane Watson',
        'Ned Leeds', 'Harry Osborn', 'May Parker', 'Miguel Ohara'
    ]

    member_checker = member_input in spiderman_club

    display_message = (
        f'Sorry {member_input}, your name is not on the list.',
        f'Congratulations {member_input}! You are now part of the Spiderman-Club.'
    )
    display(display_message[member_checker], target='result')