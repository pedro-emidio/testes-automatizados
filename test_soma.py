import unittest
from .soma import soma


class TestSoma(unittest.TestCase):
    def test_varias_entradas(self):
        x_y_saidas = (
            (10, 15, 25),
            (-10, 10, 0),
            (1.5, 1.5, 3),
            (-10, 15.5, 5.5)
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_verifica_se_x_e_int_ou_float_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('10', 6)


    def test_verifica_se_y_e_int_ou_float_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(10, '6')


if __name__ == '__main__':
    unittest.main(verbosity=True)
