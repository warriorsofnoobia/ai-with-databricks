<h1>APPROACH: Model Serving: Using External Model</h1>

> **NOTE**: *This consumes credits from the model provider and not Databricks credits. The model serving endpoint acts merely as a middleman to route API requests and responses.*

---

**Contents**:

- [Context](#context)
- [Create External Model Provider API Key](#create-external-model-provider-api-key)
- [Create Model Serving Endpoint](#create-model-serving-endpoint)
- [Create Databricks Access Token](#create-databricks-access-token)
- [Testing the Endpoint via Python](#testing-the-endpoint-via-python)

---

# Context
In this example:

- External model provider: OpenAI
- Model used: `gpt-5-mini`

> *While this example is for OpenAI, the same broad approach applies for any external model.*

# Create External Model Provider API Key
For OpenAI, go to the following:

[**platform.openai.com/api-keys**](https://platform.openai.com/api-keys)

![](./resources/platform.openai.com/api-keys.png)

> **NOTE**: *To access the above page for your purposes, you may have to create an OpenAI organisation account, but although it is called "organisation account", it can be used for personal use with no added steps. In my case, I have named my organisation "Personal", indicating that it is for personal use.*

Create either a personal API key or a service account.

***Ensure you copy the API key secret for future use.***

# Create Model Serving Endpoint
- Login to your Databricks account and go to your workspace
- Go to the "Serving" tab under "AI/ML" in the sidebar

![](./resources/databricks-create-model-serving-endpoint.png)

For this example, we will select a model from the "External model providers" section in the dropdown we get when we go into the "Entity" entry box, select the "Foundational models" option and go through the options within this. This is how the pop-up box looks like:

![](./resources/databricks-create-model-serving-endpoint-select-served-entity.png)

The result is as follows (after naming the model endpoint to `test-openai-endpoint`):

![](./resources/databricks-create-model-serving-endpoint-openai-selected-1.png)

> *Notice that "Entity" has been renamed to "Provider" here.*

After choosing the "OpenAI API type" as "OpenAI":

![](./resources/databricks-create-model-serving-endpoint-openai-selected-2.png)

In the "OpenAI API key secret" entry, add the API key secret generated and copied in the previous section. This is what Databricks will use to authorise its requests to the external model. Finally, specify the "Task type" (in this example, "Chat" is chosen) and "Provider model" to be used (in this example, `gpt-5-mini` is given):

![](./resources/databricks-create-model-serving-endpoint-openai-selected-3.png)

Hit "Create".

# Create Databricks Access Token
**See**: [`create-databricks-access-token.md`](./create-databricks-access-token.md)

For this case, add `model-serving` to the API scope(s).

Copy the generated key for future use.

# Testing the Endpoint via Python
**See**: [`scripts/model-serving-example.py`](./scripts/model-serving-example.py)

The Databricks access token has to be provided here for authorisation. The Databricks access token allows authorisation for model serving endpoint access, while the provider's API key secret given within the endpoint's configuration allows authorisation for the external model itself. The routing is as follows:

```
user --(request)-->
    --(databricks access token)--> model serving endpoint
        --(provider api key secret)--> external model
            --(response)--> model serving endpoint
                --(response)--> user
```

> **Reference**: [*Tutorial: Create external model endpoints to query OpenAI models*, **docs.databricks.com/gcp/en/generative-ai/tutorials**](https://docs.databricks.com/gcp/en/generative-ai/tutorials/external-models-tutorial)

---

> **NOTE**: *There is a cURL equivalent for this.*
