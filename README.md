# Setup Instructions

1. Install Docker and Remote Explorer Extension pack for VS Code.
2. Create a file named "credentials" in .devcontainer directory. 
3. Put your Github Username and Token into the file:
    ```
    USER=
    TOKEN=
    ```
4. Open the folder in VSCode and click on "Reopen in container" in the bottom right.

## Notes for Windows Users

Windows runs Docker on top of Windows Subsystem for Linux (WSL), which is a bit greedy when it comes to memory use. For that reason it is strongly recommended that Windows users limit the memory use of WSL. See [this link](https://docs.microsoft.com/en-us/windows/wsl/wsl-config) for details.