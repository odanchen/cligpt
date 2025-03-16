import sys
from ResponseParser import ResponseParser
import os

if __name__ == "__main__":
    api_key = os.environ.get("OPENAI_API_KEY")
    parser = ResponseParser(api_key)

    prompt = " ".join(sys.argv[1:])
    print(parser.get_response(prompt))
