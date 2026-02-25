#!/bin/bash

RUN_DIR="$(pwd)"
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
cd "$SCRIPT_DIR" || exit 1 
colcon build --symlink-install
cd "$RUN_DIR" || exit 1
