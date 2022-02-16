#!/bin/bash

goto(){
    cd "/workspaces/$1"
}

clone_repo(){

    if [[ ! -d "/workspaces/dev-container/${1}/.git" && -d "/workspaces/dev-container/${1}" ]]; then
        echo "Removing ${1} ..."
        rm -rf "/workspaces/dev-container/${1}"
    fi

    goto "dev-container"
    if [[ ! -d "/workspaces/dev-container/${1}" ]]; then
        git clone "https://${USER}:${TOKEN}@github.com/Digital-Pathology/${1}.git" -b ${2}
        goto "dev-container/${1}"
        git remote set-url origin "git@github.com:Digital-Pathology/${1}.git"
    fi
    
    # if [[ -f "/workspaces/dev-container/${1}/environment.yml" ]]; then
    #     conda env update --file "/workspaces/dev-container/${1}/environment.yml"
    # fi

    if [[ -f "/workspaces/dev-container/${1}/setup.cfg" ]]; then
        pip install -e "/workspaces/dev-container/${1}";
    fi
}

. ./.devcontainer/credentials

cp /tmp/.zshrc /home/vscode/
cp /tmp/.bashrc /home/vscode/

conda env update --file /workspaces/dev-container/environment.yml

clone_repo UnifiedImageReader main
clone_repo WebApp main
clone_repo ModelManager main
clone_repo Filtration main
clone_repo CustomDataset main
clone_repo ML-Supervised main
clone_repo ML-Unsupervised main
clone_repo PublicDatasetMaterial main
