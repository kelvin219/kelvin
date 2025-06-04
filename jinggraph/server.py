from __future__ import annotations

import json
from pathlib import Path
from flask import Flask, send_from_directory, jsonify

from .graph import JingGraph


def create_app(graph_path: str) -> Flask:
    app = Flask(__name__)
    g = JingGraph.load(graph_path)

    @app.route("/api/graph")
    def graph() -> tuple[str, int]:
        return jsonify(g.to_dict())

    @app.route("/")
    def index() -> tuple[str, int]:
        html_path = Path(__file__).with_name("index.html")
        return send_from_directory(html_path.parent, html_path.name)

    return app


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Run JingGraph demo server")
    parser.add_argument("graph", help="Path to graph JSON file")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    app = create_app(args.graph)
    app.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()

