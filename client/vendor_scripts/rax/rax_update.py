#!/usr/bin/env python

""" This script will perform an A record update. Warning: we're entering the danger zone here. Be careful, and don't pass silly values in! """

import json
import requests
from get_token import get_token


def update_record(token, current_ip, url, domain_id, record_id):
    ''' This module will use the PUT method to update the specified A record'''
    
    payload = { 'data':current_ip }
    headers = { 'X-Auth-Header':token , 'Content-Type': 'application/json' } 
    
    update_record = request.put(url + '/domains/{}/records{}'.format(domain_id, record_id), data=json.dumps(payload), headers=headers)

def main(current_ip):
    
    with open('../../../vendor_config.pkl', 'rb') as f:
        domain_id, record_id, url, api_key, username  = pickle.load(f)

    token = get_token(username, api_key)

    update_record(token, current_ip, url, domain_id, record_id)

if __name__ == '__main__':
	sys.exit("This module needs to be called by another script. Exiting.")