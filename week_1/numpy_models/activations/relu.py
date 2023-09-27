import numpy as np


class Relu_np():
    def __init__(self) -> None:
        self.output = None # save output
        self.grad = None # save gradient
        
        self.d_zeros = None # save utils which needs when backward
        
    def forward(self,x):
        """
        Args:
            x (np.array): [batch, ... ]

        Returns:
            np.array: [batch, ... ] 
        """
        ####################### edit here ###################
        
        
        return
        #####################################################
        self.output=x
        return x
    
    def backward(self, d_prev):
        """
        backward:
            output -> d_relu -> grad
        
        """
        ####################### edit here ###################
    
    
        return
        #####################################################
        self.grad = output
        return self.grad
    
    def __call__(self,x):
        return self.forward(x)