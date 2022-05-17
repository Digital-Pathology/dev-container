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

## How to Add Python Dependencies

<b>Note: it is important to follow these steps closely to avoid messing up someone else's environment</b>

1. First make sure you're on a personal git branch, then save a backup of the current environment information: `cp environment.yml environment_old.yml`
2. Assuming the dependencies you'd like to add to the docker container's environment files are already installed in your running instance of the container, you can simply export your environment using `conda env export > environment.yml`
3. After you stage the changes to environment.yml, <b>carefully</b> examine the diff using a gui-based git tool to verify that the added/changed dependencies are consistent with what you're trying to do. Pay particular attention to upgraded or downgraded dependencies.
4. (Optionally) rebuild the container to test whether the dependencies play nicely together.

## Notes for Windows Users

Windows runs Docker on top of Windows Subsystem for Linux (WSL), which is a bit greedy when it comes to memory use. For that reason it is strongly recommended that Windows users limit the memory use of WSL. See [this link](https://docs.microsoft.com/en-us/windows/wsl/wsl-config) for details.