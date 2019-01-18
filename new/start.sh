#!/bin/bash

export PATH="/home/toptop/.pyenv/bin/:$PATH"
export PATH="/usr/local/bin/geckodriver:$PATH"

eval "$(pyenv init -)"

pyenv local 3.6.0
pyenv shell 3.6.0

python selenium_try.py
