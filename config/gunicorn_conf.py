import os

def numCPUs():
    if not hasattr(os, "sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")

bind = "127.0.0.1:8001"
pidfile = "/tmp/gunicorn.pid"
logfile = "/tmp/production.log"
accesslog = "/tmp/production.log"
errorlog = "/tmp/errors.log"
loglevel = "debug"
name = "socialq"
timeout = 60*60	
max_requests = 1000
workers = numCPUs()*1

