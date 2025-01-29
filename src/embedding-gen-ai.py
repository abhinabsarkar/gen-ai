import os
import json
from openai import AzureOpenAI
from azure.identity import EnvironmentCredential, get_bearer_token_provider

# Authenticate using the Service Principal
token_provider = get_bearer_token_provider(
    EnvironmentCredential(),
    "https://cognitiveservices.azure.com/.default"
)

# Fetch the Azure OpenAI details from the environment variables
client = AzureOpenAI(
    azure_endpoint = os.getenv("OPENAI_API_BASE"), # e.g. https://api.openai.com
    azure_ad_token_provider = token_provider,    # Azure AD token provider
    api_version = os.getenv("OPENAI_API_VERSION")   # e.g. 2024-02-01
)

# Using loop to get user input and generate embeddings
while True:
    user_input = input("Enter text to get embeddings (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    response = client.embeddings.create(
        input=user_input,
        model="text-embedding-ada-002",
        # print_cost=True
    )

    data = json.loads(response.model_dump_json(indent=2))
    embedding_count = len(data['data'][0]['embedding'])
    model_name = data['model']
    prompt_token_count = data['usage']['prompt_tokens']
    total_token_count = data['usage']['total_tokens']

    print(response.model_dump_json(indent=2))
    # print(data)
    print(f"Model: {model_name}")
    print(f"Count of embedding objects: {embedding_count}")
    print(f"Prompt token count: {prompt_token_count}")
    print(f"Total token count: {total_token_count}")

print("Exited.")