Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <name>, <surname>, <title>, <company>, <address>, <mobile_number>, <homephone>, <workphone>, <secondaryphone>, <email_1>, <email_2>, <email_3>, <address2>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
| name  |  surname  |  title  |  company  |  address  |  mobile_number  |  homephone  |  workphone  |  secondaryphone  |  email_1  |  email_2  |  email_3  |  address2 |
| ihor  | wiesenfeld| mr      |   UBS     | Carolina  | 92834y92834     | 82467234    | 92364762934 |92y923649734      |  test@mail| test2@mail| test3@mail|  jbhsadcv |
| idsfr | dsdfsdfsdf| mr      |   UBS     | NJ        | 24823424422     | 82748923    | 82347837488 |788234787488      |  te23@mail| tes22@mail| wefff@mail|  fwefefwe |
| sdvse | er34fsefff| ms      |   luxoft  | LA        | 43857983457     | 94568783    | 32485779234 |92y923649734      |  3434@mail| fdwfd@mail| terfe@mail|  fefefeff |
| ihor  | wiesenfeld| mr      |   UBS     | Carolina  | 92834y92834     | 82467234    | 92364762934 |92y923649734      |  test@mail| test2@mail| test3@mail|  jbhsadcv |
| idsfr | dsdfsdfsdf| mr      |   UBS     | NJ        | 24823424422     | 82748923    | 82347837488 |788234787488      |  te23@mail| tes22@mail| wefff@mail|  fwefefwe |
| sdvse | er34fsefff| ms      |   luxoft  | LA        | 43857983457     | 94568783    | 32485779234 |92y923649734      |  3434@mail| fdwfd@mail| terfe@mail|  fefefeff |
| ihor  | wiesenfeld| mr      |   UBS     | Carolina  | 92834y92834     | 82467234    | 92364762934 |92y923649734      |  test@mail| test2@mail| test3@mail|  jbhsadcv |
| idsfr | dsdfsdfsdf| mr      |   UBS     | NJ        | 24823424422     | 82748923    | 82347837488 |788234787488      |  te23@mail| tes22@mail| wefff@mail|  fwefefwe |
| sdvse | er34fsefff| ms      |   luxoft  | LA        | 43857983457     | 94568783    | 32485779234 |92y923649734      |  3434@mail| fdwfd@mail| terfe@mail|  fefefeff |


Scenario Outline: Modify the existing contact
  Given a contact list with the contacts
  Given a random contact from the list
  Given a contact with the data
  When I enter new contact data
  Then the new contact list is equal to the old list with the edited contact


Scenario Outline: Delete the existing contact
  Given a contact list with the contacts
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list with no removed contact
