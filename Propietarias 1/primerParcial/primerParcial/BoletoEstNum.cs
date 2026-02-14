using System.Collections;

namespace primerParcial;

public class BoletoEstNum : IEnumerator
{
    private SoporteBoleto[] _lista;
    private int _posicion = -1;

    public BoletoEstNum(SoporteBoleto[] lista)
    {
        _lista = lista;
    }
    public bool MoveNext()
    {
        _posicion++;
        while (_posicion < _lista.Length && !_lista[_posicion].estadoBoleto)
        {
            _posicion++;
        }
        return (_posicion < _lista.Length);
    }

    public void Reset()
    {
        _posicion = -1;
    }

    public object Current
    {
        get
        {
            if (_posicion < 0 || _posicion >= _lista.Length)
                throw new InvalidOperationException();
            return _lista[_posicion];
        }
    }
}