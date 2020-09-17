*** Settings ***
Library  rf.AddressBook
Library  Collections
Library  BuiltIn

Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***

Add new contact
    ${old_list}=  Get contact List
    ${contact}=  New Contact  name  surname  company  address  mobile_number
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Modify contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    ${new_contact}=  New Contact  name1  surname1  company1  address1  mobile_number73268
    Modify Contact  ${contact}  ${new_contact}
    ${new_list}=  Get Contact List
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

