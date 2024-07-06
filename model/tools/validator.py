import re
def name_validator(name):
    return re.match("^[a-zA-Z]{1,30}$",name)

def national_id_validator(national_id):
    return re.match("^[a-zA-Z]{0,10}$",national_id)

