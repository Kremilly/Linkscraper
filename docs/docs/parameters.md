## Parameters

### Core

| Parameter                   | Description                    | Required        | Default      |
| --------------------------- | ------------------------------ | --------------- | ------------ |
| -u, --url                   | URL to scan                    | ✅ in live mode |              |
| -a, --action                | Run an action                  | No              | ``get-core`` |
| -p, --plugin                | Load a plugin                  | No              |              |
| -oel, --only-external-links | Show only external links       | No              | `Null`     |
| -ssc, --show-status-code    | Show status code               | No              | `Null`     |
| -smf, --show-minify-files   | Show only minify files         | No              | `Null`     |
| -f, --filter                | Filter data                    | No              |              |
| -d, --download              | Download static files          | No              | `Null`     |
| -we, --write-env            | Write environments file (.env) | No              | `Null`     |
| -v, --version               | Show current version           | No              | `Null`     |

> *The parameters `-oel`, `-ssc`, `-smf`, `-we`, and `-d` cannot take values.*

### Plugins

These parameters are only useful when used with some plugin.

| Parameter           | Description                        | Required | Default                            |
| ------------------- | ---------------------------------- | -------- | ---------------------------------- |
| -b, --browser       | Set the browser to take screenshot | No       | ``firefox``                        |
| -t, --title         | Set title the screenshot on Imgur  | No       | ``Screenshot made by Linkscraper`` |
| -gf, --google-fonts | Download fonts from Google Fonts   | No       | `Null`                           |
| -up, --upload       | Upload the screenshot to Imgur    | No       | `Null`                           |
|                     |                                    |          |                                    |

> *The parameters `-up` and `-gf` cannot take values.*
