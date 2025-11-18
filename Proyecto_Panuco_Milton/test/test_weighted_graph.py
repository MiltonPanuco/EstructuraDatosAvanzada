"""
Tests para algoritmos de optimizacion en grafos ponderados.
Cubre Dijkstra y Floyd-Warshall.
"""

import math

class WeightedGraph:
    def __init__(self):
        self.adj = {}
    
    def agregar_vertice(self, vertice):
        if vertice not in self.adj:
            self.adj[vertice] = []
    
    def agregar_arista(self, origen, destino, peso):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adj[origen].append((destino, peso))
    
    def dijkstra(self, origen):
        """Algoritmo de Dijkstra. Complejidad: O((V+E) log V)"""
        if origen not in self.adj:
            raise ValueError(f"El nodo {origen} no existe")
        
        distancias = {v: float('inf') for v in self.adj}
        padres = {v: None for v in self.adj}
        distancias[origen] = 0
        
        visitados = set()
        cola_prioridad = [(0, origen)]
        
        while cola_prioridad:
            cola_prioridad.sort()
            dist_actual, nodo_actual = cola_prioridad.pop(0)
            
            if nodo_actual in visitados:
                continue
            
            visitados.add(nodo_actual)
            
            for vecino, peso in self.adj[nodo_actual]:
                if vecino not in visitados:
                    nueva_distancia = dist_actual + peso
                    
                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
                        padres[vecino] = nodo_actual
                        cola_prioridad.append((nueva_distancia, vecino))
        
        return distancias, padres
    
    def reconstruir_camino(self, origen, destino, padres):
        """Reconstruye el camino desde origen hasta destino"""
        if destino not in padres or (padres[destino] is None and destino != origen):
            return None
        
        camino = []
        nodo = destino
        
        while nodo is not None:
            camino.append(nodo)
            nodo = padres[nodo]
        
        camino.reverse()
        return camino
    
    def floyd_warshall(self):
        """Algoritmo de Floyd-Warshall. Complejidad: O(V³)"""
        vertices = list(self.adj.keys())
        n = len(vertices)
        
        dist = {}
        siguiente = {}
        
        # Inicializacion
        for i in vertices:
            for j in vertices:
                if i == j:
                    dist[(i, j)] = 0
                    siguiente[(i, j)] = None
                else:
                    dist[(i, j)] = float('inf')
                    siguiente[(i, j)] = None
        
        # Agregar aristas existentes
        for u in vertices:
            for v, peso in self.adj[u]:
                dist[(u, v)] = peso
                siguiente[(u, v)] = v
        
        # Algoritmo principal
        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if dist[(i, k)] + dist[(k, j)] < dist[(i, j)]:
                        dist[(i, j)] = dist[(i, k)] + dist[(k, j)]
                        siguiente[(i, j)] = siguiente[(i, k)]
        
        # Detectar ciclos negativos
        for i in vertices:
            if dist[(i, i)] < 0:
                raise ValueError(f"Ciclo negativo detectado en vertice {i}")
        
        return dist, siguiente
    
    def reconstruir_camino_fw(self, origen, destino, siguiente):
        """Reconstruye camino usando matriz siguiente de FW"""
        if (origen, destino) not in siguiente or siguiente[(origen, destino)] is None:
            return None
        
        camino = []
        actual = origen
        
        while actual != destino:
            camino.append(actual)
            actual = siguiente[(actual, destino)]
            
            if actual is None:
                return None
        
        camino.append(destino)
        return camino

# TESTS

def test_1_dijkstra_simple():
    """Test 1: Dijkstra en grafo simple"""
    g = WeightedGraph()
    g.agregar_arista('A', 'B', 10)
    g.agregar_arista('A', 'C', 5)
    g.agregar_arista('C', 'D', 2)
    g.agregar_arista('B', 'D', 3)
    
    distancias, _ = g.dijkstra('A')
    
    return abs(distancias['D'] - 7) < 0.001

def test_2_dijkstra_pesos_cero():
    """Test 2: Dijkstra con pesos cero"""
    g = WeightedGraph()
    g.agregar_arista('A', 'B', 0)
    g.agregar_arista('B', 'C', 5)
    
    distancias, _ = g.dijkstra('A')
    
    return abs(distancias['C'] - 5) < 0.001

def test_3_dijkstra_desconectado():
    """Test 3: Dijkstra grafo desconectado"""
    g = WeightedGraph()
    g.agregar_arista('A', 'B', 10)
    g.agregar_vertice('C')
    
    distancias, _ = g.dijkstra('A')
    
    return math.isinf(distancias['C'])

