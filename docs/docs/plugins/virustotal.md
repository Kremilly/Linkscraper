## VirusTotal

VirusTotal is a free online service that analyzes files and URLs to detect viruses, worms, trojans, and other kinds of malicious content. It uses multiple antivirus engines and website scanners to provide a comprehensive report on the potential threats associated with the uploaded content.

To scan a url using the VirusTotal tool, simply enter the following command:

```shell
python linkscraper -u https://example.com -a get-plugins -p virustotal
```

However, remember that to utilize VirusTotal services within Linkscraper, you'll need an VirusTotal API key, which can be obtained for free. [Click here](apis/virustotal.md) to learn how.
