import unittest

from pieza import Pieza


class TestPieza(unittest.TestCase):
    def test_crear_pieza(self):
        pieza = Pieza("Alfil")
        self.assertEqual(pieza.__nombre__, "Alfil")


if __name__ == '__main__':
    unittest.main()