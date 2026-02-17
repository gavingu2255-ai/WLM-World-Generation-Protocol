"""
Command-line interface for WLM‑World‑Generation‑Protocol.

Usage:
    wlm-worldgen generate spec.json
    wlm-worldgen generate '{"theme": "ruins"}'
"""

import argparse
import json
import sys
from pathlib import Path

from .api import generate_world


def load_input(input_arg: str):
    """
    Load input either from a JSON file or inline JSON string.
    """
    path = Path(input_arg)
    if path.exists() and path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return json.loads(input_arg)


def cmd_generate(args):
    try:
        spec = load_input(args.input)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

        # unreachable but safe
    world = generate_world(spec)

    if args.out:
        Path(args.out).write_text(json.dumps(world, indent=2), encoding="utf-8")
    else:
        print(json.dumps(world, indent=2))


def main():
    parser = argparse.ArgumentParser(
        prog="wlm-worldgen",
        description="WLM‑World‑Generation‑Protocol CLI"
    )

    sub = parser.add_subparsers(dest="command")

    # generate
    p_generate = sub.add_parser(
        "generate",
        help="Generate a world from a specification"
    )
    p_generate.add_argument("input", help="JSON file path or inline JSON")
    p_generate.add_argument("--out", help="Write output to file")
    p_generate.set_defaults(func=cmd_generate)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)
