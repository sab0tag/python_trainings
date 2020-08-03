# from sys import maxsize


class User:

    def __init__(self, name=None, surname=None, nick=None, titl=None, company_name=None, street=None,
                 mobile_number=None, email_1=None, email_2=None, b_day=None, b_month=None, b_year=None, street2=None, id=None):
        self.name = name
        self.surname = surname
        self.nick = nick
        self.titl = titl
        self.company_name = company_name
        self.street = street
        self.mobile_number = mobile_number
        self.email_1 = email_1
        self.email_2 = email_2
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.street2 = street2
        self.id = id
'''
    def __repr__(self):
        return "%s %s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize '''
