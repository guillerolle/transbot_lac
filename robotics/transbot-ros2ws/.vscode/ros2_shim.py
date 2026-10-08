#!/usr/bin/env python3
import shlex
import sys

from ros2cli.cli import main

# Everything but the last argv entry is passed as-is; the last one is split shell-style.
*fixed, extra = sys.argv[1:]
sys.exit(main(argv=[*fixed, *shlex.split(extra)]))