import importlib.metadata
import importlib.resources
import json
from pathlib import Path

from nltk_data_pack_core.schema import NLTKDataPackage


def normalize_module_name(dist_name: str) -> str:
    """Normalizes dist name to module name."""
    return dist_name.replace("-", "_")


def read_metadata(name: str) -> NLTKDataPackage:
    module_name = normalize_module_name(name)
    module_path = importlib.resources.files(module_name)
    try:
        metadata = module_path.joinpath("package_metadata.json").read_text()
        metadata = NLTKDataPackage(**json.loads(metadata))
    except FileNotFoundError:
        raise FileNotFoundError(
            "Could not find metadata"
        )
    return metadata


if __name__ == "__main__":
    print(read_metadata("nltk-data-abc").model_dump_json(indent=2))
