# teams-fix-decoder

## Overview

**Teams FIX Decoder** is a lightweight parsing tool designed to decode and structure FIX (Financial Information eXchange) messages received from logs or Microsoft Teams-based support channels.

It helps **Support engineers** quickly interpret raw FIX messages without manually parsing tag-value pairs.

---

## Problem Statement

FIX messages are:

* Hard to read in raw format
* Difficult for junior support engineers to debug quickly
* Often embedded in logs or chat messages (Teams, Slack, etc.)

This tool standardizes and simplifies decoding so that:

> Raw FIX logs → Structured, readable JSON output

---

## Features (MVP)

* Parse raw FIX message strings
* Convert tag-based format into human-readable key-value pairs
* Extract common FIX fields (MsgType, Sender, Target, OrderID, etc.)
* CLI support for quick debugging
* Extensible structure for future Teams bot / API integration

---

## Example

### Input

```
8=FIX.4.4|35=D|49=CLIENT1|56=SERVER1|11=ORDER123|55=AAPL|54=1|38=100
```

### Output

```json
{
  "BeginString": "FIX.4.4",
  "MsgType": "D",
  "SenderCompID": "CLIENT1",
  "TargetCompID": "SERVER1",
  "ClOrdID": "ORDER123",
  "Symbol": "AAPL",
  "Side": "Buy",
  "OrderQty": "100"
}
```

---

## Project Structure

```
teams-fix-decoder/
│
├── src/
│   ├── parser.py          # Core FIX parsing logic
│   ├── fix_decoder.py     # Mapping & decoding rules
│   └── utils.py           # Helper functions
│
├── samples/
│   └── sample_fix.log     # Example FIX messages
│
├── tests/
│   └── test_parser.py    # Unit tests
│
├── main.py               # CLI entry point
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/issue-decoder/teams-fix-decoder.git
cd teams-fix-decoder
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run a sample decode

```bash
python main.py "8=FIX.4.4|35=D|49=CLIENT|56=SERVER"
```

---

## Roadmap

### Phase 1 (Current)

* Basic FIX parsing engine
* CLI tool
* Sample logs

### Phase 2

* FIX dictionary mapping (full tag names)
* Error handling & validation
* Structured logging support

### Phase 3

* Microsoft Teams bot integration
* “Paste FIX → get decoded response” workflow
* Secure internal API for support teams

---

## Target Users

* Production Support Engineers (L1/L2)
* Trading application support teams
* Incident management engineers
* On-call support rotations

---

## Future Vision

Turn this into a **Teams-native support assistant**:

> Paste FIX message → instantly get decoded fields, explanations, and likely issue hints.

---

## Contributing

This project is in early stage. Contributions are welcome for:

* FIX tag mappings
* Parsing improvements
* Integration adapters (Teams, Slack, APIs)

---

## License

TBD

---
