#!/bin/bash

set -e

function main() {
    prepare_image
    prepare_server
    run_app
    cleanup
}

function prepare_image() {
    echo '>>> Log in to Container Registry'
    echo "$PAT" | docker login ghcr.io -u "$USER" --password-stdin

    echo '>>> Build caddy image'
    docker build --tag ghcr.io/dmitrvk/dmitrvkml_caddy:latest caddy

    echo '>>> Build app image'
    docker build --tag ghcr.io/dmitrvk/dmitrvkml:latest .

    echo '>>> Push caddy image'
    docker push ghcr.io/dmitrvk/dmitrvkml_caddy:latest

    echo '>>> Push app image'
    docker push ghcr.io/dmitrvk/dmitrvkml:latest
}

function prepare_server() {
    echo '>>> Create project directory'
    ssh "$USER"@"$HOST" -p "$PORT" mkdir -p "~/$PROJECT_NAME"

    echo '>>> Docker login on server'
    ssh "$USER"@"$HOST" -p "$PORT" "echo $PAT | docker login ghcr.io -u $USER --password-stdin"

    echo '>>> Copy docker compose file'
    scp -P "$PORT" docker-compose.yml "$USER"@"$HOST":~/"$PROJECT_NAME"/docker-compose.yml
}

function run_app() {
    echo '>>> Pull docker images'
    ssh "$USER"@"$HOST" -p "$PORT" "cd ~/$PROJECT_NAME && docker-compose pull"

    echo '>>> Run services'
    ssh "$USER"@"$HOST" -p "$PORT" "cd ~/$PROJECT_NAME && docker-compose up -d"
}

function cleanup() {
    echo '>>> Clean docker images'
    ssh "$USER"@"$HOST" -p "$PORT" 'docker system prune --all --force'
}

main
