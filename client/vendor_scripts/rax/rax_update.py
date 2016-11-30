#!/usr/bin/env python

""" This script will perform an A record update. Warning: we're entering the danger zone here. Be careful, and don't pass silly values in! """

import json
import requests
import pickle
from get_token import get_token


def update_record(token, current_ip, url, domain_id, record_id):
    ''' This module will use the PUT method to update the specified A record'''
    
    payload = { 'data':current_ip }
    headers = { 'x-auth-token':token , 'Content-Type': 'application/json' } 
    
    for header in headers:
    	print('{}:{}'.format(header, headers[header]))

    try:
    	print('Putting header: {}, payload {} to {}'.format(headers, json.dumps(payload), url + '/domains/{}/records/{}'))
	update_record = requests.put(url + '/domains/{}/records/{}'.format(domain_id, record_id), data=json.dumps(payload), headers=headers)
    	print(url + '/domains/{}/records/{}'.format(domain_id, record_id))
	print(update_record.status_code)
	print(update_record.text)
    except:
    	raise

def main(current_ip):
    
    with open('rax_config.pkl', 'rb') as f:
        domain_id, record_id, url, api_key, username  = pickle.load(f)

    token = get_token(username, api_key)

    print("Rackspace domain ID : {}".format(domain_id))
    print("A record ID: {}".format(record_id))
    print("API URL: {}".format(url))
    update_record(token, current_ip, url, domain_id, record_id)

if __name__ == '__main__':
	sys.exit("This module needs to be called by another script. Exiting.")
