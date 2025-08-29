from xml.etree import ElementTree
import json
from nltk_data_pack_core.schema import NLTKDataPackage

index_xml_path = "../nltk_data/index.xml"

root = ElementTree.parse(index_xml_path).getroot()
packages = [NLTKDataPackage(**p.attrib) for p in root.find("packages")]

packages_dicts = [p.model_dump() for p in packages]
print(json.dumps(packages_dicts, indent=2))
