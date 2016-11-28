#!/usr/bin/env python

""" This script will save the required information for the client to use on a continual basis """


import pickle
import sys
from pick import pick
import requests

def main():
    
    # Gather user requirements
    target_domain = raw_input("Enter the domain you'd like to monitor: ").strip()
    server = raw_input("Enter the FQDN (or IP address) of the host running the server application. Format should be http://host.com:port: ").strip()
    
    # Which DNS provider will we be using?
    providers = ['Rackspace: Cloud DNS', 'AWS: Route 53']
    provider_question = "Which DNS service will we be using?"
    discard, provider_index = pick(providers, provider_question)

    if provider_index == 0:

        provider = 'rax'
        account_num = raw_input("Enter your Rackspace Cloud account number: ")
        username = raw_input("Enter your Rackspace Cloud username: ").strip()
        api_key = raw_input("Enter your API key: ").strip()

        import vendor_scripts.rax.rax_setup
        vendor_scripts.rax.rax_setup.main(username, api_key, account_num, target_domain)

    else:
        sys.exit("Only RAX US is supported right now, other options coming soon...")

    # Save for the client application
    with open('config.pkl', 'wb') as f:
        pickle.dump([target_domain, server, provider], f)


if __name__ =='__main__':
    main()
