"""
This file contains a function that will read the lottie animations as json data.
"""
import requests


def read_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()