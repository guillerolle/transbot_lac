#!/bin/bash
# Este archivo compila el Dockerfile del ROSLAC, imagen que se usará para múltiples proyectos.
RUN_DIR="$(pwd)"
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
cd "$SCRIPT_DIR" || exit 1

ROSDISTRO="jazzy"

docker build --build-arg UID="$(id -u "${USER}")" --build-arg GID="$(id -g "${USER}")" --build-arg ROSDISTRO="$ROSDISTRO" --rm -t "roslac:$ROSDISTRO" .
cd "$RUN_DIR" || exit 1