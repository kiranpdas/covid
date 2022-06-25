#!/bin/bash

# Executes the covid count retriever
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
config_file=kpra_covid/resources/config.json
python kpra_covid/main.py -c $config_file
