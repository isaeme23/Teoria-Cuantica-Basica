import unittest
import observa as ob
import numpy as np


class TestExperiments(unittest.TestCase):

# Ejercicio 4.3.1
    def test_First(self):
        matrix = np.array([[0,1],[1,0]])
        state1 = [1,0]
        state2 = [0,1]
        self.assertEqual(ob.FinalState(state1,matrix), [0, 1])
        self.assertEqual(ob.FinalState(state2, matrix), [1, 0])

# Ejercicio 4.3.2
    def test_Second(self):
        matrix = np.array([[0, 1], [1, 0]])
        state1 = [1, 0]
        self.assertEqual(ob.EigenvectorsProbability(matrix,state1)[1], [0.4999999999999999, 0.4999999999999999])
        self.assertEqual(ob.ValueDistribution(matrix,state1), 0.0)

# Ejercicio 4.4.1
    def test_Third(self):
        matrix1 = np.array([[0,1], [1,0]])
        matrix2 = np.array([[(2**(1/2))/2, (2**(1/2))/2], [(2**(1/2))/2, -(2**(1/2))/2]])
        matrix = np.matmul(matrix1,matrix2)
        self.assertEqual(ob.VerifyUnitary(matrix), True)

# Ejercicio 4.4.2
    def test_Fourth(self):
        matrix = np.array([[0, 1/2**(1/2), 1/2**(1/2), 0],
                           [1j/2**(1/2), 0, 0, 1/2**(1/2)],
                           [1/2**(1/2), 0, 0, 1j/2**(1/2)],
                           [0, 1/2**(1/2), -(1/2**(1/2)), 0]])
        state = [1, 0, 0, 0]
        self.assertEqual(ob. FinalState(state, matrix), [0j, 0.7071067811865475j, (0.7071067811865475+0j), 0j])

if __name__ == '__main__':
    unittest.main()