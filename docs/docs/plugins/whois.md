## Whois

WHOIS is a query and response protocol that is used for querying databases that store an Internet resource's registered users or assignees. These resources include domain names, IP address blocks and autonomous systems, but it is also used for a wider range of other information.

The `whois` plugin allows you to extract details about a particular domain, including ownership information, unless it's set to private. To utilize this plugin, execute the command below:

```shell
python linkscraper -u https://example.com -a get-plugins -p whois
```

This plugin provides the subsequent domain-related details:

* Domain name
* Domain registrar
* WHOIS server
* Domain creation date
* Expiration date
