import unittest
from graphi import Graf

class TestGraf(unittest.TestCase):

    def setUp(self):
        self.graf = Graf()
        for v in ['A', 'B', 'C', 'D', 'E', 'F']:
            self.graf.dobavit_vershinu(v)
        self.graf.dobavit_rebro('A', 'D')
        self.graf.dobavit_rebro('B', 'D')
        self.graf.dobavit_rebro('C', 'E')
        self.graf.dobavit_rebro('D', 'F')
        self.graf.dobavit_rebro('E', 'F')

    def test_topologicheskaya_sortirovka(self):
        result = self.graf.topologicheskaya_sortirovka()
        self.assertIsNotNone(result)
        self.assertLess(result.index('C'), result.index('E'))
        self.assertLess(result.index('A'), result.index('D'))
        self.assertLess(result.index('B'), result.index('D'))
        self.assertLess(result.index('D'), result.index('F'))
        self.assertLess(result.index('E'), result.index('F'))

    def test_dobavit_vershinu(self):
        self.graf.dobavit_vershinu('G')
        self.assertIn('G', self.graf.smezhnost)

    def test_dobavit_rebro(self):
        self.graf.dobavit_rebro('A', 'E')
        self.assertIn('E', self.graf.smezhnost['A'])

if __name__ == '__main__':
    unittest.main()
