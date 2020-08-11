from sys import maxsize


class User:

    def __init__(self, name=None, surname=None, nickname=None,id=None,
                 title=None, company=None, address=None,
                 mobile_number=None, homephone=None, workphone=None, secondaryphone=None, all_phones_from_homepage=None,
                 email_1=None, email_2=None, email_3 = None, all_emails_from_homepage=None,
                 b_day=None, b_month=None, b_year=None,
                 address2=None):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.mobile_number = mobile_number
        self.homephone = homephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.email = email_1
        self.email2 = email_2
        self.email3 = email_3
        self.all_emails_from_homepage = all_emails_from_homepage
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.address2 = address2
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
