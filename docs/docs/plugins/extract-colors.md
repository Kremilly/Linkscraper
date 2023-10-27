## Extract-colors

To extract the colors used in the creation of the page from the URL provided by the user, you can utilize the `extract-colors` plugin. Its usage is straightforward; simply enter the following command into your terminal:

```shell
python linkscraper -u https://example.com -a get-plugins -p extract-colors
```

This plugin has a limitation: it can only recognize colors that fit into four specific patterns. See some examples below:

* `#fff`
* `#ffffff`
* `rgb(255, 255, 255)`
* `rgba(255, 255, 255, 1)`
