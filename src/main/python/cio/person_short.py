from datetime import date, timedelta, datetime
import re

today = date(2018, 1, 1)
articles = {'male': 'he ', 'female': 'she ', 'unknown': ''}

DATE_FORMAT = "%d.%m.%Y"
CURRENT_DATE = datetime.strptime("01.01.2018", DATE_FORMAT)



class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        bd = date(*map(int, reversed(birth_date.split('.'))))

        self._name = f'{first_name} {last_name}'
        self._age = (today - bd) // timedelta(days=365.2425)
        self._work = f'{articles[gender]}is a {job}'.capitalize()
        self._money = re.sub(r"\B(?=(?:\d{3})+$)", " ", str(salary * working_years * 12))
        self._home = f'Lives in {city}, {country}'

    __getattr__ = lambda s, n: lambda: getattr(s, '_' + n)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")