Scenario Outline: Add new group
  Given a group list
  Given a group with <groupName>, <headerDescr> and <footerDescr>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  | groupName | headerDescr | footerDescr |
  | name1     | descr1      | descr2      |
  | name2     | descr2      | descr2      |
  | name3     | descr3      | descr3      |
