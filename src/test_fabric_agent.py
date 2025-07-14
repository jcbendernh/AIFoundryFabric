# pylint: disable=line-too-long,useless-suppression
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

"""
FILE: test_agent_revenue.py

DESCRIPTION:
    Test script to interact with an existing agent and ask about revenue per country.

USAGE:
    python test_agent_revenue.py

    Before running the script:
    pip install azure-identity
    pip install --pre azure-ai-projects
"""

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder

# Initialize the project client
project_client = AIProjectClient(
    endpoint="https://foundry-q3te.services.ai.azure.com/api/projects/project-q3te",
    credential=DefaultAzureCredential(),
)

# Existing agent ID to test
AGENT_ID = "<AGENT ID>" #Insert Agent ID from AI Foundry Portal

with project_client:
    agents_client = project_client.agents
    
    print(f"Testing Agent ID: {AGENT_ID}")
    
    # Get agent details to confirm it exists
    try:
        agent = agents_client.get_agent(AGENT_ID)
        print(f"Agent Name: {agent.name}")
        print(f"Agent Model: {agent.model}")
        print(f"Agent Instructions: {agent.instructions[:100]}...")
    except Exception as e:
        print(f"Error retrieving agent: {e}")
        exit(1)

    # Create thread for communication
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

    print("\nReady to chat with the agent. Type 'exit' or 'quit' to end the conversation.\n")
    
    while True:
        user_question = input("Your question: ").strip()
        
        if user_question.lower() in ['exit', 'quit', '']:
            print("Ending conversation...")
            break

        # Create message to thread
        message = agents_client.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_question,
        )

        # Create and process an Agent run in thread
        print("Processing...")
        run = agents_client.runs.create_and_process(thread_id=thread.id, agent_id=AGENT_ID)

        if run.status == "failed":
            print(f"❌ Run failed: {run.last_error}")
        else:
            # Get the latest assistant message
            messages_list = list(agents_client.messages.list(thread_id=thread.id, order=ListSortOrder.DESCENDING, limit=1))
            if messages_list and messages_list[0].text_messages:
                last_text = messages_list[0].text_messages[-1]
                print(f"\n🤖 Agent: {last_text.text.value}\n")
                print("-" * 60)

    print(f"\nConversation ended. Thread ID: {thread.id}")
