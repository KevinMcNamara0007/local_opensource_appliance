from dotenv import find_dotenv, dotenv_values
from llama_cpp import Llama


class ModelThread:
    """
    Low Level Manager Component for every Model Connection.
    Attributes:
        - model_name(str)       : Alias name for model
        - model_path(str)       : System resolved path of model (based on OS)
        - llm(Llama)            : Llama Object for given configuration
    """

    def __init__(self, model_name: str, model_path: str):
        self.model_name = model_name
        self.model_path = model_path

        # Original Loader
        # Setting verbose to False in Llama
        # self.llm = Llama(
        #     model_path=self.model_path,
        #     n_ctx=8192,
        #     n_batch=512,
        #     n_threads=7,
        #     n_gpu_layers=2,
        #     verbose=False,
        #     seed=42,
        # )

        # Loader from .env
        args = dotenv_values(find_dotenv('model_args.env'))
        for key, value in args.items():
            args[key] = int(value)
        self.llm = Llama(
            model_path=self.model_path,
            **args,
            verbose=False
        )

    def model_response_complete(self, query: str) -> dict:
        """
        Get Complete Model response object from Model for Query
        :param query: User Query
        :return: response as dictionary
        """
        output = ""
        try:
            output = self.llm(query, echo=True, stream=False, max_tokens=4096)
        except Exception as e:
            print("[LLM RESPONSE FAIL] Failure in instruct response from local llm")
            print(self.get_model_props())
            print(str(e))
        return output

    def chat_completions_full(self, query: str) -> dict:
        """
        Get Complete Model response object from Model for Query
        :param query: User Query
        :return: response as dictionary
        """
        output = ""
        try:
            output = self.llm(query, echo=True, stream=False, max_tokens=4096)
        except Exception as e:
            print("[LLM RESPONSE FAIL] Failure in chat completion response from local llm")
            print(self.get_model_props())
            print(str(e))
        return output

    def model_response(self, query: str) -> str:
        """
        Get Model response output object from Model for Query
        :param query: User Query
        :return: response text
        """
        output = ""
        try:
            output = self.llm(query, echo=True, stream=False, max_tokens=4096)
        except Exception as e:
            print("[LLM RESPONSE FAIL] Failure in instruct response from local llm")
            print(self.get_model_props())
            print(str(e))

        try:
            print("deb")
            print(output)
            output = output['choices'][0]['text']

        except Exception as e:
            print("[RESPONSE EXTRACT FAIL] Failure in instruct response extraction local llm")
            print(str(e))
        return output

    def chat_completions(self, query: str) -> str:
        """
        Get Model response output object from Model for Query
        :param query: User Query
        :return: response text
        """
        output = ""
        try:
            # print("deb")
            # print(query)
            output = self.llm(query, echo=True, stream=False, max_tokens=4096)
        except Exception as e:
            print("[LLM RESPONSE FAIL] Failure in chat completions response from local llm")
            print(self.get_model_props())
            print(str(e))

        try:
            # print("deb")
            # print(output)
            output = output['choices'][0]['text']

        except Exception as e:
            print("[RESPONSE EXTRACT FAIL] Failure in chat completions response extraction local llm")
            print(str(e))
        return output

    def chat_completions_fake(self, query: str) -> str:
        """
        A fake model response generater for response and flow testing with model details
        :param query: User Query
        :return: response string
        """
        output = f'''\
{self.model_name}
My response for {query} is ...
        '''
        return output

    def chat_completions_fake_2(self, query: str) -> str:
        """
        A fake model response generater for response and flow testing with model details
        :param query: User Query
        :return: response string
        """
        output = f'''\
Input to Model:
{query}
Output of Model:
<fake message>
        '''
        return output

    def get_model_props(self):
        props = {
            "name": self.model_name,
            "path": self.model_path
        }
        return props
