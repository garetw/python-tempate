import os
import requests
import logging

###### Logging Module #######
#############################
level = {
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG
}.get(os.environ.get('LOG_LEVEL', 'INFO'))

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - sample_lib[%(process)s]: %(message)s',
    level=level,
    filename="./sample.log"
)
##############################

##### Modules #####
###################
def get_url_explicit_args(url, headers=None):
    try:
        r = requests.get(url, headers)
        return r
    except Exception as e:
        return e

def get_url_kwargs(**kwargs):
    try:
        r = requests.get(**kwargs)
        return r
    except Exception as e:
        return e
######################