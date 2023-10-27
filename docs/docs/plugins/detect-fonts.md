## Detect-fonts

To detect fonts in the provided URL, you need to use the `detect-fonts` plugin. To utilize this plugin, simply enter the following command into your terminal:

```shell
python linkscraper -u https://example.com -a get-plugins -p detect-fonts
```

### Google Fonts

To collect variations of a specific font, simply use the `-gf` flag, type the font name, and press Enter. Doing this, Linkscraper will list all font files indexed by Google Fonts.

```shell
python linkscraper -u https://example.com -a get-plugins -p detect-fonts -gf
```

However, remember that to utilize Google Fonts services within Linkscraper, you'll need an Google Fonts API key, which can be obtained for free. [Click here](apis/google-fonts.md) to learn how.

### Download

To download all variants of the font, you just need to add the `-d` flag.

```shell
python linkscraper -u https://example.com -a get-plugins -p detect-fonts -gf -d
```
