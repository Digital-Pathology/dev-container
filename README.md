# Setup Instructions

1. Install Docker and Remote Explorer Extension pack for VS Code.
2. Configure Github credentials for:
    - [Cloning Repos] Create a file named "credentials" in .devcontainer directory. In this file put your Github Username and Token using the following format:
        ```
        USER=<your-github-username>
        TOKEN=<your-github-token>
        ```
    - [Pushing/Pulling Repos] Follow the OS-specific instructions found at [this link](https://code.visualstudio.com/docs/remote/containers#_sharing-git-credentials-with-your-container).
3. Open the folder in VSCode using the docker extension.

## Notes for Windows Users

Windows runs Docker on top of Windows Subsystem for Linux (WSL), which is a bit greedy when it comes to memory use. For that reason it is strongly recommended that Windows users limit the memory use of WSL. See [this link](https://docs.microsoft.com/en-us/windows/wsl/wsl-config) for details.