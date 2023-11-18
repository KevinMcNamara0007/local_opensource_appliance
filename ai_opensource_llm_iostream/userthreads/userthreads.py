import re
import textwrap
from typing import Optional, Tuple

from modelthreads.modelthreads import ModelThreads
from userthreads.messagestore import MessageStore
from userthreads.userthread import UserThread


class UserThreads:

    def __init__(self):
        self._user_mapping: Optional[dict] = dict()
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
        is_model_update_message = message.upper().find('!MODEL') != -1
        if (not is_model_update_message) and (user.chat_model_name is None):
            msg = MessageStore.MODEL_NOT_SET.value
            msg = msg.format(self._model_threads.model_names)
            response = textwrap.dedent(msg)
            response = response.strip()
            return response

        if is_model_update_message:
            find_list = re.findall(r"!MODEL\s*(\w*)\s*", message.upper())
            if (len(find_list) == 0) or (find_list[0].upper() not in self._model_threads.model_names):
                msg = MessageStore.MODEL_PARSE_ERROR.value
                msg = msg.format(self._model_threads.model_names)
                response = textwrap.dedent(msg)
                response = response.strip()
                return response

            else:
                try:
                    user.chat_model_name = find_list[0].upper()
                    msg = MessageStore.MODEL_SET_SUCCESS.value
                    msg=msg.format(user.chat_model_name)
                    response = textwrap.dedent(msg)
                    response = response.strip()
                    return response

                except Exception as e:
                    msg = MessageStore.MODEL_SET_FAIL.value
                    msg=msg.format(user.chat_model_name)
                    response = textwrap.dedent(msg)
                    response = response.strip()
                    print(str(e))
                    return response

        model_name = user.chat_model_name
        model_thread = self._model_threads.get_modelthread(model_name)
        response = model_thread.chat_completions_fake(message)
        # response = model_thread.chat_completions(message)
        user.append_chat_list(message)
        user.append_chat_list(response)

        return response
