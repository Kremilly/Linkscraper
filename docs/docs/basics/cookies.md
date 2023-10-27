## Cookies

Retrieves all cookies from the site.

```shell
python linkscraper -u https://example.com -a get-cookies
```

This will return a list of all the cookies used by `https://example.com`.

### Filter

The `-filter` option allows users to refine their results by including only those entries that match the filter keyword.

```shell
python linkscraper -u https://example.com -a get-cookies -filter cookie
```

To collect cookies from the website "`https://example.com`" and then filter the results to only show those related to the term "`cookie`"
