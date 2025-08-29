from typing import Optional, Annotated, Any

from pydantic import BaseModel, Field, BeforeValidator, ConfigDict


def parse_boolean(value: Any) -> Any:
    if isinstance(value, int):
        return bool(value)
    elif (
            isinstance(value, str)
            and value.lower() in ["true", "1", "false", "0", "yes", "no"]
    ):
            return bool(value)
    return value


class NLTKDataPackage(BaseModel):
    id: str
    name: str
    unzip: Annotated[bool, BeforeValidator(parse_boolean)]
    unzipped_size: int
    size: int
    checksum: str
    subdir: str
    url: str

    webpage: Optional[str] = None
    author: Optional[str] = None
    contact: Optional[str] = None
    license: Optional[str] = None
    languages: Optional[str] = None
    copyright: Optional[str] = None
    note: Optional[str] = None
    license_url: Optional[str] = Field(None, alias="licenseurl")
    sample: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    available: Annotated[bool, BeforeValidator(parse_boolean)] = True

    model_config = ConfigDict(populate_by_name=True)
