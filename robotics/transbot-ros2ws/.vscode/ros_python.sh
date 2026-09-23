#!/usr/bin/env bash
source /opt/ros/jazzy/setup.bash
source "$(dirname "$0")/../install/setup.bash"   # your workspace overlay
exec /usr/bin/python3 "$@"
