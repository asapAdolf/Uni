namespace primerParcial;
    public class SoporteBoleto : IBoleto, IComparable
    {
        public string Problema { get; set; }
        public Prioridad NivelPrioridad { get; set; }
        public bool estadoBoleto { get; set; }

        public SoporteBoleto(string problema, Prioridad p)
        {
            Problema = problema;
            NivelPrioridad = p;
        }

        public void Atender()
        {
            Console.WriteLine("--Operando--");
            estadoBoleto = false; 
        }
        
        public int CompareTo(object obj)
        {
            SoporteBoleto sigBol = obj as SoporteBoleto;
            if (sigBol == null) return 1;
            
            return sigBol.NivelPrioridad.CompareTo(this.NivelPrioridad);
        }
    }
