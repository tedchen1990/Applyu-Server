# This is not for install steps, it's about server, do not change any things here 

# Applyu-Server

# uvicorn main:applyu --reload

# lsof -t -i tcp:8000 | xargs kill -9

# gunicorn -w 4 -k uvicorn.workers.UvicornWorker  main:applyu --reload -D

# pkill gunicorn 

# https://docs.gunicorn.org/en/latest/sttings.html#settings
