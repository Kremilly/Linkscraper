<div align="center">
    <img src="https://i.imgur.com/m12BVHm.png" align="center" />
    <br><br>
    A powerful tool to scrape and manage links from web pages.
</div><br>

**Table of Contents:**

* [Introduction](https://github.com/kremilly/linkscraper/#-introduction)
* [Requirements](https://github.com/kremilly/linkscraper/#-requirements)
* [Getting started](https://github.com/kremilly/linkscraper/#-getting-started)
* [Parameters](https://github.com/kremilly/linkscraper/#-parameters)
* [Usage](https://github.com/kremilly/linkscraper/#-usage)
* [Plugins](https://github.com/kremilly/linkscraper/#-requirements)
* [Additional links](https://github.com/kremilly/linkscraper/#-additional-links)
* [Changelog](https://github.com/kremilly/linkscraper/#-changelog)
* [External api&#39;s use](https://github.com/kremilly/linkscraper/#-external-apis-use)
* [Dependencies](https://github.com/kremilly/linkscraper/#-dependencies)
* [Roadmap](https://github.com/kremilly/linkscraper/#-roadmap)
* [License](https://github.com/kremilly/linkscraper/#-license)
* [Sponsor](https://github.com/kremilly/linkscraper/#-sponsor)

## 🌐 Introduction

Dive deep into the web's intricate layers with Linkscraper! Whether you're a researcher, developer, or a curious explorer, our tool efficiently scans web pages to fetch links, images, emails, and much more. Powered by an array of versatile plugins and a user-friendly interface, Linkscraper streamlines the process of extracting and managing web data. From headers to JavaScript files, and from cookies to CSS – uncover the digital signatures of the web with ease. Join us on this journey and uncover the treasures hidden in plain sight on the web.

## 📌 Requirements:

* Python >= 3.6 ([Download](https://www.python.org/downloads/))

## 🚀 Getting Started

Clone this repository.

```shell
git clone https://github.com/kremilly/linkscraper.git
```

To install dependencies.

```python
pip install -r requirements.txt
```

## 📖 Parameters

| Parameter                   | Description                        | Required                | Default                            |
| --------------------------- | ---------------------------------- | ----------------------- | ---------------------------------- |
| -u, --url                   | URL to scan                        | ✅                      |                                    |
| -a, --action                | Run an action                      | No                      | ``get-core``                       |
| -p, --plugin                | Load a plugin                      | No                      |                                    |
| -k, --key                   | Set the API key                    | Yes, if plugin is needs |                                    |
| -f, --file                  | Save output file                   | Yes, if plugin is needs |                                    |
| -b, --browser               | Set the browser to take screenshot | No                      | ``chrome``                         |
| -t, --title                 | Set title the screenshot on Imgur  | No                      | ``Screenshot made by Linkscraper`` |
| -up, --upload               | Upload the screenshot to Imgur    | No                      |                                    |
| -oel, --only-external-links | Show only external links           | No                      | `false`                          |
| -ssc, --show-status-code    | Show status code                   | No                      | `false`                          |
| -smf, --show-minify-files   | Show only minify files             | No                      | `false`                          |
| -filter, --filter           | Filter data                        | No                      |                                    |
| -d, --download              | Download static files              | No                      | `false`                          |
| -version, --version         | Show current version               | No                      |                                    |

## 🛠 Usage

Here are some examples of how to use Linkscraper:

*Get core:*

```shell
python linkscraper -u https://example.com -a get-core
```

*Get headers:*

```shell
python linkscraper -u https://example.com -a get-headers
```

* *Get headers and filter header:*

  ```shell
  python linkscraper -u https://example.com -a get-headers -filter header
  ```

*Get cookies:*

```shell
python linkscraper -u https://example.com -a get-cookies
```

* *Get cookies and filter cookie:*

  ```shell
  python linkscraper -u https://example.com -a get-cookies -filter cookie
  ```

*Get js files:*

```shell
python linkscraper -u https://example.com -a get-js-files
```

* *Get js files and filter files:*

  ```shell
  python linkscraper -u https://example.com -a get-js-files -filter example.js
  ```
* *Get js files and show only minify files:*

  ```shell
  python linkscraper -u https://example.com -a get-js-files -smf true
  ```
* *Get js files and download files:*

  ```shell
  python linkscraper -u https://example.com -a get-js-files -d true
  ```

*Get css files:*

```shell
python linkscraper -u https://example.com -a get-css-files
```

* *Get css files and filter files:*

  ```shell
  python linkscraper -u https://example.com -a get-css-files -filter example.css
  ```
* *Get css files and show only minify files (new):*

  ```shell
  python linkscraper -u https://example.com -a get-css-files -smf true
  ```
* *Get css files and download files:*

  ```shell
  python linkscraper -u https://example.com -a get-css-files -d true
  ```

*Get images files:*

```shell
python linkscraper -u https://example.com -a get-images-files
```

* *Get images files and filter files:*

  ```shell
  python linkscraper -u https://example.com -a get-images-files -filter example.png
  ```
* *Get images files and download files:*

  ```shell
  python linkscraper -u https://example.com -a get-images-files -d true
  ```

*Get links:*

```shell
python linkscraper -u https://example.com -a get-links
```

* *Get links and filter url:*

  ```shell
  python linkscraper -u https://example.com -a get-links -filter domain.com
  ```
* *Get links and show only external links:*

  ```shell
  python linkscraper -u https://example.com -a get-links -oel true
  ```
* *Get links and show status code:*

  ```shell
  python linkscraper -u https://example.com -a get-links -ssc true
  ```

*Get emails:*

```shell
python linkscraper -u https://example.com -a get-emails
```

* *Get emails and filter email:*

  ```shell
  python linkscraper -u https://example.com -a get-css-files -filter example@domain.com
  ```

## 🧩 Plugins

*wp-detect:*

```shell
python linkscraper -u https://example.com -a get-plugins -p wp-detect
```

*whois:*

```shell
python linkscraper -u https://example.com -a get-plugins -p whois
```

*page-details:*

```shell
linkscraper -u https://example.com -a get-plugins -p page-details
```

*robots:*

```shell
python linkscraper -u https://example.com -a get-plugins -p robots
```

*virustotal:*

```shell
python linkscraper -u https://example.com -a get-plugins -p virustotal -k YOUR_VIRUSTOTAL_KEY
```

* *virustotal and get key in ENV variable:*

  ```shell
  python linkscraper -u https://example.com -a get-plugins -p virustotal -k env:VIRUSTOTAL_KEY
  ```

*ip-location:*

```shell
python linkscraper -u https://example.com -a get-plugins -p ip-location
```

*detect-fonts (new):*

```shell
python linkscraper -u https://example.com -a get-plugins -p detect-fonts
```

*extract-colors (new):*

```shell
python linkscraper -u https://example.com -a get-plugins -p detect-fonts
```

screenshot:

```shell
python linkscraper -u https://example.com -a get-plugins -p screenshot -f screenshot.png -b chrome
```

* *screenshot and upload to Imgur:*

  ```shell
  python linkscraper -u https://example.com -a get-plugins -p screenshot -f screenshot.png -b chrome -up imgur -k YOUR_IMGUR_CLIENT_ID -t "Title of post here"
  ```
* *screenshot and upload to Imgur and get key in ENV variable:*

  ```shell
  python linkscraper -u https://example.com -a get-plugins -p screenshot -f screenshot.png -b chrome -up imgur -k env:IMGUR_CLIENT_ID -t "Title of post here"
  ```

## 🔗 Additional links

* [Get your free VirusTotal Key](https://www.virustotal.com/gui/my-apikey)
* [Get your free Imgur Client ID](https://api.imgur.com/oauth2/addclient)

## 📜 Changelog

> Current version: ``2.2.0``

Minors

* Refactoring code, rename functions and variables for snake_case pattern
* Refactoring struct folders

Fixes

* Fixed the GitHub Gist URLs

Added

* Function ``get_links`` was added
* Function ``get_emails`` was added
* Function `download_css` wass added
* Function `download_js` wass added
* Function `download_images` wass added

Improvements

* Improvement in interface
* Improvement in plugin ``wp_detect``
* Improvement in plugin ``detect_fonts``

Plugins removed

* Plugin ``mshots`` was removed and replacement by ``screenshot``
* Plugin ``page_title`` was removed and replacement by ``page_details``

Plugins added

* Plugin ``whois`` was added
* Plugin ``imgur`` was added
* Plugin ``robots`` was added
* Plugin ``virustotal`` was added
* Plugin ``screenshot`` was added
* Plugin ``ip_location`` was added
* Plugin ``page_details`` was added
* Plugin ``detect_fonts`` was added
* Plugin ``extract_colors`` was added

## 📡 External API's use

* [Imgur](https://imgur.com)
* [VirusTotal](https://virustotal.com)
* [IP-API](https://ip-api.com/)
* [who.is](https://who.is/)

## 📦 Dependencies

* beautifulsoup4
* cloudscraper
* pyfiglet
* pyperclip
* requests
* selenium
* whois
* rich
* python-decouple

## 🗺 Roadmap

* [ ] Implement a micro database key-value type ([TinyDB](https://tinydb.readthedocs.io/en/latest/) like)
* [ ] List of possible pdf's files on current page
* [ ] Download public PDF files listed on current page

## 📝 License

Code licensed under [MIT License](https://github.com/kremilly/linkscraper/blob/main/LICENSE)

## 💡 Sponsor

Hello passionate Linkscraper user!

Building and maintaining a tool like Linkscraper demands time, dedication, and resources. If you've found value in using Linkscraper, please consider supporting its future development. Your financial contribution, no matter how small, will not only help keep Linkscraper up-to-date and robust, but also fuel the addition of new exciting features tailored for your needs.

By contributing, you're not just supporting a tool – you're championing a vision of making web data extraction accessible and efficient for everyone. Together, we can ensure that Linkscraper continues to grow and serve the digital community.

[Click here](https://github.com/sponsors/kremilly) to support Linkscraper. Every bit counts, and we truly appreciate your generosity. 🚀❤️

Thank you for being an integral part of our journey!
