import unittest

import cambiaTexto

class ProbarCambiaTexto(unittest.TestCase):
    def testMayusculas(self):
        palabra = "Buenas mis perros"
        resultado = cambiaTexto.todoMayusculas(palabra)
        self.assertEqual(resultado, "BUENAS MIS PERROS")

if __name__ == "__main__":
    unittest.main()