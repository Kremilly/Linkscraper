## Get Links

The `-get-links` command is designed to extract all links from a user-specified URL. Along with its primary function, it supports three additional sub-commands that we will detail below.

The command allows for tailored actions through different parameters. A common use case is to harvest links from web pages, as demonstrated:

```shell
python linkscraper -u https://example.com -a get-links
```

### Filter

The `-filter` option allows users to refine their results by including only those entries that match the filter keyword.

```shell
python linkscraper -u https://example.com -a get-links -filter domain.com
```

### Only external links

The `-oel` option allows users to refine their results by including only those entries that match the links outside from `-u`.

```shell
python linkscraper -u https://example.com -a get-emails -oel
```

### Show status code

The `-ssc` option show the status code of all links listed

```shell
python linkscraper -u https://example.com -a get-emails -ssc
```
