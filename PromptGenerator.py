class PromptGenerator:
    __PROMPT_BODY = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system",
             "content": "You are a helpful assistant. Your responses will be printed to the UNIX terminal. Please "
                        "maintain string width of 80 symbols and be aware of the character pool limitations. Feel "
                        "free to "
                        "use ASCII graphics. Avoid markdown in your responses. Provide answers in plaintext only."},
            {"role": "user", "content": "Hi"}
        ],
        "temperature": 0.7
    }
    __DEFAULT_MODEL = "gpt-4o-mini"

    def __init__(self):
        pass

    def get_body(self, prompt: str, model=None) -> dict:
        model = PromptGenerator.__DEFAULT_MODEL if model is None else model
        body = PromptGenerator.__PROMPT_BODY
        body["messages"][1]["content"] = prompt
        body["model"] = model
        return body
