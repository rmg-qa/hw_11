import dataclasses
from datetime import date


@dataclasses.dataclass
class User:
    name: str
    last_name: str
    email: str
    mobile_number: str
    current_address: str
    date_of_birth: date
    math: str

user_student = User(name='Роман', last_name='Гороховик', email='roman_qa@gmail.com', mobile_number='9963334558',
                    current_address='Кемерово, ул. Советсткая, д.6', date_of_birth=date(1996,10,1),
                    math='math')

