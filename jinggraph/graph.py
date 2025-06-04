from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Any


@dataclass
class Node:
    id: str
    type: str
    label: str
    origin: Optional[str] = None
    attributes: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Edge:
    source: str
    target: str
    type: str
    weight: Optional[float] = None
    context: Optional[str] = None


class JingGraph:
    def __init__(self) -> None:
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []

    def add_node(self, node: Node) -> None:
        self.nodes[node.id] = node

    def add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)

    @classmethod
    def load(cls, path: str) -> "JingGraph":
        graph = cls()
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for n in data.get("nodes", []):
            node = Node(**n)
            graph.add_node(node)
        for e in data.get("edges", []):
            edge = Edge(**e)
            graph.add_edge(edge)
        return graph

    def to_dict(self) -> Dict[str, Any]:
        return {
            "nodes": [asdict(n) for n in self.nodes.values()],
            "edges": [asdict(e) for e in self.edges],
        }

    def save(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)

