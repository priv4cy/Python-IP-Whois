# IP WHOIS Python Module

This is a Python module for performing WHOIS lookups on IP addresses. It can be used to obtain information about the owner of an IP address, including the organization name, contact details, and more.


## Requirements

This module requires Python 3.x. There are no additional external dependencies.


## Installation

To use this module, simply copy the `ipwhois.py` file into your project directory. You can then import it in your Python script as follows:

```py
import ip_whois

ip = "196.49.192.49"
result = ip_whois.lookup(ip)
print(result)
```


## Usage

To use this module, call the `lookup` function with the IP address as the argument. The function will return the results of the WHOIS lookup as a JSON object. You can print it out or use it as needed.

```py
import ip_whois

ip_address = '192.0.2.0'
result = ip_whois.lookup(ip_address)
print(result)
```

The module will automatically perform a WHOIS lookup on the given IP address and parse the response to return a JSON object containing the information.


## License

[GNU General Public License v3.0](LICENSE)

