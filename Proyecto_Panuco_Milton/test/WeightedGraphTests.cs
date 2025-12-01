using System;
using System.Collections.Generic;
using System.Linq;

namespace SistemaGrafos
{
    public static class WeightedGraphTests
    {
        public static void EjecutarTodos()
        {
            Console.WriteLine("\n" + new string('=', 60));
            Console.WriteLine("  EJECUCION DE TESTS DE DIJKSTRA Y FLOYD-WARSHALL");
            Console.WriteLine(new string('=', 60));

            int pasados = 0;
            int total = 0;

            // Test 1: Dijkstra simple
            total++;
            if (Test1_Dijkstra_Simple())
            {
                Console.WriteLine("Test 1: [PASS] Dijkstra en grafo simple");
                pasados++;
            }
            else
            {
                Console.WriteLine("Test 1: [FAIL] Dijkstra en grafo simple");
            }

            // Test 2: Dijkstra con pesos cero
            total++;
            if (Test2_Dijkstra_PesosCero())
            {
                Console.WriteLine("Test 2: [PASS] Dijkstra con pesos cero");
                pasados++;
            }
            else
            {
                Console.WriteLine("Test 2: [FAIL] Dijkstra con pesos cero");
            }

            // Test 3: Dijkstra grafo desconectado
            total++;
            if (Test3_Dijkstra_Desconectado())
            {
                Console.WriteLine("Test 3: [PASS] Dijkstra grafo desconectado");
                pasados++;
            }
            else
            {
                Console.WriteLine("Test 3: [FAIL] Dijkstra grafo desconectado");
            }

            // Test 4: Reconstruir camino
            total++;
            if (Test4_ReconstruirCamino())
            {
                Console.WriteLine("Test 4: [PASS] Reconstruccion de camino");
                pasados++;
            }
            else
            {
                Console.WriteLine("Test 4: [FAIL] Reconstruccion de camino");
            }

            // Test 5: Floyd-Warshall simple
            total++;
            if (Test5_FloydWarshall_Simple())
            {
                Console.WriteLine("Test 5: [PASS] Floyd-Warshall simple");
                pasados++;
            }
            else
            {
                Console.WriteLine("Test 5: [FAIL] Floyd-Warshall simple");
            }

            // Test 6: Floyd-Warshall con pesos negativos
            total++;
            if (Test6_FloydWarshall_Negativos())
            {
                Console.WriteLine("Test 6: [PASS] Floyd-Warshall pesos negativos");
                pasados++;
            }
            else
            {
                Console.WriteLine("Test 6: [FAIL] Floyd-Warshall pesos negativos");
            }

            // Test 7: Deteccion de ciclo negativo
            total++;
            if (Test7_CicloNegativo())
            {
                Console.WriteLine("Test 7: [PASS] Deteccion ciclo negativo");
                pasados++;
            }
            else
            {
                Console.WriteLine("Test 7: [FAIL] Deteccion ciclo negativo");
            }

            // Test 8: Dijkstra nodo inexistente
            total++;
            if (Test8_Dijkstra_NodoInexistente())
            {
                Console.WriteLine("Test 8: [PASS] Dijkstra nodo inexistente");
                pasados++;
            }
            else
            {
                Console.WriteLine("Test 8: [FAIL] Dijkstra nodo inexistente");
            }

            // Test 9: Vertice mas central
            total++;
            if (Test9_VerticeMasCentral())
            {
                Console.WriteLine("Test 9: [PASS] Vertice mas central");
                pasados++;
            }
            else
            {
                Console.WriteLine("Test 9: [FAIL] Vertice mas central");
            }

            // Test 10: Distancia maxima
            total++;
            if (Test10_DistanciaMaxima())
            {
                Console.WriteLine("Test 10: [PASS] Distancia maxima");
                pasados++;
            }
            else
            {
                Console.WriteLine("Test 10: [FAIL] Distancia maxima");
            }

            Console.WriteLine("\n" + new string('=', 60));
            Console.WriteLine("RESULTADO: " + pasados + "/" + total + " tests pasados");
            Console.WriteLine(new string('=', 60) + "\n");
        }

