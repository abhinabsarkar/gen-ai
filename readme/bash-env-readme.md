# Set Environment vairables

## Linux / WSL
1. Set the Environment Variable Temporarily:
* You can set the environment variable for the current session by running the following command in your WSL2 terminal:

    ```bash
    export OPENAI_API_VERSION='your_api_version_here'
    ```
* Replace `your_api_version_here` with the actual API version you intend to use.
* After setting it, run your Python script again in the same terminal session.

2. Set the Environment Variable Permanently:
* To permanently set the environment variable, you can add the `export` command to your shell's startup script, such as `~/.bashrc` or `~/.zshrc`, depending on your shell.
* Open your shell's startup script in a text editor. For example, if you're using bash, you can use:
    ```bash
    nano ~/.bashrc
   ```
* Add the following line at the end of the file:
    ```bash
    export OPENAI_API_VERSION='your_api_version_here'
    ```
* Save the file and exit the editor. Then, apply the changes by sourcing the startup script:
    ```bash
    source ~/.bashrc
    ```
* Now, every new terminal session will have the `OPENAI_API_VERSION` environment variable set.

3. Directly Specify the API Version in Code:
* As a quick fix, you can also directly specify the API version in your code instead of relying on an environment variable. This is less flexible but ensures your code runs without needing to set environment variables:
    ```bash
    client = AzureOpenAI(
    azure_endpoint=os.getenv("OPENAI_API_BASE"),
    azure_ad_token_provider=token_provider,
    api_version="your_api_version_here"  # Directly specify the API version here
    )
    ```
* Replace `"your_api_version_here"` with the actual API version.

Choose the method that best suits your needs. Setting the environment variable permanently is generally more flexible, especially if you're working on a project that might be run in different environments or shared with others.