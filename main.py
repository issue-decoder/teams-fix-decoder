from src.parser import parse_fix, summarize_fix
import json
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"8=FIX...|35=D|...\"")
        return

    message = sys.argv[1]

    parsed = parse_fix(message)
    summary = summarize_fix(parsed)

    print("\n--- PARSED FIX (JSON) ---")
    print(json.dumps(parsed, indent=2))

    print("\n--- HUMAN SUMMARY ---")
    print(summary)


if __name__ == "__main__":
    main()
