class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = {".com", ".bg", ".org", ".net"}

while True:
    line = input()
    if line == 'End':
        break

    if '@' not in line:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = line.split('@')

    if len(name) <= 4:
        raise NameTooShortError("The name must be more than 4 characters")

    if line[line.index("."):] not in VALID_DOMAINS:
        raise InvalidDomainError("The domain must be valid")

    print("Email is valid")
