import heapq

class SistemaTransporte:
    def __init__(self):
        # Grafo: conexiones entre estaciones (tiempo estimado en minutos)
        self.grafo = {
            "Portal Norte": {"Calle 100": 10},
            "Calle 100": {"Portal Norte": 10, "Calle 72": 8},
            "Calle 72": {"Calle 100": 8, "Av. Jiménez": 7},
            "Av. Jiménez": {"Calle 72": 7, "Portal Sur": 15},
            "Portal Sur": {"Av. Jiménez": 15}
        }

        # Heurística: estimación al destino (ejemplo hacia Portal Sur)
        self.heuristica = {
            "Portal Norte": 30,
            "Calle 100": 20,
            "Calle 72": 15,
            "Av. Jiménez": 5,
            "Portal Sur": 0
        }

    def buscar_ruta(self, inicio, destino):
        cola = []
        heapq.heappush(cola, (0, inicio))

        costos = {inicio: 0}
        padres = {}

        while cola:
            _, actual = heapq.heappop(cola)

            if actual == destino:
                return self.reconstruir_ruta(padres, inicio, destino)

            for vecino, costo in self.grafo[actual].items():
                nuevo_costo = costos[actual] + costo

                if vecino not in costos or nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    prioridad = nuevo_costo + self.heuristica[vecino]
                    heapq.heappush(cola, (prioridad, vecino))
                    padres[vecino] = actual

        return None

    def reconstruir_ruta(self, padres, inicio, destino):
        ruta = [destino]
        while destino != inicio:
            destino = padres[destino]
            ruta.append(destino)
        ruta.reverse()
        return ruta


# ========================
# PRUEBA DEL SISTEMA
# ========================

if __name__ == "__main__":
    sistema = SistemaTransporte()

    origen = input("Ingrese estación origen: ")
    destino = input("Ingrese estación destino: ")

    ruta = sistema.buscar_ruta(origen, destino)

    if ruta:
        print("🛣️ Mejor ruta encontrada:")
        for estacion in ruta:
            print(f"→ {estacion}")
    else:
        print("❌ No se encontró ruta")