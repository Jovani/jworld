"""
The HOSTMAP variable is a dictionary of lists. The keys represent
roles of a server, the values represent the hostnames of machines that
fill those roles. If you are reading this, you likely know what you're
doing. If you don't know what you're doing, you probably want to put
your hostname into local_dev. Ensure it has a comma at the end, and
the hostname is a string.

You can get your hostname by typing `hostname` into a terminal.
"""
import os
import sys
import socket
from django.utils import importlib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.append(os.path.join(BASE_DIR, 'conf/settings'))

HOSTMAP = {
    'default': [
        'jworld',
    ],
}


def update_current_settings(file_name):
    """
    Given a filename, this function will insert all variables and
    functions in ALL_CAPS into the global scope.
    """
    new_settings = importlib.import_module(file_name)
    for k, v in new_settings.__dict__.items():
        if k.upper() == k:
            globals().update({k: v})

current_hostname = socket.gethostname()

to_load = []

for key, hosts in HOSTMAP.items():
    if current_hostname in hosts:
        to_load.append(key)

for host_file in to_load:
    try:
        update_current_settings(host_file)
    except ImportError:
        print('Error importing {}!'.format(host_file))

if not to_load:
    try:
        update_current_settings('localsettings')
    except ImportError:
        print('Error importing localsettings!')
