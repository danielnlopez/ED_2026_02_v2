class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def _mostrar_heap(self):
        """Dibuja el estado actual del heap como un árbol binario."""
        import math
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle

        n = len(self.arreglo) - 1

        if n == 0:
            fig, ax = plt.subplots(figsize=(4, 2))
            ax.text(0.5, 0.5, "Heap vacío", ha="center", va="center")
            ax.axis("off")
            plt.show()
            return

        profundidad = math.floor(math.log2(n))
        ancho = max(6, 1.15 * (2 ** profundidad))
        alto = max(2.5, 1.35 * (profundidad + 1))

        fig, ax = plt.subplots(figsize=(ancho, alto))
        posiciones = {}

        # Calcula la posición de cada nodo según su índice en el arreglo.
        for i in range(1, n + 1):
            nivel = i.bit_length() - 1
            primer_indice = 2 ** nivel
            posicion_nivel = i - primer_indice

            x = (posicion_nivel + 0.5) / (2 ** nivel)
            y = -nivel
            posiciones[i] = (x, y)

        # Dibuja primero las aristas para que queden detrás de los nodos.
        for i in range(1, n + 1):
            for hijo in (2 * i, 2 * i + 1):
                if hijo <= n:
                    x1, y1 = posiciones[i]
                    x2, y2 = posiciones[hijo]
                    ax.plot([x1, x2], [y1, y2],
                            color="black", linewidth=1.5, zorder=1)

        radio = 0.22 / (2 ** max(0, profundidad - 2))
        radio = max(0.055, radio)

        # Dibuja los nodos y escribe su valor.
        for i, (x, y) in posiciones.items():
            nodo = Circle(
                (x, y), radio,
                facecolor="#E8F1FA",
                edgecolor="#24527A",
                linewidth=1.5,
                zorder=2
            )
            ax.add_patch(nodo)
            ax.text(
                x, y, str(self.arreglo[i]),
                ha="center", va="center",
                fontsize=max(7, 12 - profundidad),
                zorder=3
            )

        ax.set_xlim(-0.08, 1.08)
        ax.set_ylim(-profundidad - 0.6, 0.6)
        ax.set_aspect("equal")
        ax.axis("off")
        plt.tight_layout()
        plt.show()

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        indice_hijo = len(self.arreglo) - 1

        # Sube el nuevo elemento mientras sea menor que su padre.
        while indice_hijo > 1:
            indice_padre = indice_hijo // 2

            if self.arreglo[indice_hijo] >= self.arreglo[indice_padre]:
                break

            self.arreglo[indice_hijo], self.arreglo[indice_padre] = (
                self.arreglo[indice_padre], self.arreglo[indice_hijo]
            )
            indice_hijo = indice_padre

        if imagen:
            self._mostrar_heap()

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) == 1:
            raise IndexError("No se puede eliminar de un heap vacío.")

        menor = self.arreglo[1]
        ultimo = self.arreglo.pop()

        if len(self.arreglo) > 1:
            self.arreglo[1] = ultimo
            indice = 1

            # Baja el elemento hasta recuperar la propiedad de min heap.
            while 2 * indice < len(self.arreglo):
                hijo = 2 * indice
                hijo_derecho = hijo + 1

                if (hijo_derecho < len(self.arreglo)
                        and self.arreglo[hijo_derecho] < self.arreglo[hijo]):
                    hijo = hijo_derecho

                if self.arreglo[indice] <= self.arreglo[hijo]:
                    break

                self.arreglo[indice], self.arreglo[hijo] = (
                    self.arreglo[hijo], self.arreglo[indice]
                )
                indice = hijo

        if imagen:
            self._mostrar_heap()

        return menor

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)

        # Aplica el procedimiento de abajo hacia arriba.
        for indice in range((len(self.arreglo) - 1) // 2, 0, -1):
            while 2 * indice < len(self.arreglo):
                hijo = 2 * indice
                hijo_derecho = hijo + 1

                if (hijo_derecho < len(self.arreglo)
                        and self.arreglo[hijo_derecho] < self.arreglo[hijo]):
                    hijo = hijo_derecho

                if self.arreglo[indice] <= self.arreglo[hijo]:
                    break

                self.arreglo[indice], self.arreglo[hijo] = (
                    self.arreglo[hijo], self.arreglo[indice]
                )
                indice = hijo

        if imagen:
            self._mostrar_heap()
