# What's My IP Address?

This Python project contains a grouping of scripts that will allow a client to monitor their external IP address and update an A record, if the monitored address differs.

This service is not dissimilar to those offered by no-ip.org, dyn, etc, however offers support for the following DNS providers;

  - Rackspace: Cloud DNS - US
  - Rackspace: Cloud DNS - UK (Coming soon)
  - Azure: Route 53 (Coming soon)

This provides the following advantage;
 - No additional costs (it's an open source application!)
 - BYO domain
 - Ability to contribute your own provider APIs
 
This application works by sending a HTTP request to a host running the server daemon.py script. This host will simple return the source IP address, of the host, in plain text.

The client then compares this IP address to the current value of the configured A record, and will update it via the configured API if the two values differ.

### Requirements

The following Python packages are required, for this application to run. All can be installed via PIP.

#### Client
* [Requests] - Python HTTP library
* [DNS.Resolver] - Python DNS library, ofter installed by default
* [Pickle] - Data (un)serliaser
* [Pick] - Simple CLI menus
* [JSON] - JSON encoder/decoder

#### Server
* [Flask] - Python web framework
* [JSON] - JSON encoder/decoder

### Installation

There are two parts to this application, one being for your 'server' and another being for the client.

Clone this repository to the client, then run the setup.py in 

```sh
$ git clone https://gitlab.com/camerone/whatsmyip
$ cd whatsmyip/client
$ python setup.py
```

This script will lead down differnt paths, depending on your current DNS provider. Here's an example for Rackspace

```sh
$ python setup.py
Enter the domain youd like to monitor: home.domain.com
Enter the FQDN (or IP address) of the host running the server application. Format should be http://host.com:port: http://domain.com:8081
Enter your Rackspace Cloud account number: 12345
Enter your Rackspace Cloud username: cloud_user
Enter your API key: 43km3423431fe5gv43ed234vfb54pg11
Enter the root domain (not subdomain): domain.com
$
```

### Todos

 - Add Rackspace: Cloud DNS - UK support
 - Add AWS: Route 53 support
 - IPv6 Support
 - Complete this documentation


License
----

MIT

   [Requests]: <http://docs.python-requests.org/en/master/>
   [DNS.Resolver]: <http://www.dnspython.org/>
   [Pickle]: <https://docs.python.org/2/library/pickle.html>
   [Pick]: <https://pypi.python.org/pypi/pick>
   [JSON]: <https://docs.python.org/2/library/json.html>
   [Flask]: <http://flask.pocoo.org/>
   