#!/bin/bash

declare -px > /tmp/.env
chmod 0644 /tmp/.env
python edge_server.py
