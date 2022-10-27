#!/bin/bash

declare -px > /tmp/.env
chmod 0644 /tmp/.env
python server.py
