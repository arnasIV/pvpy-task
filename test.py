import unittest
import numpy as np
from cell_power import calculate_total_power, element_power_ratio

class EnergyPowerTest(unittest.TestCase): 
  
    # Testing with data provided in the task 
    def test_sample_case(self):    
        mat = [[1, 0, 0], 
               [1, 1, 0], 
               [1, 1, 1]]
        A = element_power_ratio(mat, 0, 0)
        self.assertEqual(A, 1.15 * 1.15)

        B = element_power_ratio(mat, 1, 0)
        self.assertEqual(B, 1.1 * 1.08 * 1.15)
 
        C = element_power_ratio(mat, 1, 1)
        self.assertEqual(C, 1.12 * 1.15)

        D = element_power_ratio(mat, 2, 0)
        self.assertEqual(D, 1.1 * 1.1 * 1.08 * 1.08)

        E = element_power_ratio(mat, 2, 1)
        self.assertEqual(E, 1.1 * 1.08 * 1.12)

        F = element_power_ratio(mat, 2, 2)
        self.assertEqual(F, 1.12 * 1.12)

        tot_r = A + B + C + D + E + F
        init_power = 100
        
        tot_power = calculate_total_power(mat, init_power) 
        self.assertEqual(tot_power, tot_r * init_power)

      
    def test_case1(self):    
        mat = [[1, 0, 1], 
               [0, 1, 0], 
               [1, 0, 1]]
        A = element_power_ratio(mat, 0, 0)
        self.assertEqual(A, 1)

        B = element_power_ratio(mat, 0, 2)
        self.assertEqual(B, 1)
 
        C = element_power_ratio(mat, 1, 1)
        self.assertEqual(C, 1)

        D = element_power_ratio(mat, 2, 0)
        self.assertEqual(D, 1)

        E = element_power_ratio(mat, 2, 2)
        self.assertEqual(E, 1)

        tot_r = A + B + C + D + E
        init_power = 55.87
        
        tot_power = calculate_total_power(mat, init_power) 
        self.assertEqual(tot_power, tot_r * init_power)

    def test_case2(self):    
        mat = np.zeros(shape=(1, 100)) + 1
        tot_r = 0
        for i in range(len(mat[0])):
            X = element_power_ratio(mat, 0, i)
            ratio = pow(1.08, len(mat[0]) - 1 - i) * pow(1.12, i)
            self.assertAlmostEqual(X, ratio, places=4)
            tot_r += ratio

        init_power = 10.0
        
        tot_power = calculate_total_power(mat, init_power) 
        self.assertAlmostEqual(tot_power, tot_r * init_power, places=4)

    def test_case3(self):    
        mat = np.zeros(shape=(1, 100)) + 1
        mat = mat.transpose()
        tot_r = 0
        for i in range(len(mat)):
            Y = element_power_ratio(mat, i, 0)
            ratio = pow(1.15, len(mat) - 1 - i) * pow(1.1, i)
            self.assertAlmostEqual(Y, ratio, places=4)
            tot_r += ratio

        init_power = 10.0
        
        tot_power = calculate_total_power(mat, init_power) 
        self.assertAlmostEqual(tot_power, tot_r * init_power, places=4)
        
  
if __name__ == '__main__': 
    unittest.main() 
