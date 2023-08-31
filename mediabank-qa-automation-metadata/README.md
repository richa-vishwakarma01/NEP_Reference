## Install Python
```
brew install  pyenv
pyenv install 3.8.12
pyenv use 3.8.12
```

## Install dependencies
```
pip install poetry
pyenv shell 3.8.12
poetry install
```

## Run test
```
pyenv shell 3.8.12
poetry run pytest -s -m "tag"
Ie:   poetry run pytest -s -m "ofblIntegration"
```