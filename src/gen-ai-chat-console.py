import os
from openai import AzureOpenAI
from azure.identity import EnvironmentCredential, get_bearer_token_provider

# Authenticate using the Service Principal.
# Add the below values to your environment variables.
        # AZURE_CLIENT_ID=
        # AZURE_CLIENT_SECRET=
        # AZURE_TENANT_ID=
token_provider = get_bearer_token_provider(
    EnvironmentCredential(),
    "https://cognitiveservices.azure.com/.default"
)

# Fetch the Azure OpenAI details from the environment variables
client = AzureOpenAI(
    azure_endpoint=os.getenv("OPENAI_API_BASE"),
    azure_ad_token_provider=token_provider,
    api_version=os.getenv("OPENAI_API_VERSION")
)

# Define the prompt and context for the model
prompt_and_context = "You are a helpful assistant answering questions about Cricket. \
                    You will only answer about cricket questions & nothing else."

while True:
    user_input = input("Enter your question (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    # Use the OpenAIClient to get a response from the model
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt_and_context}, # Set the prompt & context for the AI assistant
            {"role": "user", "content": user_input}
        ]
    )

    # Get the response details
    completion_text = response.choices[0].message.content
    model = response.model
    prompt_token_count = response.usage.prompt_tokens
    completion_token_count = response.usage.completion_tokens
    total_token_count = response.usage.total_tokens

    # Print the response
    print(completion_text)
    print(f"\n--- Response Analytics ---")
    print(f"Model: {model}")
    print(f"Prompt token count: {prompt_token_count}")
    print(f"Completion token count: {completion_token_count}")
    print(f"Total token count: {total_token_count}")

print("Exited.")