# Open AI 

## References

### Gen AI references
* [Authenticating with Azure OpenAI models, using Entra ID](https://github.com/LazaUK/AOAI-EntraIDAuth-SDKv1/tree/main)
* `Explained by MSFT's John Savill`
    * [RAG, semantic search, embedding, vector](https://www.youtube.com/watch?v=orLGv2LgWDE) <img src="/images/YouTube-icon-PNG.png" width="15" height="15">
* `Explained via blog & video - Luis Serrano - Cohere`
    * [Transformer Models](https://docs.cohere.com/docs/transformer-models)
        * [Transformers, explained: Understand the model behind GPT, BERT, and T5](https://www.youtube.com/watch?v=SZorAJ4I-sA) <img src="/images/YouTube-icon-PNG.png" width="15" height="15"> - `Better Explanation by Dale (Google)` 
    * [Text embeddings / Word & Sentence Embeddings](https://cohere.com/blog/sentence-word-embeddings)
    * [Semantic Search](https://cohere.com/blog/what-is-semantic-search)

### Hands-On code
* [ChatGPT-like app with your data using Azure OpenAI and Azure AI Search (Python)](https://github.com/Azure-Samples/azure-search-openai-demo/?tab=readme-ov-file)
    * <span style="color: green;">Works - got me to create Azure Open AI</span>
* [Langchain sample](https://github.com/Azure-Samples/SQL-AI-samples/blob/main/AzureSQLDatabase/LangChain/dbOpenAI.ipynb) - `Code sample using python, Azure SQL, OpenAI`
* [‘Talk’ to Your SQL Database Using LangChain and Azure OpenAI](https://towardsdatascience.com/talk-to-your-sql-database-using-langchain-and-azure-openai-bb79ad22c5e2) - `Explains the code & Prompt Engineering`
* [Building your own DB Copilot for Azure SQL with Azure OpenAI](https://devblogs.microsoft.com/azure-sql/building-your-own-db-copilot-for-azure-sql-with-azure-openai-gpt-4/)
    * <span style="color: red;">Errors out - Internal Server error - 500 (Azure APIM fronting the Azure Open AI)</span>
    * <span style="color: green;">Works - if request sent to Azure Open AI directly</span>
* [AI applications built on data from an Azure SQL Database](https://github.com/Azure-Samples/SQL-AI-samples) - `Code Samples using various LLM model & Azure SQL`
* [Key Concepts](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql#key-concepts)
    * [Retrieval Augmented Generation (RAG)](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql#retrieval-augmented-generation)
    * [Prompts and prompt engineering](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql#prompts-and-prompt-engineering)
    * [Tokens](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql#tokens)
    * [Vectors](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql#vectors)
    * [Embeddings](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql#embeddings)
    * [Semantic kernel](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql#semantic-kernel-integration)
    * [Langchain integration](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql#langchain-integration)
        * [Langchain](https://github.com/langchain-ai/langchain)
* [Intelligent applications with Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications?view=azuresql)
* [How I built a session recommender in 1 hour using Open AI](https://devblogs.microsoft.com/azure-sql/how-i-built-a-session-recommender-in-1-hour-using-open-ai/)
* [Python - DefaultAzureCredential & EnvironmentCredential ](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python#environment-variables)
* [how to generate embeddings with Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/embeddings?tabs=python-new)

### Generic references
* [How to set environment variables in bash](bash-env-readme.md)
* [Add certificate to CA bundle](https://github.com/jiasli/azure-notes/blob/master/cli/proxy-cert-win.md)
    * Refer to the steps on how it is explained that HTTPS traffic is intercepted by proxy `the root CA should be a self-signed certificate or a certificate issued by the company's IT department` & then how it is solved in section below `Add certificate to CA bundle`