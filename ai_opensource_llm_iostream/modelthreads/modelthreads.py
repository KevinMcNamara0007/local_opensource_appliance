from pathlib import Path
from typing import Tuple, Optional, List

from dotenv import find_dotenv, dotenv_values

from modelthreads.modelthread import ModelThread


class ModelThreads:
    def __init__(self):
        self._model_names = None
        self._model_details_dict = None
        self.refresh_state()

    @property
    def model_names(self) -> List[str]:
        return self._model_names

    @property
    def model_details_dict(self) -> dict:
        return self._model_details_dict

    def _isvalid_model_name(self, name):
        name = name
        if name.upper() in self._model_names:
            indx = self._model_names.index(name.upper())
            return True, self._model_names[indx]
        else:
            return False, None

    def refresh_state(self) -> None:
        res = dotenv_values(find_dotenv('models.env'))
        base_path = res.get('BASE_PATH', None)
        if not base_path:
            raise Exception('[ENV] BASE_PATH for models folder not defined in environment')

        base_path = Path(base_path)
        if not base_path.exists():
            raise Exception('[ENV] BASE_PATH for models folder Invalid')

        res.pop('BASE_PATH')

        model_names = list(res)

        if len(model_names) == 0:
            raise Exception('[ENV] No Models Specified in Environment')

        self._model_names = model_names.copy()

        model_details_dict = dict(res)

        for model_name in model_details_dict:
            model_path = base_path.joinpath(model_details_dict[model_name])
            if not model_path.exists():
                raise Exception(f'[ENV] resultant path invalid for {model_name}')
            model_details_dict[model_name] = model_path.resolve()

        self._model_details_dict = model_details_dict.copy()

    def get_model_details_name(self, search_model_name: str) -> Tuple[str, Path]:
        if search_model_name not in self._model_names:
            raise Exception(f'[ENV] Details for Model - {search_model_name} NOT FOUND')
        return search_model_name, self._model_details_dict.get(search_model_name)

    def get_model_details_index(self, search_model_index: int) -> Tuple[str, Path]:
        if not (0 <= search_model_index <= (len(self._model_names) - 1)):
            raise Exception(f'[ENV] Details for Model Index - {search_model_index} NOT FOUND')

        search_model_name = self._model_names[search_model_index]
        return search_model_name, self._model_details_dict.get(search_model_name)

    def get_modelthread(self, name=None, index=None) -> Optional[ModelThread]:
        if name is not None:
            if not isinstance(name, str):
                raise Exception(f'[MODEL] NAME of Model {name} is not a String')
            isvalid, key_name = self._isvalid_model_name(name)
            if isvalid:
                model_details = self.get_model_details_name(key_name)
                model_name = model_details[0]
                model_path = str(model_details[1])
                return ModelThread(model_name, model_path)
            else:
                print('Keyname provided to modelthread is not valid!')
                return None

        # Flow for index
        if index is not None:
            if not isinstance(index, int):
                raise Exception(f'[MODEL] INDEX of Model {index} is not an Integer')

            model_details = self.get_model_details_index(index)
            model_name = model_details[0]
            model_path = str(model_details[1])
            return ModelThread(model_name, model_path)

        return None
