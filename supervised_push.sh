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
}

pip_install_editable(){
    pip install -e "/workspaces/dev-container/${1}";
}

rm -rf /workspaces/dev-container/ML-Supervised
clone_repo ML-Supervised main

copy /workspaces/dev-container/ML-Supervised
build_and_push kevin_supervised