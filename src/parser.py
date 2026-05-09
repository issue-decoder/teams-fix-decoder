from src.fix_tags import (
    FIX_TAGS,
    MSGTYPE_MAP,
    SIDE_MAP,
    ORDSTATUS_MAP,
    EXECTYPE_MAP,
    ORDTYPE_MAP,
    TIMEINFORCE_MAP
)


def _decode(tag, value):
    """Apply FIX enum decoding where applicable."""
    if tag == "35":
        return MSGTYPE_MAP.get(value, value)

    if tag == "54":
        return SIDE_MAP.get(value, value)

    if tag == "39":
        return ORDSTATUS_MAP.get(value, value)

    if tag == "150":
        return EXECTYPE_MAP.get(value, value)

    if tag == "40":
        return ORDTYPE_MAP.get(value, value)

    if tag == "59":
        return TIMEINFORCE_MAP.get(value, value)

    return value


def parse_fix(message: str):
    """
    Parse raw FIX string into structured dictionary.
    """
    fields = message.split("|")
    result = {}

    for field in fields:
        if "=" in field:
            tag, value = field.split("=", 1)

            name = FIX_TAGS.get(tag, tag)
            decoded_value = _decode(tag, value)

            result[name] = decoded_value

    return result


def summarize_fix(parsed: dict) -> str:
    """
    Convert parsed FIX into human-readable summary.
    """
    summary = []

    msg_type = parsed.get("MsgType")
    side = parsed.get("Side")
    symbol = parsed.get("Symbol")
    qty = parsed.get("OrderQty")
    status = parsed.get("OrdStatus")
    price = parsed.get("Price")

    if msg_type:
        summary.append(f"Message Type: {msg_type}")

    if side and symbol and qty:
        summary.append(f"{side} order for {qty} shares of {symbol}")

    if price:
        summary.append(f"Price: {price}")

    if status:
        summary.append(f"Status: {status}")

    return " | ".join(summary)
