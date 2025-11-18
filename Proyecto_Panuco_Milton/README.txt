=================================================================
  PROYECTO SEMANA 3, 4: GRAFOS Y VALIDACIÓN HAVEL-HAKIMI
=================================================================

AUTOR: Milton Castillo  
MATRÍCULA: 2301743  
CURSO: Estructuras de Datos Avanzadas  
FECHA: 4 de noviembre de 2025

=================================================================
CONTENIDO DEL PROYECTO
=================================================================

codigo/
  ├── Graph.cs              - Clase genérica de grafo
  ├── GraphValidator.cs     - Implementación Havel-Hakimi
  ├── Program.cs            - Programa principal con pruebas
  └── analysis.py           - Análisis de grafos en Python

datos/
  ├── edges_undirected.txt  - Grafo no dirigido (7 aristas)
  ├── edges_directed.txt    - Grafo dirigido (19 aristas)
  └── ciudad_extendida.txt  - Mapa urbano extendido (25 zonas)

tests/
  ├── GraphValidatorTests.cs - Tests unitarios C#
  └── test_havel_hakimi.py   - Tests casos oficiales Python

visualizaciones/
  └── havel_visualizer.html  - Visualizador interactivo

reportes/
  ├── Reporte_Semana3_Castillo.pdf
  └── Reporte_Semana4_Castillo.pdf

=================================================================
INSTRUCCIONES DE EJECUCIÓN
=================================================================

--- C# ---

1. Abrir el proyecto en Visual Studio o con dotnet CLI  
2. Compilar:
   dotnet build  
3. Ejecutar el programa principal:
   dotnet run --project Program.cs  
4. Los tests se ejecutan automáticamente al final del Program.cs

--- PYTHON ---

1. Ir a la carpeta codigo/:  
   cd codigo  
2. Ejecutar el análisis:
   python analysis.py  
3. Para probar los casos de Havel-Hakimi:
   cd ../tests  
   python test_havel_hakimi.py

--- VISUALIZADOR ---

1. Abrir visualizaciones/havel_visualizer.html en el navegador  
2. Ingresar una secuencia, por ejemplo: 4,3,3,2,2,2,1,1  
3. Dar clic en "Validar" y luego en "Paso Siguiente"

=================================================================
REQUISITOS DEL SISTEMA
=================================================================

C#:
  - .NET Framework 4.7 o .NET Core 3.1 en adelante  
  - Visual Studio 2019 o superior (opcional)

Python:
  - Versión 3.7 o superior  
  - No necesita librerías externas

Navegador:
  - Chrome, Firefox, Edge o Safari actualizados

=================================================================
DESCRIPCIÓN DE ARCHIVOS CLAVE
=================================================================

Graph.cs  
  Implementa una clase genérica para crear grafos con lista de adyacencia.  
  Soporta grafos dirigidos y no dirigidos.  
  Permite agregar vértices y aristas, recorrer con BFS/DFS  
  y exportar el grafo a un archivo .txt.

GraphValidator.cs  
  Contiene la parte del algoritmo de Havel-Hakimi para validar secuencias gráficas.  
  Incluye métodos para verificar si la suma de grados es par  
  y para extraer la secuencia desde un grafo cargado.

analysis.py  
  Script sencillo en Python que:
  - Carga grafos desde archivos .txt  
  - Calcula grados de entrada/salida  
  - Muestra el vértice más conectado  
  - Busca caminos con BFS

=================================================================
CASOS DE PRUEBA IMPLEMENTADOS
=================================================================

Se usaron los 10 casos del documento original.

VÁLIDOS:
  1. [4,3,3,2,2,2,1,1]
  2. [3,2,2,1]
  3. [4,3,3,2,2,2]
  4. [0,0,0,0]
  5. [3,3,3,3]

INVÁLIDOS:
  6. [3,3,3,1]
  7. [5,5,4,3,2,1]
  8. [3,2,1]
  9. [6,1,1,1,1,1,1]
  10. [5,3,2,2,1]

=================================================================
RESULTADOS ESPERADOS
=================================================================

Al ejecutar Program.cs:
  ✓ Carga el grafo de la semana 3  
  ✓ Extrae la secuencia de grados  
  ✓ Valida con Havel-Hakimi  
  ✓ Revisa que la suma sea par  
  ✓ Corre los 10 casos de prueba  
  ✓ Resultado final esperado: 10/10 PASS

Al ejecutar analysis.py:
  ✓ Analiza los grafos de ejemplo  
  ✓ Muestra grados y vértices conectados  
  ✓ Indica el vértice con más conexiones  
  ✓ Busca caminos entre vértices  

=================================================================
NOTAS ADICIONALES
=================================================================

- Los archivos .txt usan el formato: origen destino peso  
- En los grafos no dirigidos no se duplican las aristas  
- ciudad_extendida.txt contiene 25 zonas con nombres reales  
- La secuencia de grados debe ser gráfica según Havel-Hakimi  
- Si algún test falla, revisar el método IsGraphicalSequence()
