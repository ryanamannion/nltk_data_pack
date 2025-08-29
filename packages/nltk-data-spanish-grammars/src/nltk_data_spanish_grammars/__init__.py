from pathlib import Path
from nltk_data_pack_core.metadata import read_metadata

package = Path(__file__).parent.name
metadata = read_metadata(package)
