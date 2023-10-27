## Images

The `-get-images-files` command is designed to extract and list all JavaScript (JS) files from a user-specified URL. This is particularly useful for web developers, designers, and security professionals who wish to review or analyze the style assets of a website.

To fetch all JS files from the website `https://example.com`, you can execute the following command:

```shell
python linkscraper -u https://example.com -a get-images-files
```

### Filter

The `-filter` option allows users to refine their results by including only those entries that match the filter keyword.

```shell
python linkscraper -u https://example.com -a get-images-files -filter example.png
```

### Download

You can also download all the listed files easily; simply use the `-d` flag.

```shell
python linkscraper -u https://example.com -a get-images-files -d
```

### Formats of images

Linkscraper is compatible with the main image formats used on the modern internet and also supports some formats that aren't widely used today, aiming to enhance the command's compatibility and to ensure no image format is left out.

* PNG
* SVG
* TIFF
* WebP
* AVIF
* JPEG
* JPEG XR
* JPEG 2000
