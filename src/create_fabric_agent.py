# pylint: disable=line-too-long,useless-suppression
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

"""
FILE: sample_agents_fabric.py

DESCRIPTION:
    This sample demonstrates how to use Agent operations with the Microsoft Fabric grounding tool from
    the Azure Agents service using a synchronous client.

USAGE:
    python sample_agents_fabric.py

    Before running the sample:

    pip install azure-identity
    pip install --pre azure-ai-projects

    Set this environment variables with your own values:
    1) PROJECT_ENDPOINT - The Azure AI Project endpoint, as found in the Overview
                          page of your Azure AI Foundry portal.
    2) MODEL_DEPLOYMENT_NAME - The deployment name of the AI model, as found under the "Name" column in
       the "Models + endpoints" tab in your Azure AI Foundry project.
    3) FABRIC_CONNECTION_ID  - The ID of the Fabric connection, in the format of:
       /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace-name}/connections/{connection-name}
"""

import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder

# Set PROJECT_ENDPOINT with fallback to environment variable
PROJECT_ENDPOINT = "<PROJECT_ENDPOINT>" 

# Set FABRIC_CONNECTION_ID with fallback to environment variable
FABRIC_CONNECTION_ID = "<FABRIC_CONNECTION_ID>"

# Set MODEL_DEPLOYMENT_NAME with fallback to environment variable
MODEL_DEPLOYMENT_NAME ="<MODEL_DEPLOYMENT_NAME>"   

project_client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

# [START create_agent_with_fabric_tool]
conn_id = FABRIC_CONNECTION_ID

print(f"Using Fabric connection: {conn_id}")

# Create an Agent with the Fabric connection as a knowledge source
with project_client:
    agents_client = project_client.agents

    agent = agents_client.create_agent(
        model=MODEL_DEPLOYMENT_NAME,
        name="Fabric Data Agent",
        instructions="""You are a confident, persuasive, and insightful AI sales assistant with access to live revenue data through the Revenue-Agent Fabric connection.
FIELD MAPPINGS:
- When users ask about "Revenue", this refers to the LineTotal field
- When users ask about "Customer", this refers to the CustomerName field
- When users ask about "Product", this refers to the ProductName field
- Revenue by country data is available via CountryRegion and LineTotal fields""",
        metadata={
            "fabric_connection_id": conn_id,
            "connection_type": "fabric_dataagent"
        }
    )
    # [END create_agent_with_fabric_tool]
    print(f"Created Agent, ID: {agent.id}")

    # Create thread for communication
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Delete the Agent when done
    # agents_client.delete_agent(agent.id)
    # print("Deleted agent")
