## Screenshot

With the `screenshot` plugin, you can capture screenshots of a URL using the Selenium library. To utilize this plugin, enter the following command in your terminal:

```shell
python linkscraper -u https://example.com -a get-plugins -p screenshot -b firefox
```

*The `-b` flag specifies which browser you'll use for the screenshot capture (ensure the software is installed on your machine). You have two browser options: Google Chrome and Mozilla Firefox. However, th*

*# Ignore the path site/ere's a crucial caveat when using Google Chrome with this feature, as noted below.*

> *Versions starting from 114 of the Google Chrome browser are incompatible with this feature; we suggest using the Mozilla Firefox browser.*

### Upload to Imgur

To upload the screenshot to Imgur, simply use the `-up` flag. However, remember that to utilize Imgur services within Linkscraper, you'll need an Imgur API key, which can be obtained for free. [Click here](apis/imgur.md) to learn how.

```shell
python linkscraper -u https://example.com -a get-plugins -p screenshot -b firefox -up -t "Title of post here"
```

*The `-t` flag sets the title for the post. By default, its value is '`Screenshot made by Linkscraper`'.*
