## Resend Integration

[resend.com](https://resend.com) Integration for Frappe

![Resend Integration Workspace Screenshot](https://github.com/NagariaHussain/resend_integration/assets/34810212/7b866b2f-2a92-4cc0-ad8a-f6a035a3e7d2)

## Installation

Follow [this](https://frappeframework.com/docs/v14/user/en/installation) documentation to setup bench and then you can install this app by running the commands below:

```sh
bench get-app NagariaHussain/resend_integration
bench --site <site-name> install-app resend_integration
```

### Setup

Head over to your [Resend](https://resend.com) dashboard and generate an API key, and paste it in **Resend Settings**:

![Resend Settings Screenshot](https://github.com/NagariaHussain/resend_integration/assets/34810212/327a0001-890e-48b5-8cfc-0045f2ca3a38)

#### Webhook Setup

Add webhook with URL:

```
https://<your-site-domain>/api/method/resend_integration.api.handle_resend_webhook
```

Copy the signing secret from your webhook dashboard on Resend:

![Resend Signing Secret](https://github.com/frappe/changemakers/assets/34810212/7e797c6e-442b-4845-a4c0-0fa6789dfa78)

and paste it in **Resend Settings** in your Frappe instance.

### Sending Broadcast Emails

Use the **Resend Broadcast Email** DocType.

### API

You can send emails from your custom app or server scripts too:

```python
from resend_integration.api import send_resend_emails

send_resend_emails(
 "Get discount!",
 from_email="notifications@buildwithhussain.dev",
 to_emails=["faris@frappe.io"],
 email_html="<h1>Hey!</h1>",
 reply_to="hussain@frappe.io",
)
```

> Note: You will need to verify your domain before you can use it to send emails. For example, in the above example, "buildwithhussain.dev" has been already verified from Resend dashboard.

#### License

AGPL 3.0
