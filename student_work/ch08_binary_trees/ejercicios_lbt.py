from goodrich.ch08.linked_binary_tree import LinkedBinaryTree
from goodrich.ch06.array_queue import ArrayQueue

def es_completo(T):
    """Retorna True si T es un árbol binario completo."""
    if T.is_empty():
        return True

    cola = ArrayQueue()
    cola.enqueue(T.root())
    falta_hijo = False

    while not cola.is_empty():
        p = cola.dequeue()

        izquierdo = T.left(p)
        derecho = T.right(p)

        if izquierdo is not None:
            if falta_hijo:
                return False
            cola.enqueue(izquierdo)
        else:
            falta_hijo = True

        if derecho is not None:
            if falta_hijo:
                return False
            cola.enqueue(derecho)
        else:
            falta_hijo = True

    return True


def camino(T, p, q):
    """Retorna el camino de p a q como string: 'H -> D -> B -> E'."""
    ancestros_p = []
    actual = p

    while actual is not None:
        ancestros_p.append(actual)
        actual = T.parent(actual)

    ancestros_q = []
    actual = q

    while actual is not None:
        ancestros_q.append(actual)
        actual = T.parent(actual)

    for ancestro in ancestros_p:
        if ancestro in ancestros_q:
            comun = ancestro
            break

    camino_nodos = []

    actual = p
    while actual != comun:
        camino_nodos.append(actual)
        actual = T.parent(actual)

    camino_nodos.append(comun)

    parte_q = []
    actual = q
    while actual != comun:
        parte_q.append(actual)
        actual = T.parent(actual)

    camino_nodos.extend(reversed(parte_q))

    return " -> ".join(str(nodo.element()) for nodo in camino_nodos)


if __name__ == "__main__":
    # tus pruebas (opcional)
    pass
