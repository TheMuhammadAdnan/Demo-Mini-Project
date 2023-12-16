import inflection


def camelize(value):
    return inflection.camelize(value, uppercase_first_letter=False)

