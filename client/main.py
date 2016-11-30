#!/usr/bin/env python

"""This script will check the current public IP address of your client, compare it to an A record and update the A record if it has changed.
Designed to keep A records updated where static IP addresses are not an option, this script should be added to a cron job, to run as often as you like. """

import sys
import dns.resolver
import requests
import pickle


def resolve(target_domain):
    
    # Spawn a resolver instance
    resolver = dns.resolver.Resolver()

    # Attempt to resolve the domain
    try:
        answer = resolver.query(target_domain, "A")
        print("{} resolves to {}".format(target_domain, answer))

    except NXDOMAIN:
        sys.exit("Unable to resolve {} - Check your A record. Exiting without action".format(target_domain))

    if len(answer) != 1:
        sys.ext("Multiple A records found. That's too complex for me right now. Exiting without action.")

    return(answer)


def compare_current_ip(server, a_record, provider):

    # Make a request, to our server, for the current public IP address
    current_ip = requests.get(server).text
    print("This host's current public IP address is: {}".format(current_ip))

    # Compare it to the existing A record for the specified domain
    if current_ip == a_record:
        sys.exit("Our current IP address, {}, matches the A record for {}. Exiting without action".format(current_ip, domain))
    else:
        update_dns(current_ip, provider)


def update_dns(current_ip, provider):

    # Call the updater module, specific of the provider
    if provider == 'rax':
        print("Calling Rackspace to update the A record.")
        
        import vendor_scripts.rax.rax_update
        vendor_scripts.rax.rax_update.main(current_ip)

    else:
        sys.exit("I'm not compatible with the provider listed. Please run setup.py again.")


def main():

    # Load the variables saved by setup.py
    with open('config.pkl', 'rb') as f:
        target_domain, server, provider = pickle.load(f)

    # Obtain the current A record of the saved domain
    a_record = resolve(target_domain)

    # Compare and, if required, update the A record
    compare_current_ip(server, a_record, provider)


if __name__ == '__main__':
    main()
