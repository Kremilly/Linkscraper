## Get Emails

By using various parameters, users can define specific actions, like collecting email addresses from the web pages. In the context of the provided command:

```shell
python linkscraper -u https://example.com -a get-emails
```

The flag is directed to scrape the website "`https://example.com`" with the specific action (`-a`) of retrieving email addresses (`get-emails`). This allows users to gather emails present on the given site, which can be useful for various purposes, including research, auditing, or data collection. As always, such a tool should be used ethically and with proper permissions to avoid any legal or ethical violations.

### Filter

The `-filter` option allows users to refine their results by including only those entries that match the filter keyword.

```shell
python linkscraper -u https://example.com -a get-emails -filter example@domain.com
```

To collect emails from the website "`https://example.com`" and then filter the results to only show those related to the email "`example@doamin.com`"
