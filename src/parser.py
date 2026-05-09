from src.fix_tags import FIX_TAGS, SIDE_MAP

def parse_fix(message: str):
    fields = message.split("|")
    result = {}

    for field in fields:
        if "=" in field:
            tag, value = field.split("=", 1)

            name = FIX_TAGS.get(tag, tag)

            # decode side
            if tag == "54":
                value = SIDE_MAP.get(value, value)

            result[name] = value

    return result
