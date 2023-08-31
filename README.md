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
## Create Bastion Host to connect to access API Endpoints
````
To connect to  bastion host please refer
https://nepglobal.atlassian.net/wiki/spaces/MEDPRO/pages/353305072/Using+a+bastion+host
````

## Run test
```
pyenv shell 3.8.12
poetry run pytest -s -m "tag"
Ie:   poetry run pytest -s -m "helloWorld"
```

### How to run the tests (AWS scenarios)
1. Go to AWS Account and get your personal ACCESS KEY, SECRET ACCESS KEY and SESSION TOKEN for using account,
2. Put them in `.env` file as following
   ```
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   AWS_SESSION_TOKEN=
   ```
   