def test_4_reconstruir_camino():
    """Test 4: Reconstruccion de camino"""
    g = WeightedGraph()
    g.agregar_arista('A', 'B', 4)
    g.agregar_arista('A', 'C', 2)
    g.agregar_arista('B', 'D', 1)
    g.agregar_arista('C', 'D', 3)
    
    distancias, padres = g.dijkstra('A')
    camino = g.reconstruir_camino('A', 'D', padres)
    
    return (camino is not None and 
            len(camino) == 3 and 
            camino[0] == 'A' and 
            camino[2] == 'D')

def test_5_floyd_warshall_simple():
    """Test 5: Floyd-Warshall simple"""
    g = WeightedGraph()
    g.agregar_arista('A', 'B', 4)
    g.agregar_arista('B', 'C', 2)
    g.agregar_arista('C', 'A', 3)
    
    dist, _ = g.floyd_warshall()
    
    return abs(dist[('A', 'C')] - 6) < 0.001

def test_6_floyd_warshall_negativos():
    """Test 6: Floyd-Warshall con pesos negativos"""
    g = WeightedGraph()
    g.agregar_arista('A', 'B', 2)
    g.agregar_arista('B', 'C', -1)
    
    dist, _ = g.floyd_warshall()
    
    return abs(dist[('A', 'C')] - 1) < 0.001

def test_7_ciclo_negativo():
    """Test 7: Deteccion de ciclo negativo"""
    g = WeightedGraph()
    g.agregar_arista('A', 'B', -2)
    g.agregar_arista('B', 'A', -1)
    
    try:
        dist, _ = g.floyd_warshall()
        return False
    except ValueError:
        return True

def test_8_dijkstra_nodo_inexistente():
    """Test 8: Dijkstra con nodo inexistente"""
    g = WeightedGraph()
    g.agregar_arista('A', 'B', 10)
    
    try:
        distancias, _ = g.dijkstra('Z')
        return False
    except ValueError:
        return True

def test_9_camino_inexistente():
    """Test 9: Camino inexistente retorna None"""
    g = WeightedGraph()
    g.agregar_arista('A', 'B', 10)
    g.agregar_vertice('C')
    
    distancias, padres = g.dijkstra('A')
    camino = g.reconstruir_camino('A', 'C', padres)
    
    return camino is None

def test_10_floyd_warshall_desconectado():
    """Test 10: Floyd-Warshall con grafo desconectado"""
    g = WeightedGraph()
    g.agregar_arista('A', 'B', 10)
    g.agregar_vertice('C')
    
    dist, _ = g.floyd_warshall()
    
    return math.isinf(dist[('A', 'C')])

def ejecutar_todos_los_tests():
    """Ejecuta todos los tests y muestra resultados"""
    print("\n" + "="*60)
    print("  EJECUCION DE TESTS DE DIJKSTRA Y FLOYD-WARSHALL - PYTHON")
    print("="*60 + "\n")
    
    tests = [
        ("Test 1: Dijkstra simple", test_1_dijkstra_simple),
        ("Test 2: Dijkstra pesos cero", test_2_dijkstra_pesos_cero),
        ("Test 3: Dijkstra desconectado", test_3_dijkstra_desconectado),
        ("Test 4: Reconstruccion camino", test_4_reconstruir_camino),
        ("Test 5: Floyd-Warshall simple", test_5_floyd_warshall_simple),
        ("Test 6: Floyd-Warshall negativos", test_6_floyd_warshall_negativos),
        ("Test 7: Ciclo negativo", test_7_ciclo_negativo),
        ("Test 8: Dijkstra nodo inexistente", test_8_dijkstra_nodo_inexistente),
        ("Test 9: Camino inexistente", test_9_camino_inexistente),
        ("Test 10: FW desconectado", test_10_floyd_warshall_desconectado)
    ]
    
    pasados = 0
    total = len(tests)
    
    for nombre, test_func in tests:
        try:
            if test_func():
                print(f"{nombre}: [PASS]")
                pasados += 1
            else:
                print(f"{nombre}: [FAIL]")
        except Exception as e:
            print(f"{nombre}: [FAIL] - Error: {e}")
    
    print("\n" + "="*60)
    print(f"RESULTADO: {pasados}/{total} tests pasados")
    print("="*60 + "\n")

if __name__ == "__main__":
    ejecutar_todos_los_tests()