        private static bool Test1_Dijkstra_Simple()
        {
            try
            {
                WeightedGraph g = new WeightedGraph();
                g.AgregarArista("A", "B", 10);
                g.AgregarArista("A", "C", 5);
                g.AgregarArista("C", "D", 2);
                g.AgregarArista("B", "D", 3);

                var (distancias, _) = g.Dijkstra("A");

                return Math.Abs(distancias["D"] - 7) < 0.001;
            }
            catch
            {
                return false;
            }
        }

        private static bool Test2_Dijkstra_PesosCero()
        {
            try
            {
                WeightedGraph g = new WeightedGraph();
                g.AgregarArista("A", "B", 0);
                g.AgregarArista("B", "C", 5);

                var (distancias, _) = g.Dijkstra("A");

                return Math.Abs(distancias["C"] - 5) < 0.001;
            }
            catch
            {
                return false;
            }
        }

        private static bool Test3_Dijkstra_Desconectado()
        {
            try
            {
                WeightedGraph g = new WeightedGraph();
                g.AgregarArista("A", "B", 10);
                g.AgregarVertice("C");

                var (distancias, _) = g.Dijkstra("A");

                return double.IsPositiveInfinity(distancias["C"]);
            }
            catch
            {
                return false;
            }
        }

        private static bool Test4_ReconstruirCamino()
        {
            try
            {
                WeightedGraph g = new WeightedGraph();
                g.AgregarArista("A", "B", 4);
                g.AgregarArista("A", "C", 2);
                g.AgregarArista("B", "D", 1);
                g.AgregarArista("C", "D", 3);

                var (distancias, padres) = g.Dijkstra("A");
                List<string> camino = g.ReconstruirCamino("A", "D", padres);

                return camino != null && 
                       camino.Count == 3 && 
                       camino[0] == "A" && 
                       camino[2] == "D";
            }
            catch
            {
                return false;
            }
        }

        private static bool Test5_FloydWarshall_Simple()
        {
            try
            {
                WeightedGraph g = new WeightedGraph();
                g.AgregarArista("A", "B", 4);
                g.AgregarArista("B", "C", 2);
                g.AgregarArista("C", "A", 3);

                var (dist, _) = g.FloydWarshall();

                return Math.Abs(dist[("A", "C")] - 6) < 0.001;
            }
            catch
            {
                return false;
            }
        }

        private static bool Test6_FloydWarshall_Negativos()
        {
            try
            {
                WeightedGraph g = new WeightedGraph();
                g.AgregarArista("A", "B", 2);
                g.AgregarArista("B", "C", -1);

                var (dist, _) = g.FloydWarshall();

                return Math.Abs(dist[("A", "C")] - 1) < 0.001;
            }
            catch
            {
                return false;
            }
        }

        private static bool Test7_CicloNegativo()
        {
            try
            {
                WeightedGraph g = new WeightedGraph();
                g.AgregarArista("A", "B", -2);
                g.AgregarArista("B", "A", -1);

                var (dist, _) = g.FloydWarshall();

                return false; // No deberia llegar aqui
            }
            catch (InvalidOperationException)
            {
                return true; // Debe lanzar excepcion
            }
            catch
            {
                return false;
            }
        }

        private static bool Test8_Dijkstra_NodoInexistente()
        {
            try
            {
                WeightedGraph g = new WeightedGraph();
                g.AgregarArista("A", "B", 10);

                var (distancias, _) = g.Dijkstra("Z");

                return false; // No deberia llegar aqui
            }
            catch (ArgumentException)
            {
                return true; // Debe lanzar excepcion
            }
            catch
            {
                return false;
            }
        }

        private static bool Test9_VerticeMasCentral()
        {
            try
            {
                WeightedGraph g = new WeightedGraph();
                g.AgregarArista("A", "B", 1);
                g.AgregarArista("A", "C", 1);
                g.AgregarArista("B", "D", 1);
                g.AgregarArista("C", "D", 1);

                string central = g.EncontrarVerticeMasCentral();

                return central == "A" || central == "D";
            }
            catch
            {
                return false;
            }
        }

        private static bool Test10_DistanciaMaxima()
        {
            try
            {
                WeightedGraph g = new WeightedGraph();
                g.AgregarArista("A", "B", 5);
                g.AgregarArista("B", "C", 10);

                double maxDist = g.CalcularDistanciaMaxima();

                return Math.Abs(maxDist - 15) < 0.001;
            }
            catch
            {
                return false;
            }
        }
    }

}
