import re
import textwrap
from typing import Optional, Tuple

from userthread import UserThread
from ..modelthreads.modelthreads import ModelThreads
from messagestore import MessageStore

class UserThreads:

    def __init__(self):
        self._user_mapping: Optional[dict] = None
        self._model_threads: ModelThreads = ModelThreads()

    def get_user(self, identifier: Tuple[str, int]) -> UserThread:
        if not (identifier in self._user_mapping):
            self._user_mapping[identifier] = UserThread(identifier)

        return self._user_mapping[identifier]

    def is_model_change_chat(self):
        pass

    def chat(self, identifier: Tuple[str, int], message: str):
        user = self.get_user(identifier)
        response = None
        if user.chat_model_name is None:
            msg = MessageStore.MODEL_NOT_SET.value
            msg.format(self._model_threads.model_names)
            response = textwrap.dedent(msg)
            response = response.strip()
            return response

        else:
            if message.upper().find('!MODEL'):
                find_list = re.findall(r"!MODEL\s*(\w*)\s*", message.upper())
                if len(find_list) == 0:
                    msg = MessageStore.MODEL_PARSE_ERROR.value
                    msg.format(self._model_threads.model_names)
                    response = textwrap.dedent(msg)
                    response = response.strip()
                    return response

                else:
                    try:
                        user.chat_model_name = find_list[0]
                        msg = MessageStore.MODEL_SET_SUCCESS.value
                        response = textwrap.dedent(msg)
                        response = response.strip()
                        return response

                    except Exception as e:
                        msg = MessageStore.MODEL_SET_FAIL.value
                        response = textwrap.dedent(msg)
                        response = response.strip()
                        print(str(e))
                        return response
