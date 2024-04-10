## Imgur API Integration

To integrate with Imgur's API, follow this guide:

1. **Sign Up for an Account**: If you're not an Imgur user, [register here](https://imgur.com/).
2. **Application Registration**: Go to [Imgur&#39;s developer portal](https://api.imgur.com/oauth2/addclient) and register your app. This grants API access and provides your Client ID and Secret.
3. **Form Details**:
   1. **Application Name**: Assign a distinctive name to your app.
   2. **Authorization Type**: Select your preferred authorization flow. Typically, "OAuth 2 without a callback URL" suffices.
   3. **Contact & Overview**: Provide your email and a concise app description.
4. **Finalize Registration**: Submit the form.
5. **Secure Your Credentials**: Post-registration, you'll receive a `Client ID` and `Client Secret`. Store these securely, as they're essential for API interactions.
6. **API Calls**: With your `Client ID`, you're set to interact with the Imgur API. Always respect Imgur's API practices and terms.

***Reminder**: The free-tier has rate limits. For extensive API usage, consider premium plans or optimize your app to stay within free limits. Always refer to Imgur's official documentation for current details.*

> *Visit the [Environments](../../settings/env.md) page to learn how to save the key in your .env file so that Linkscraper starts using your key.*
