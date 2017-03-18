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
 
This application works by sending a HTTP request to a host running the server daemon.py script. This host will simply return the source IP address, of the host, in plain text.

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

There are two parts to this application, one being for your 'server' and another being for the 'client'. The server needs to sit outside your monitored network

1. Clone this repository to the client, then run the setup.py in 

```sh
$ git clone https://github.com/CameronEx/whatsmyip.git
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
Enter your API key: PLfSy1Qgt89A60z5emrDPLfSy1Qgt89A60z5emrD
Enter the root domain (not subdomain): domain.com
$
```

Once done, you'll want to configure the script to run every so often. Here's an example cronjob that can be installed on a Linux client, running the script every 60 minutes:
```
00 * * * * python /path/to/script
```

2. Copy the server scripts to the appropriate places on your server

Note: Installation of the server daemon will depend on the operating system of your server. An upstart script has been included for those running Ubuntu.

For Ubuntu, you can copy the daemon.py script to '/usr/local/bin/whatsmyip/daemon.py', ensure it is esecutable:
```$ cp daemon.py /usr/local/bin/whatsmyip/daemon.py
$ chmod +x /usr/local/bin/whatsmyip/daemon.py
```

Then install the upstart script and test it out:
```
$ cp whatsmyip.conf /etc/init/whatsmyip.conf
$ sudo start whatsmyip
```

You should be able to CURL against your server now, and have your IP address returned.


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
   