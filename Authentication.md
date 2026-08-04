# Shopify Customer Authentication Setup Log

This file logs the current status of the customer login/sign-up integration and lists the next steps required to complete the setup.

---

## 1. Authentication System Status

*   **System Type**: New Customer Accounts (Shopify-hosted, passwordless secure login).
*   **Sign-in Link Status**: Enabled in the online store header and checkout.
*   **Customization Mode**: Visual design configured via the unified **Checkout and Customer Accounts Editor**.
*   **Branding Configuration**:
    *   **Page Type**: Customer Accounts `Sign-in` preview.
    *   **Customizations Needed**: Logo upload under Header settings; color variables (e.g., deep teal `#013F3E` and gold accent) configured inside the editor's Settings tab (Gear icon).

---

## 2. Setting Up "Sign in with Google"

To complete the Google authentication link, you must create a web client in your Google Cloud Console.

### A. Google Cloud Credentials
*   **Console Link**: [Google Cloud Credentials Console](https://console.cloud.google.com/apis/credentials)
*   **Project Name**: Recommended to name it `Swastik Jewels Accounts` or select your existing active project.

### B. Configuration Details for Google Console
When creating the **OAuth Client ID** for a **Web Application**, copy-paste these exact values:

#### 1. Authorized JavaScript Origins
```text
https://shopify.com
https://sitpg1-i1.account.myshopify.com
```

#### 2. Authorized Redirect URIs
```text
https://shopify.com/authentication/98923479358/social/google/callback
https://sitpg1-i1.account.myshopify.com/authentication/social/google/callback
```

#### 3. Deauthorize Callback URIs
```text
https://shopify.com/authentication/98923479358/social/google/revoke
https://sitpg1-i1.account.myshopify.com/authentication/social/google/revoke
```

---

## 3. Checklist to Continue Later

*   [ ] Complete the Google Cloud Console credential generation.
*   [ ] Copy the resulting **Client ID** and **Client Secret** from Google Cloud Console.
*   [ ] Return to **Shopify Admin** > **Settings** > **Customer accounts** > **Authentication** > **Google (Connect)**.
*   [ ] Paste the **Client ID** and **Client Secret** and save the configuration.
*   [ ] Verify the "Sign in with Google" button appears on your custom store login page (`https://shopify.com/98923479358/account` / `/account`).
