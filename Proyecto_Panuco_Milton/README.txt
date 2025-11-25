================================================================================
PROYECTO DE ESTRUCTURAS DE DATOS AVANZADAS - SEMANAS 1 A 6
================================================================================

ALUMNO: Milton Cruz Pánuco Castillo
PROFESOR: Dr. Eligardo Cruz Sanchez

================================================================================
DESCRIPCION
================================================================================

Este es mi proyecto del curso de Estructuras de Datos Avanzadas donde aprendi
sobre grafos y algoritmos. El proyecto principal es modelar una red de calles
de una ciudad y encontrar las rutas mas cortas entre puntos.

Empece aprendiendo recursividad basica (semanas 1-2), luego grafos (semana 3),
validacion de grafos (semana 4), recorridos BFS/DFS (semana 5) y finalmente
algoritmos de rutas mas cortas como Dijkstra y Floyd-Warshall (semana 6).

================================================================================
QUE APRENDI
================================================================================

SEMANAS 1-2: Recursividad y programacion dinamica
SEMANA 3: Grafos basicos, como representarlos en codigo
SEMANA 4: Teorema de Havel-Hakimi para validar grafos
SEMANA 5: BFS (busqueda por niveles) y DFS (busqueda en profundidad)
SEMANA 6: Dijkstra y Floyd-Warshall para encontrar rutas mas cortas

================================================================================
ARCHIVOS PRINCIPALES
================================================================================

proyecto-semana3-4/codigo/csharp/
  - Graph.cs, GraphValidator.cs, Program.cs

proyecto-semana3-4/codigo/python/
  - graph.py, graph_validator.py, analysis.py

proyecto-semana3-4/datos/
  - edges_undirected.txt, edges_directed.txt, ciudad_extendida.txt

proyecto-semana3-4/tests/
  - test_havel_hakimi.py, GraphValidatorTests.cs

proyecto-semana3-4/visualizaciones/
  - havel_visualizer.html

proyecto-semana6/codigo/python/
  - weighted_graph.py, test_weighted_graph.py

proyecto-semana6/datos/
  - edges_weighted.csv

================================================================================
COMO USAR
================================================================================

EJECUTAR CODIGO C#:
  cd proyecto-semana3-4/codigo/csharp
  dotnet run
  dotnet test

EJECUTAR CODIGO PYTHON:
  cd proyecto-semana3-4/codigo/python
  python graph.py
  
  cd proyecto-semana6/codigo/python
  python weighted_graph.py
  pytest test_weighted_graph.py -v

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

- BFS: Busqueda en amplitud, O(V+E)
- DFS: Busqueda en profundidad, O(V+E)
- Dijkstra: Ruta mas corta desde un origen, O((V+E) log V)
- Floyd-Warshall: Rutas mas cortas entre todos los pares, O(V^3)
- Havel-Hakimi: Validacion de secuencias de grados, O(V^2)

================================================================================
USO DE IA
================================================================================

Use inteligencia artificial como herramienta de apoyo en algunas partes del
codigo, especificamente en la implementacion de Floyd-Warshall. Todo uso de
IA esta documentado en el codigo con comentarios que dicen:
"En esta parte tome ayuda de la IA para..."

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

================================================================================
RESULTADOS
================================================================================

- Mas de 1000 lineas de codigo en C# y Python
- Tests unitarios funcionando
- Algoritmos implementados correctamente
- Proyecto completo de red urbana funcional