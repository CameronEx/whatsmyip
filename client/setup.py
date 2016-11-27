#!/usr/bin/env python

""" This script will save the required information for the client to use on a continual basis """


import pickle
from pick import pick


def main():
    
    # Gather user requirements
    domain = raw_input("Enter the domain you'd like to monitor: ").strip()
    server = raw_input("Enter the FQDN (or IP address) of the host running the server application. Format should be http://host.com:port: ").strip()

    # Which DNS provider will we be using?
    providers = ['Rackspace: Cloud DNS', 'AWS: Route 53']
    provider_question = "Which DNS service will we be using?"
    provider, discard = pick(providers, provider_question)

    # Save for the client application
    with open('config.pkl', 'wb') as f:
        pickle.dump([domain, server, provider], f)


if __name__ =='__main__':
    main()
