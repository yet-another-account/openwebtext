# OpenWebText

This project is a clone of the GPT-2 WebText dataset as outlined in the [OpenAI paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). This project is still heavily WIP.

## Dependencies

Pipenv, Python 3,

To install python dependencies:
```
pipenv install
```

[Newspaper](https://github.com/codelucas/newspaper#get-it-now) Dependencies:

On Ubuntu:
```
sudo apt-get install libxml2-dev libxslt-dev
```
On OS X:
```
brew install libxml2 libxslt
```
## Usage

1. Get list of URLs from reddit:

```
pipenv run python get_urls.py
```

2. Download data from URLs:

```
pipenv run python download.py
```

Resulting files will be deposited in `data/` with format `{domain}-{sha256 hash of url}.txt`.

Enjoy!
