# nltk_data_pack

Installable packages for nltk_data

# Intended Workflow

## Installation 

### With uv

Specify your dependency and the link to git as the source in `pyproject.toml`

```toml
[project]
# ...
dependencies = [
    "nltk-data-spanish-grammars"
]

[tool.uv.sources]
nltk-data-spanish-grammars = { url = "https://github.com/..." }
```

### With pip via requirements.txt

```text
# requirements.txt
nltk-data-spanish-grammars @ https://github.com/...
```

```bash
$ pip install -r requirements.txt
```

## Using with nltk

```python
import nltk_data_pack

nltk_data_pack.configure_nltk_data()
```

# Ideas

* Loop through all installed packages, add their path to nltk.data.path list