#!/usr/bin/env python

""" This script will save the required information for the client to use on a continual basis """


import pickle
import sys
from pick import pick


def main():
    
    # Gather user requirements
    target_domain = raw_input("Enter the domain you'd like to monitor: ").strip()
    server = raw_input("Enter the FQDN (or IP address) of the host running the server application. Format should be http://host.com:port: ").strip()

    # Which DNS provider will we be using?
    providers = ['Rackspace: Cloud DNS - US', 'AWS: Route 53']
    provider_question = "Which DNS service will we be using?"
    discard, provideer_index = pick(providers, provider_question)

    if provider_index == 0 or :
        import vendor_scripts.rax.setup

        provider = 'rax'
        username = raw_input("Enter your Rackspace Cloud username: ").strip()
        api_key = raw_input("Enter your API key: ").strip()

        vendor_scripts.rax.setup.main(username, api_key, account_num, target_domain)

    else:
        sys.exit("Only RAX US is supported right now, other options coming soon...")

    # Save for the client application
    with open('config.pkl', 'wb') as f:
        pickle.dump([target_domain, server, provider], f)


if __name__ =='__main__':
    main()
