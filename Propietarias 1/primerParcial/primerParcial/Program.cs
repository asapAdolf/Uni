using System;

namespace primerParcial;

    class Program
    {
        static void Main(string[] args)
        {
            SoporteBoleto t1 = new SoporteBoleto("Pantalla azul", Prioridad.Alta);    // Prioridad 3
            SoporteBoleto t2 = new SoporteBoleto("Mouse sucio", Prioridad.Baja);      // Prioridad 1
            SoporteBoleto t3 = new SoporteBoleto("Servidor caído", Prioridad.Alta);   // Prioridad 3
            SoporteBoleto t4 = new SoporteBoleto("Actualizar Software", Prioridad.Media);// Prioridad 2
            
            t3.Atender(); 

            
            Contenedor bandeja = new Contenedor(new SoporteBoleto[] { t1, t2, t3, t4 });

            Console.WriteLine("\n--- Organizando por Prioridad ---");
            bandeja.Organizar(); 

            Console.WriteLine("--- Tickets Pendientes ---");
            
            foreach (SoporteBoleto sp in bandeja)
            {
                Console.WriteLine($"[PENDIENTE] Prioridad: {sp.NivelPrioridad} | {sp.Problema}");
            }

            Console.ReadLine();
        }
    }
