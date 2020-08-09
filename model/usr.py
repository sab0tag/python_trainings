from sys import maxsize


class User:

    def __init__(self, name=None, surname=None, nick=None, titl=None, company_name=None, street=None,
                 mobile_number=None, homephone=None, workphone=None, secondaryphone=None,
                 email_1=None, email_2=None, b_day=None, b_month=None, b_year=None, street2=None, id=None):
        self.name = name
        self.surname = surname
        self.nick = nick
        self.titl = titl
        self.company_name = company_name
        self.street = street
        self.mobile_number = mobile_number
        self.homephone = homephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email_1 = email_1
        self.email_2 = email_2
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.street2 = street2
        self.id = id

    # строковое представление объекта памяти
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.surname)

    # функция для сравнения объектов по логическому критерию
    # добавлено правило сравнения записей, в случае если идентификатор записи в результате не определен
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.surname == other.surname

    # вычисление ключа по контакту для сравнения
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
