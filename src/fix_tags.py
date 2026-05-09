# =========================
# FIX TAGS (Field Dictionary)
# =========================

FIX_TAGS = {
    "8": "BeginString",
    "9": "BodyLength",
    "35": "MsgType",
    "49": "SenderCompID",
    "56": "TargetCompID",
    "34": "MsgSeqNum",
    "52": "SendingTime",

    "11": "ClOrdID",
    "37": "OrderID",
    "41": "OrigClOrdID",
    "17": "ExecID",

    "55": "Symbol",
    "48": "SecurityID",
    "22": "SecurityIDSource",

    "54": "Side",
    "38": "OrderQty",
    "40": "OrdType",
    "44": "Price",
    "59": "TimeInForce",
    "60": "TransactTime",
    "126": "ExpireTime",

    "39": "OrdStatus",
    "150": "ExecType",
    "151": "LeavesQty",
    "14": "CumQty",
    "6": "AvgPx",

    "10": "CheckSum",
    "21": "HandlInst",
    "109": "ClientID",
}


# =========================
# ENUM DECODERS
# =========================

MSGTYPE_MAP = {
    "D": "New Order Single",
    "8": "Execution Report",
    "F": "Order Cancel Request",
    "G": "Order Cancel/Replace Request",
    "0": "Heartbeat",
    "1": "Test Request",
    "2": "Resend Request",
    "3": "Reject",
    "4": "Sequence Reset",
    "5": "Logout"
}

SIDE_MAP = {
    "1": "Buy",
    "2": "Sell",
    "3": "Buy Minus",
    "4": "Sell Plus",
    "5": "Sell Short",
    "6": "Sell Short Exempt"
}

ORDSTATUS_MAP = {
    "0": "New",
    "1": "Partially Filled",
    "2": "Filled",
    "3": "Done for Day",
    "4": "Canceled",
    "5": "Replaced",
    "6": "Pending Cancel",
    "8": "Rejected"
}

EXECTYPE_MAP = {
    "0": "New",
    "1": "Partial Fill",
    "2": "Fill",
    "4": "Canceled",
    "5": "Replaced",
    "8": "Rejected"
}

ORDTYPE_MAP = {
    "1": "Market",
    "2": "Limit",
    "3": "Stop",
    "4": "Stop Limit"
}

TIMEINFORCE_MAP = {
    "0": "Day",
    "1": "Good Till Cancel",
    "3": "Immediate or Cancel",
    "4": "Fill or Kill"
}
