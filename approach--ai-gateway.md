<h1>APPROACH: AI Gateway</h1>

> **NOTE**:
> 
> - If using Databricks-hosted models: <br> *Consumes Databricks credits*
> - If using external provider models: <br> *Consumes external provider credits*

---

**Contents**:

- [View AI Gateway Tab](#view-ai-gateway-tab)
- [Create AI Gateway Endpoint (*if required*)](#create-ai-gateway-endpoint-if-required)
- [Create Databricks Access Token](#create-databricks-access-token)
- [Testing the Endpoint via cURL](#testing-the-endpoint-via-curl)
- [Testing the Endpoint via Python](#testing-the-endpoint-via-python)

---

# View AI Gateway Tab
- Login to your Databricks account and go to your workspace
- Go to the "AI Gateway" tab under "AI/ML" in the sidebar

![](./resources/databricks-ai-gateway.png)

Here is an example of an existing AI gateway endpoint:

![](./resources/databricks-ai-gateway-databricks-claude-opus-4-8.png)

# Create AI Gateway Endpoint (*if required*)
Select "+ AI Gateway Endpoint" below:

![](./resources/databricks-ai-gateway.png)

Here is how the creation page looks like (showing Databricks-hosted models):

![](./resources/databricks-ai-gateway-create-ai-gateway-endpoint-using-databricks-hosted.png)

Here is how the creation page looks like (showing external provider models):

![](./resources/databricks-ai-gateway-create-ai-gateway-endpoint-use-external-provider.png)

> **NOTE**: *Notice that you can select your own external-provider-using serving endpoint here. In this case, 2 model serving endpoints created by me (`open-ai-endpoint` and `test`) are also visible in the options.*

# Create Databricks Access Token
**See**: [`create-databricks-access-token.md`](./create-databricks-access-token.md)

For this case, add `ai-gateway` to the API scope(s).

Copy the generated key for future use.

# Testing the Endpoint via cURL
[`scripts/ai-gateway-example.curl`](./scripts/ai-gateway-example.curl)

# Testing the Endpoint via Python
[`scripts/ai-gateway-example.py`](./scripts/ai-gateway-example.py)
