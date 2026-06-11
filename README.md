<h1>AI with Databricks</h1>

*Explores the use of AI with Databricks.*

---

**Contents**:

- [KEY POINT: OpenAI-Compatible REST API for Model Access](#key-point-openai-compatible-rest-api-for-model-access)
- [APPROACH: Model Serving: Using External Model](#approach-model-serving-using-external-model)
- [APPROACH: Model Serving: Using Built-In Model](#approach-model-serving-using-built-in-model)
- [APPROACH: AI Gateway](#approach-ai-gateway)
- [Using AI Playground](#using-ai-playground)
- [Integrating Databricks AI Endpoint to IDE](#integrating-databricks-ai-endpoint-to-ide)

---

# KEY POINT: OpenAI-Compatible REST API for Model Access
Databricks Mosaic AI Model Serving and the Unity AI Gateway expose a unified, OpenAI-compatible REST API across all supported foundational LLMs. This standardizes the interface, allowing you to use standard openai library code to query Anthropic Claude models natively or externally hosted within your Databricks workspace.

# APPROACH: Model Serving: Using External Model
**See**: [`approach--model-serving--using-external-model.md`](./approach--model-serving--using-external-model.md)

# APPROACH: Model Serving: Using Built-In Model
**See**: [`approach--model-serving--using-built-in-model.md`](./approach--model-serving--using-built-in-model.md)

# APPROACH: AI Gateway
**See**: [`approach--ai-gateway.md`](./approach--ai-gateway.md)

# Using AI Playground
AI Playground in Databricks offers a web UI to test:

- AI gateway endpoints
- Model serving endpoints

# Integrating Databricks AI Endpoint to IDE
**See**: [`integrate-databricks-ai-endpoint-to-ide.md`](./integrate-databricks-ai-endpoint-to-ide.md)