## Page-details

The `page-details` plugin extracts all metadata from the given URL, excluding CSS, JS files, and fonts, since they necessitate additional `linkscraper` resources.

```shell
linkscraper -u https://example.com -a get-plugins -p page-details
```

With the plugin, you can gather the following metadata:

* Title
* Description
* Robots directives
* Viewport
* Charset
* WordPress
  * WordPress version
* OG metadata ([read documentation](https://ogp.me/))
