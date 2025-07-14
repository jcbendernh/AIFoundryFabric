# AIFoundryFabric

This repository provides sample Python scripts for working with Microsoft Fabric and Azure AI Foundry Agents. The scripts demonstrate how to create, configure, and interact with AI agents that leverage live data connections through Microsoft Fabric.

## Contents

- `src/create_fabric_agent.py`: Example script to create an AI agent using the Microsoft Fabric grounding tool. The agent is configured to access live revenue data and respond to queries about revenue, customers, products, and countries. The script shows how to set up the agent, provide instructions, and manage the agent lifecycle using the Azure AI Projects SDK.

- `src/test_fabric_agent.py`: Interactive test script to communicate with an existing agent created in Azure AI Foundry. The script allows you to ask questions about revenue per country and receive responses from the agent. It demonstrates how to retrieve agent details, create a conversation thread, send user questions, and display agent responses in a conversational loop.

## Prerequisites

- Python 3.8+ installed on your system
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest) installed on your system.
- An Azure AI Foundry Project created.  <BR>For more information check out [Create a project for Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry&pivots=fdp-project).
- A Microsoft Fabric Connected Resource created in the AI Foundry Project.  <BR>For more information check out [Use the Microsoft Fabric data agent | Setup](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/fabric?pivots=portal#setup)
- Install required packages:
  ```sh
  pip install azure-identity
  pip install --pre azure-ai-projects
  ```

## Usage

### 1. Create an Agent

Edit [`create_fabric_agent.py`](src/create_fabric_agent.py) to set your environment variables or replace the placeholder values for:
- `PROJECT_ENDPOINT`
- `MODEL_DEPLOYMENT_NAME`
- `FABRIC_CONNECTION_ID`

Run the script:
```sh
python src/create_fabric_agent.py
```
This will create a new agent with access to your Fabric data connection.

**Important:** After creating the agent, you must manually add the following resources in the Azure AI Foundry portal:
- **Fabric Connected Resource** under Knowledge
- **Code Interpreter** tool under Actions

Navigate to your agent in the Azure AI Foundry portal and add these resources before proceeding to test the agent.

### 2. Test the Agent

Edit [`test_fabric_agent.py`](src/test_fabric_agent.py) and set the `AGENT_ID` variable to the ID of the agent created in the previous step.

Run the script:
```sh
python src/test_fabric_agent.py
```
You can now interact with the agent in a conversational loop. Type your questions and receive responses from the agent. Type `exit` or `quit` to end the session.

NOTE: Because we added the Code Interpreter, you can visualize the data in graphs when using the **Agents playground** in the AI Foundry Portal.  Try the following phrase "Show me this as a bar graph" after you have asked a data query like "What is the revenue per country?"

## License

This project is licensed under the MIT License.