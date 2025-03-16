from ApiClient import ApiClient


class ResponseParser:
    __PREFIX = "gpt>"

    def __init__(self, api_key: str):
        self.__api_client = ApiClient(api_key)

    def get_response(self, prompt: str) -> str:
        response = self.__api_client.get_chat_completion_response(prompt)
        message = self.__extract_message(response)
        return "\n".join([f"{self.green(self.__PREFIX)} {line}" for line in message.split("\n") if line])

    @staticmethod
    def green(txt: str) -> str:
        return f"\033[32m{txt}\033[0m"

    def __extract_message(self, response: dict) -> str:
        return response["choices"][0]["message"]["content"]
