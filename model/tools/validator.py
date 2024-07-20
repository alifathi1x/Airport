import re


def name_validator(name):
    return re.match("^[a-zA-Z]{1,30}$", name)


def national_id_validator(national_id):
    return isinstance(national_id, str) and re.match("^[0-9a-zA-Z]{10}$", national_id)


def passport_validator(passport):
    return isinstance(passport, str) and re.match("^{9}$", passport)
