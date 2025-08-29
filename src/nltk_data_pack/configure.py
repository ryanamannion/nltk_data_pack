import atexit
import importlib.metadata
import tempfile
import zipfile
from importlib import import_module, resources
from pathlib import Path
from typing import Iterator

import nltk

from nltk_data_pack_core.metadata import normalize_module_name


def get_installed_nltk_data_dists() -> Iterator[importlib.metadata.Distribution]:
    for dist in importlib.metadata.distributions():
        if "nltk-data-" in dist.name and dist.name != "nltk-data-pack":
            yield dist


def get_installed_dists_paths():
    dists_paths = {}
    for dist in get_installed_nltk_data_dists():
        module_name = normalize_module_name(dist.name)
        module = import_module(module_name)
        module_dir = getattr(module, "__file__", None)
        if module_dir is not None:
            module_dir = Path(module_dir).parent
        dists_paths[module_name] = module_dir
    return dists_paths


class NLTKDataManager:
    _instance = None
    _temp_dir = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(NLTKDataManager, cls).__new__(cls, *args, **kwargs)
            atexit.register(cls._instance.cleanup)
        return cls._instance

    def __init__(self):
        if self._temp_dir is None:
            self._temp_dir = tempfile.TemporaryDirectory()
            # TODO:
            print(f"NLTK data configured at: {self._temp_dir.name}")

    def _unzip_data(self):
        with importlib.resources.path('your_package_name.data', 'nltk_data.zip') as zip_path:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self._temp_dir.name)

    def _configure_nltk(self):
        # Add the temporary directory to NLTK's data path
        nltk.data.path.append(self._temp_dir.name)

    def cleanup(self):
        # This function is called automatically when the program exits
        if self._temp_dir:
            self._temp_dir.cleanup()
            self._temp_dir = None
            print("NLTK temporary data directory cleaned up.")


def configure_nltk_data():
    NLTKDataManager()


if __name__ == "__main__":
    print(get_installed_dists_paths())
