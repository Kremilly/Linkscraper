## Headers

Fetches and displays the headers of the specified URL.

```shell
python linkscraper -u https://example.com -a get-headers
```

When you run the above command, it will fetch and display the headers of the URL `https://example.com`.

### Filter headers

Upon running the command, the tool will visit the webpage at https://example.com, scrape the links found on the page, and retrieve the headers associated with those links. The results will then be filtered to only display links that match the filter criteria specified by header.

```shell
python linkscraper -u https://example.com -a get-headers -filter header
```
