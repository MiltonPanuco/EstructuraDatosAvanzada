================================================================================
PROYECTO DE ESTRUCTURAS DE DATOS AVANZADAS 
================================================================================

ALUMNO: Milton Cruz Pánuco Castillo
PROFESOR: Dr. Eligardo Cruz Sanchez

================================================================================
DESCRIPCION
================================================================================

Este es mi proyecto del curso de Estructuras de Datos Avanzadas donde aprendi
sobre grafos, algoritmos y estructuras arboreas. El proyecto principal es
modelar una red de calles de una ciudad y encontrar las rutas mas cortas
entre puntos, ademas de implementar estructuras de datos especializadas como
arboles de busqueda balanceados y algoritmos de compresion.

Empece aprendiendo recursividad basica (semanas 1-2), luego grafos (semana 3),
validacion de grafos (semana 4), recorridos BFS/DFS (semana 5), algoritmos
de rutas mas cortas como Dijkstra y Floyd-Warshall (semana 6), arboles
generadores minimos con Prim y Kruskal (semana 7), y finalmente estructuras
arboreas avanzadas como BST, AVL y Huffman (semana 8).

================================================================================
QUE APRENDI
================================================================================

SEMANAS 1-2: Recursividad y programacion dinamica
SEMANA 3: Grafos basicos, como representarlos en codigo
SEMANA 4: Teorema de Havel-Hakimi para validar grafos
SEMANA 5: BFS (busqueda por niveles) y DFS (busqueda en profundidad)
SEMANA 6: Dijkstra y Floyd-Warshall para encontrar rutas mas cortas
SEMANA 7: Arboles generadores minimos (MST) con Prim y Kruskal, Union-Find
SEMANA 8: Arboles BST, AVL con rotaciones, y compresion Huffman

El profesor tira buen paro en la enseñanza pero también me ayudo a desarrollar
habilidades de aprendizaje autonomo. Aprendi a buscar informacion por mi cuenta
y a ser mas autodidacta, lo cual fue clave para entender temas complejos como
las rotaciones AVL, los algoritmos de compresion, y la estructura Union-Find
para deteccion de ciclos.

Aunque, si hubo algunos temas (por ejemplo el de Floyd-Warshall y Union-Find)
que utilice mucha inteligencia artificial para entender las cosas que estaba
haciendo al momento de ejecutar codigo.

================================================================================
COMO USAR
================================================================================

EJECUTAR CODIGO C#:
  cd codigo
  dotnet run
  dotnet test

EJECUTAR CODIGO PYTHON (Grafos):
  cd codigo
  python graph.py
  
  cd codigo
  python weighted_graph.py
  pytest test_weighted_graph.py -v

EJECUTAR CODIGO PYTHON (MST - Semana 7):
  cd codigo
  python mst.py
  pytest test_mst.py -v

EJECUTAR CODIGO PYTHON (Arboles - Semana 8):
  cd codigo
  python bst.py
  python avl.py
  python huffman.py
  python evaluador_postfijo.py

EJECUTAR TESTS (Semana 8):
  cd codigo
  python -m unittest test_bst.py -v
  python -m unittest test_avl.py -v
  python -m unittest test_huffman.py -v

VER VISUALIZACIONES:
  Abrir havel_visualizer.html en el navegador

================================================================================
QUE SE NECESITA INSTALAR
================================================================================

Para C#: .NET SDK desde https://dotnet.microsoft.com
Para Python: Python 3.8+ desde https://python.org
Para tests de Python: pip install pytest

================================================================================
ALGORITMOS IMPLEMENTADOS
================================================================================

GRAFOS:
- BFS: Busqueda en amplitud, O(V+E)
- DFS: Busqueda en profundidad, O(V+E)
- Dijkstra: Ruta mas corta desde un origen, O((V+E) log V)
- Floyd-Warshall: Rutas mas cortas entre todos los pares, O(V^3)
- Havel-Hakimi: Validacion de secuencias de grados, O(V^2)

ARBOLES GENERADORES MINIMOS (SEMANA 7):
- Prim: Construccion incremental del MST, O(E log V)
- Kruskal: MST por ordenamiento de aristas, O(E log E)
- Union-Find: Deteccion de ciclos con path compression, O(α(n))

ARBOLES (SEMANA 8):
- BST: Arbol binario de busqueda con insercion, busqueda y eliminacion
- AVL: Arbol autobalanceado con 4 tipos de rotaciones (LL, RR, LR, RL)
- Huffman: Compresion de datos mediante codificacion de longitud variable
- Evaluador postfijo: Evaluacion de expresiones en notacion polaca inversa

================================================================================
USO DE IA
================================================================================

Use inteligencia artificial como herramienta de apoyo en algunas partes del
codigo, especificamente en la implementacion de Floyd-Warshall, Union-Find
con path compression, y en algunos casos de las rotaciones AVL. Todo uso de
IA esta documentado en el codigo con comentarios que dicen:
"En esta parte tome ayuda de la IA para...". 

Sin embargo, en actividades mas recientes (semana 6-8 particularmente), no fue
tan necesaria su uso ya que desarrolle mejor capacidad de resolver problemas
por mi cuenta.

================================================================================
PROYECTO FINAL
================================================================================

El proyecto integrador consiste en modelar una red urbana donde:
- Nodos = Intersecciones o estaciones
- Aristas = Calles o conexiones
- Pesos = Distancias en km o tiempos en minutos

Con esto puedo:
1. Verificar si la red esta bien conectada
2. Encontrar la ruta mas corta entre dos puntos
3. Calcular distancias entre todos los puntos
4. Analizar el impacto de cerrar una calle
5. Diseñar red minima de conexion con MST (menor costo total)
6. Indexar y comprimir informacion de la red con estructuras arboreas

================================================================================
RESULTADOS
================================================================================

- Mas de 2000 lineas de codigo en C# y Python
- Tests unitarios funcionando para todas las estructuras
- Algoritmos de grafos, MST y arboles implementados correctamente
- Proyecto completo de red urbana funcional
- Sistema de compresion Huffman operativo
- Arboles AVL con balanceo automatico funcionando
- Implementacion de MST para diseño de redes con costo minimo

================================================================================
CONTACTO
================================================================================

Alumno: Milton Cruz Pánuco Castillo
Email: miltoncruz280@gmail.com
Universidad Autonoma de Nayarit

================================================================================