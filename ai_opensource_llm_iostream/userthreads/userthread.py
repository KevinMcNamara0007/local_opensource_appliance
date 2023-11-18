from typing import Tuple, Optional, List


class UserThread:
    def __init__(self, identifier: Tuple[str, int]):
        self._identifier = identifier
        self._chat_model_name: Optional[str] = None
        self._chat_list: Optional[List[str]] = None

    @property
    def identifier(self) -> Tuple[str, int]:
        return self._identifier

    @property
    def chat_model_name(self) -> Optional[str]:
        return self._chat_model_name

    @property
    def chat_list(self) -> Optional[List[str]]:
        return self._chat_list
