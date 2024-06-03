DEFAULT_TEXT_MAX_LENGTH = 20

def is_empty(value):
    return not value

def is_exceeded(value, length = DEFAULT_TEXT_MAX_LENGTH):
    return len(value) > length

    