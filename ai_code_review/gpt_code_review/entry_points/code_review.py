import sys
import openai
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="A simple code review for generic pull requests")
    parser.add_argument("-a", "--apikey", type=str, required=True, help="The file path to text file holding open ai api-key")
    parser.add_argument("-f", "--file", type=str, default=20, help="The file to be reviewed.")
    return parser.parse_args()
# from openai import OpenAIAPIException

def get_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()

def read_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def send_code_for_review(api_key, code):
    openai.api_key = api_key
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Review the following code. If you find inconsistencies, possible bugs or better ways to style or "
             "organize code suggest them. Be on the lookout for duplicated or excess code that could be otherwise "
             "refactored into a function. For any existing functions, lacking a docstring, you should provide a dock "
             "string. Also look for missing type hints. Your goal is to review the code and create comments that will "
             "enhance readability and collaboration as much as possible. Here is the code:\n\n" + code,
      temperature=0.3,
      max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    args = parse_args()


    api_key_file = args.apikey
    code_file = args.file

    api_key = get_api_key(api_key_file)
    code = read_code(code_file)

    review = send_code_for_review(api_key, code)
    print("Code review:")
    print(review)

if __name__ == "__main__":
    main()
