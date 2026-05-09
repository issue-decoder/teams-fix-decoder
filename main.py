from src.parser import parse_fix
import json
import sys

def main():
    message = sys.argv[1]
    result = parse_fix(message)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
