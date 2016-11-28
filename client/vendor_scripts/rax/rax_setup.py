#!/usr/bin/env python

""" This script will produce the configuration file nessecary to update A records in the Rackspace Cloud"""


import json
from get_token import get_token
import requests
import sys

def find_domain_id(account_num, target_domain, headers, url):
	''' Parse through all domains under the account, to find our domain's ID. '''
	
	all_domains = requests.get(url + '/domains', headers=headers)

	for domain in all_domains.json()['domains']:
		if domain['name'] == target_domain:
			return domain['id']
		else:
			sys.exit("Was unable to find the domain '{}' under the supplied account".format(target_domain))


def find_record_id(account_num, domain_id, headers, url):
	''' Parse through all records under our domain, to find our A record's ID. '''
	
	all_records = requests.get(url + '/domains/{}/records'.format(domain_id), headers=headers)

	for record in all_records.json()['records']:
	    if record['name'] == 'exley.com.au' and record['type'] == 'A':
	        return record['id']


def main(username, api_key, account_num, target_domain):

	headers = { 'X-Auth-Token':get_token(username, api_key) }
	url = 'https://dns.api.rackspacecloud.com/v1.0/' + account_num

	domain_id = find_domain_id(account_num, target_domain, headers, url)
	record_ip = find_record_id(account_num, domain_id, headers, url)

	with open('../../../vendor_config.pkl', 'rb') as f:
		pickle.dump([domain_id, record_id, url, api_key, username], 'f')


if __name__ == '__main__':
	username = raw_input("Etner your Rackspace username: ")
	api_key = raw_input("Enter your Rackspace API key: ")
	account_num = raw_input("Enter your Rackspace account number: ")
	target_domain = raw_input("Enter the domain to be monitored: ")

	main(username, api_key, account_num, target_domain)
