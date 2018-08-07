from datetime import date

class Person:

    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        date_dmy = birth_date.split('.')
        self.birth_date = date(int(date_dmy[2]), int(date_dmy[1]), int(date_dmy[0]))
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def age(self):
        return (date(2018,1,1) - self.birth_date).days // 365

    def work(self):
        if self.gender == 'male':
            return "He is a " + self.job
        if self.gender == 'female':
            return "She is a %s" % self.job
        else:
            return "Is a %s" % self.job

    def money(self):
        return "{:,d}".format(self.salary * 12 * self.working_years).replace(",", " ")

    def home(self):
        return "Lives in %s, %s" % (self.city, self.country)


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

