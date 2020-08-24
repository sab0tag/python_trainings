from model.usr import User
import random
import string
import os.path  # define path to the file
import jsonpickle
import getopt  # read the command line options
import sys  # get access to the command line options


# read the args from the command line
try:
    # "n:" amount of generated data; "f:" file with generated data; [hint]
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file to save"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# set default values
n = 7 # count of new created contacts
f = "data/contacts.json" # file where all the contacts have to be saved

for o, a in opts:
    if o == "-n":
        n = int(a) # if option os convert amount of groups value to int
    elif o == "-f":
        f = a #


# gen random testdata
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [User(name="", surname="", nickname="", title="", company="", address="",
                 mobile_number="", homephone="", workphone="", secondaryphone="",
                 email_1="", email_2="", email_3="", address2="")] + [
               User(name=random_string("name", 10), surname=random_string("surname", 10),
                    nickname=random_string("nickname", 10), title=random_string("title", 10),
                    company=random_string("company", 5), address=random_string("address", 20),
                    mobile_number=random_string("mobile", 10), homephone=random_string("homephone", 10),
                    workphone=random_string("workphone", 10), secondaryphone=random_string("second", 10),
                    email_1=random_string("email", 10), email_2=random_string("email2", 10),
                    email_3=random_string("email3", 10),
                    address2=random_string("address2", 20))
               for i in range(5)
           ]

# define path to json file
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)  # get the current directory for file
# open it into a write mode
with open(file, "w") as out_file:
    jsonpickle.set_encoder_options("json", indent=2)
    out_file.write(jsonpickle.encode(testdata))
    # out_file.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))  # func to convert object into a dict
