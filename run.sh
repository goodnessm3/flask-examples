#!/usr/bin/env bash
websocketd/websocketd --port=8080 tail -f guni.log &
gunicorn main:app -b 0.0.0.0:8000 --access-logfile guni.log --reload --reload-extra-file main/static --reload-extra-file main/templates