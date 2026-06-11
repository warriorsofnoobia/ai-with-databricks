<h1>Integrate Databricks AI Endpoint to IDE</h1>

---

**Contents**:

- [Goal](#goal)
- [Context](#context)
  - [About Continue](#about-continue)
  - [About VS Code](#about-vs-code)
  - [VS Code Extension for Continue](#vs-code-extension-for-continue)
- [Setup](#setup)
  - [Install VS Code](#install-vs-code)
  - [Install the Continue Extension for VS Code](#install-the-continue-extension-for-vs-code)
  - [Setup Endpoint](#setup-endpoint)

---

# Goal
The goal is as follows:

- Use the chat interface available through an IDE
- Access and communicate with one of the following:
    - Databricks Model Serving Endpoint
    - AI Gateway Endpoint
- ***Use Databricks credits to use AI models***
- Circumvent provider-specific accounts and interfaces

# Context
## About Continue
Continue (also called Continue.dev) is an open-source AI coding agent available as a CLI, VS Code extension, and JetBrains plugin. It is licensed under Apache 2.0, and provides chat, autocomplete, and agentic coding features within an IDE. It is provider-agnostic; rather than being tied to a single model or service, it supports a wide range of LLM providers through a unified configuration interface, including any OpenAI-compatible endpoint.

> **References**:
> 
> - [`continuedev`/`continue`, **github.com**](https://github.com/continuedev/continue); see:
>   - Repository's README
>   - The provider list in `core/llm/llms/index.ts`
> - [**www.continue.dev**](https://www.continue.dev/)

## About VS Code
VS Code (Visual Studio Code) is a free, open-source code editor developed by Microsoft, first released in 2015. It runs on Windows, macOS, and Linux, and has become one of the most widely used editors due to its extensibility, built-in Git support, and large ecosystem. At its heart, Visual Studio Code features a lightning fast source code editor, but you can install any number of third-party extensions to add further functionality to the core VS Code IDE.

> **Reference**: [*Why did we build Visual Studio Code?*, **code.visualstudio.com/docs/editor**](https://code.visualstudio.com/docs/editor/whyvscode)

## VS Code Extension for Continue
The VS Code extension packages Continue's functionality as a standard VS Code extension, installable from the VS Code Marketplace. Once installed, it adds a dedicated chat side panel to the VS Code UI, inline code editing commands, and autocomplete suggestions within the editor itself. The extension reads from `~/.continue/config.yaml` (`~` here refers to the home directory in Ubuntu; for Windows, this path may differ) to determine which models and providers to use, meaning the IDE integration is entirely configuration-driven, with no code changes required. The extension's Marketplace listing is at [`marketplace.visualstudio.com/items?itemName=Continue.continue`](https://marketplace.visualstudio.com/items?itemName=Continue.continue), and its source is in the `extensions/vscode` directory of the Continue.dev monorepo (see: [`continuedev`/`continue`, **github.com**](https://github.com/continuedev/continue)).

> **Reference**: [`continuedev`/`continue`/`extensions`/`vscode`, **github.com**](https://github.com/continuedev/continue/tree/main/extensions/vscode)

# Setup
## Install VS Code
**See**: [**code.visualstudio.com/download**](https://code.visualstudio.com/download)

## Install the Continue Extension for VS Code
You can do this within VS Code, using the extensions tab in the sidebar:

![](./resources/installed-continue-extension-for-vscode.png)

## Setup Endpoint