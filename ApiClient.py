import os
import requests
from PromptGenerator import PromptGenerator


class ApiClient:
    __COMPLETION_ENDPOINT = "/v1/chat/completions"
    __BASE_URL = "https://api.openai.com"

    def __init__(self, api_key):
        self.__api_key = api_key
        self.__generator = PromptGenerator()

    def __get_headers(self):
        return {"Authorization": f"Bearer {self.__api_key}", "Content-Type": "application/json"}

    def __get_endpoint(self, endpoint: str) -> str:
        return ApiClient.__BASE_URL + endpoint

    def __execute_post(self, url: str, data):
        return requests.post(url, headers=self.__get_headers(), json=data)

    def get_chat_completion_response(self, prompt):
        return self.__execute_post(self.__get_endpoint(ApiClient.__COMPLETION_ENDPOINT),
                                   self.__generator.get_body(prompt)).json()
