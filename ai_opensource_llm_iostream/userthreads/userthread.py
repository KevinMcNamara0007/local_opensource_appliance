from typing import Tuple, Optional, List


class UserThread:
    def __init__(self, identifier: Tuple[str, int]):
        self._identifier = identifier
        self._chat_model_name: Optional[str] = None
        self._chat_list: List[str] = []

    @property
    def identifier(self) -> Tuple[str, int]:
        return self._identifier

    @property
    def chat_model_name(self) -> Optional[str]:
        return self._chat_model_name

    @chat_model_name.setter
    def chat_model_name(self, preferred_model_name):
        if not (isinstance(preferred_model_name, str)):
            raise TypeError('Preferred Model Name should be string')
        else:
            self._chat_model_name = preferred_model_name

    @property
    def chat_list(self) -> Optional[List[str]]:
        return self._chat_list

    def append_chat_list(self, text: str) -> bool:
        try:
            self._chat_list.append(text)
            return True
        except Exception as e:
            print("[Exception] Occurred")
            print(e)
            return False
