#!/bin/bash

# Executes the covid count retriever
export PYTHONPATH=$PYTHONPATH:$(pwd)
config_file=resources/config.json
python src/main.py -c $config_file
