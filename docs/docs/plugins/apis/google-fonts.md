## Google Fonts Integration

**Obtaining an API Key for Google Fonts Developer API:**

1. **Google Cloud Console**:

   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - If you haven’t already, sign in with your Google account.
   - Create a new project or select an existing one.
2. **Enable the API**:

   - In the navigation menu, select "APIs & Services" > "Library".
   - In the search bar, type "Google Fonts Developer API".
   - Click on the Google Fonts Developer API from the search results.
   - Click on the "Enable" button.
3. **Create Credentials**:

   - After enabling the API, you’ll be directed to the API page. If not, go back to the dashboard of your project.
   - Click on "APIs & Services" > "Credentials".
   - Click the "Create Credentials" dropdown button and select "API key".
   - Your new API key will be displayed. Copy this key for your use.
4. **(Optional) Restrict the API Key**:

   - For added security, you might want to restrict the API key so that it can only be used by certain IPs, apps, or other specific conditions.
   - On the "Credentials" page, click on the API key you've just created.
   - Under "Key restriction", choose the option that suits your needs, and follow the on-screen instructions to set the restrictions.
5. **Usage**:

   - With the API key in hand, you can use it to make calls to the Google Fonts Developer API following the official documentation.

> *Visit the [Environments](../../env.md) page to learn how to save the key in your .env file so that Linkscraper starts using your key.*
