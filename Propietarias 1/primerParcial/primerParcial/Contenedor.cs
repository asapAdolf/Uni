using System.Collections; 

namespace primerParcial
{
    public class Contenedor : IEnumerable
    {
        private SoporteBoleto[] _boletos;

        public Contenedor(SoporteBoleto[] boletos)
        {
            _boletos = boletos;
        }

        public void Organizar()
        {
            Array.Sort(_boletos); 
        }
        public IEnumerator GetEnumerator()
        {
            return new BoletoEstNum(_boletos);
        }
    }
}