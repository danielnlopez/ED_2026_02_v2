from goodrich.ch14.graph import Graph


def vecinos(g, v):
    """Retorna una lista con los elementos de los vecinos de v."""
    return [
        e.opposite(v).element()
        for e in g.incident_edges(v)
    ]


def dfs(g, v, d):
    """Agrega a d cada vértice descubierto y la arista que lo descubrió.

    v ya debe estar en d antes de llamar esta función.
    """
    for e in g.incident_edges(v):
        w = e.opposite(v)
        if w not in d:
            d[w] = e
            dfs(g, w, d)


def bfs(g, v):
    """Retorna los vértices descubiertos y la arista que descubrió a cada uno."""
    d = {v: None}
    nivel = [v]

    while nivel:
        siguiente_nivel = []

        for u in nivel:
            for e in g.incident_edges(u):
                w = e.opposite(u)
                if w not in d:
                    d[w] = e
                    siguiente_nivel.append(w)

        nivel = siguiente_nivel

    return d


def alcanzables(g, v):
    """Retorna los elementos de los vértices alcanzables desde v, incluido v."""
    descubiertos = bfs(g, v)
    return [vertice.element() for vertice in descubiertos]


if __name__ == "__main__":
    pass
