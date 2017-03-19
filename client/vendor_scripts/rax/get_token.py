#!/usr/bin/env python

"""This script will obtain an auth token from the Rackspace cloud """

import sys
import json
import requests

def get_token(username, api_key):

    url = 'https://identity.api.rackspacecloud.com/v2.0/tokens'
    payload = {"auth":{"RAX-KSKEY:apiKeyCredentials":{"username":username,"apiKey":api_key}}}
    headers = {'Content-Type': 'application/json'}

    # Attempt to hit the authentication API
    try:
        print("Grabbing a token from {}".format(url))
        r = requests.post(url, data=json.dumps(payload), headers=headers)
    except:
        sys.exit("\n\nUnable to call the Rackspace API, exiting.")

    # If successful, return the token
    return(r.json()['access']['token']['id'])


if __name__ == '__main__':

    username = raw_input("Enter your Rackspace Cloud username: ")
    api_key = raw_input("Enter your Rackspace account's API key: ")

    print("Your token is:\n{}".format(get_token(username, api_key)))