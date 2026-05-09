def parse_fix(message: str):
    fields = message.split("|")
    result = {}

    for field in fields:
        if "=" in field:
            tag, value = field.split("=", 1)
            result[tag] = value

    return result
