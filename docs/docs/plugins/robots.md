## Robots

The `robots.txt` file is a standard used by websites to communicate with web crawlers and other web robots. The file indicates which areas of the site should not be processed or scanned. These rules are set by the site administrator to ensure certain pages or directories aren't crawled and to specify a delay for crawling, among other functions.

To view the `robots.txt` file of a domain, it's straightforward. Simply use the `robots` plugin by executing the following command in your terminal:

```shell
python linkscraper -u https://example.com -a get-plugins -p robots
```
