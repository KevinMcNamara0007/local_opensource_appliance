import os

from llama_cpp import Llama


class ModelThread:

    def __init__(self, model_name: str, model_path: str):
        self.model_name = model_name
        self.model_path = model_path

        # Setting verbose to False in Llama
        self.llm = Llama(
            model_path=self.model_path,
            n_ctx=8192,
            n_batch=512,
            n_threads=7,
            n_gpu_layers=2,
            verbose=False,
            seed=42,
        )

    def model_response_complete(self, query: str):
        output = ""
        try:
            output = self.llm(query, echo=True, stream=False, max_tokens=4096)
        except Exception as e:
            print("[LLM RESPONSE FAIL] Failure in instruct response from local llm")
            print(self.get_model_props())
            print(str(e))
        return output

    def chat_completions_full(self, query: str):
        output = ""
        try:
            output = self.llm(query, echo=True, stream=False, max_tokens=4096)
        except Exception as e:
            print("[LLM RESPONSE FAIL] Failure in chat completion response from local llm")
            print(self.get_model_props())
            print(str(e))
        return output

    def model_response(self, query: str):
        output = ""
        try:
            output = self.llm(query, echo=True, stream=False, max_tokens=4096)
        except Exception as e:
            print("[LLM RESPONSE FAIL] Failure in instruct response from local llm")
            print(self.get_model_props())
            print(str(e))

        try:
            output = output = output['choices'][0]['text']

        except Exception as e:
            print("[RESPONSE EXTRACT FAIL] Failure in instruct response extraction local llm")
            print(str(e))
        return output

    def chat_completions(self, query: str):
        output = ""
        try:
            output = self.llm(query, echo=True, stream=False, max_tokens=4096)
        except Exception as e:
            print("[LLM RESPONSE FAIL] Failure in chat completions response from local llm")
            print(self.get_model_props())
            print(str(e))

        try:
            output = output = output['choices'][0]['text']

        except Exception as e:
            print("[RESPONSE EXTRACT FAIL] Failure in chat completions response extraction local llm")
            print(str(e))
        return output

    def get_model_props(self):
        props = {
            "name": self.model_name,
            "path": self.model_path
        }
        return props


def test_run():
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv('config.env'))

    model_name = "Zephyr"
    model_path = os.getenv('ZEPHYR_PATH', None)
    if model_path is None:
        raise Exception('model path is invalid! Correct path in config.env file')
    print("model path : ", model_path)

    model = ModelThread(model_name, model_path)

    return


if __name__ == '__main__':
    test_run()
