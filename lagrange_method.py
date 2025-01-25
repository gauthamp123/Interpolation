class LagrangeEstimator:
    '''
        Class for interpolating a function using the Lagrange Interpolation
        Args:
            x_vals (list): List of inputs
            y_vals (list): List of corresponding outputs
    '''
    def __init__(self, x_vals, y_vals):
        self.x_vals = x_vals
        self.y_vals = y_vals
    
    def lagrange_divided_differences(self, i):
        '''
            Function for getting the coefficient for the current iteration of the Lagrange polynomial

            Args:
                i (int): Current iteration

            Return: float
        '''
        product = 1

        for j in range(0, len(self.x_vals)):
            if i == j:
                continue
            product = product * (self.x_vals[i] - self.x_vals[j])
        
        return self.y_vals[i]/product

    def nested_multiplication_lagrange(self, i, x):
        '''
            Function computing the interpolation by computing products at each iteration
            
            Args:
                x (float): Value to interpolate
                i (int): Current iteration

            Return: float
        '''
        product = 1
        
        for j in range(0, len(self.x_vals)):
            if i == j:
                continue
            product = product * (x - self.x_vals[j])
        
        return product

    def get_lagrange_estimate(self, x):
        '''
            Function getting the estimate of a value x

            Return: float
        '''
        final_estimate = 0.0
        
        for i in range(0, len(self.x_vals)):
            product_1 = self.nested_multiplication_lagrange(i, x)
            product_2 = self.lagrange_divided_differences(i)

            final_estimate += product_1*product_2
        
        return final_estimate