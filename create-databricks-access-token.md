**How-To**

<h1>Create Databricks Access Token</h1>

---

Go to your account's settings:

*Select "Settings" below*...

![](./resources/databricks-home-page-view-settings-option.png)

*You shall arrive at this page*...

![](./resources/databricks-settings.png)

Select the "Developer" tab:

> **NOTE**: *This option is only available with admin access.*

![](./resources/databricks-settings-developer.png)

Click "Manage" beside the "Access tokens" section:

![](./resources/databricks-settings-developer-access-tokens.png)

Click on "Generate new token"; you will get a pop-up like this:

![](./resources/databricks-settings-developer-access-tokens-generate-new-token.png)

Add the API scope(s) from the dropdown as appropriate.

| E.g.: Adding `model-serving` |
| --- |
| ![](./resources/databricks-settings-developer-access-tokens-generate-new-token-add-model-serving-to-api-scopes.png) |

> **NOTE**:
> 
> - We can add multiple API scopes for a single access token
> - Putting the scope as `all APIs` allows the token to access any API <br> ... *This is generally not recommended due to safety concerns*

Copy the generated key for future use.