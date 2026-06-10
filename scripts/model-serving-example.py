from openai import OpenAI

client = OpenAI(
    api_key="<your-api-key>", # Your Databricks API access token scoped to `model-serving`
    base_url="https://<your-workspace-id>.cloud.databricks.com/serving-endpoints"
)

response = client.chat.completions.create(
    model="<your-model-name>", # Your given name of the model serving endpoint)
    messages=[
        {"role": "user", "content": "What is depression?"}
    ]
)
print(response.choices[0].message.content)