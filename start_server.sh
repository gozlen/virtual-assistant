#!/bin/bash
rasa run actions &
rasa run -v --endpoints endpoints.yml --log-file log &
