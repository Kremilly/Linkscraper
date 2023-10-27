## JavaScript

The `-get-js-files` command is designed to extract and list all JavaScript (JS) files from a user-specified URL. This is particularly useful for web developers, designers, and security professionals who wish to review or analyze the style assets of a website.

To fetch all JS files from the website `https://example.com`, you can execute the following command:

```shell
python linkscraper -u https://example.com -a get-js-files
```

### Filter

The `-filter` option allows users to refine their results by including only those entries that match the filter keyword.

```shell
python linkscraper -u https://example.com -a get-js-files -filter example.css
```

### Show minify files

The `-smf` option filters the listed files to display only minified ones identified as `.min.css`.

```shell
python linkscraper -u https://example.com -a get-js-files -smf
```

### Download

You can also download all the listed files easily; simply use the `-d` flag.

```shell
python linkscraper -u https://example.com -a get-js-files -d
```
