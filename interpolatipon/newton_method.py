

class NewtonEstimator:
    '''
        Class for interpolating a function using Newton's Polynomial
        Args:
            x_vals (list): List of inputs
            y_vals (list): List of corresponding outputs
    '''
    def __init__(self, x_vals, y_vals):
        self.x_vals = x_vals
        self.y_vals = y_vals



    def divided_difference(self):
        '''
            Function for getting the list of coefficients for the Newton polynomial

            Return: list
        '''
        if len(self.x_vals) != len(self.y_vals):
            return []
        if len(self.y_vals) == 1:
            return self.y_vals
        
        table = []
        n = len(self.x_vals)

        # Fill in first column in table
        table.append(self.x_vals)

        # Fill in second column in table
        table.append(self.y_vals)

        for i in range(2, len(self.x_vals)):
            new_row = []
            for j in range(0, len(self.y_vals)-i+1):
                val = (table[i-1][j+1] - table[i-1][j])/(table[0][i+j-1] - table[0][j])
                new_row.append(val)
            table.append(new_row)

        last_val = []
        val = (table[n-1][1] - table[n-1][0])/(table[0][n-1] - table[0][0])
        last_val.append(val)
        table.append(last_val)
        
        return [table[i][0] for i in range(1, n+1)]

    

    def nested_multiplication(self, coefficients, x):
        '''
            Function computing the interpolation by computing products at each iteration
            
            Args:
                coefficients (list): Coefficients computed by divided differences function
                x (float): Value to interpolate

            Return: float
        '''
        product = coefficients[0]
        for i in range(1, len(coefficients)):
            sub_product = coefficients[i]
            for j in range(0, i):
                sub_product = sub_product * (x - self.x_vals[j])
            product += sub_product
        
        return product
    
    def get_newton_estimate(self, x):
        '''
            Function getting the estimate of a value x

            Return: float
        '''
        coefficients = self.divided_difference()
        return self.nested_multiplication(coefficients, x)
