import numpy as np

class SGD_momentum_np:
    def __init__(self, alpha: float = 0.9) -> None:
        self.velocity = dict()
        self.alpha = alpha
        """
        alpha: default 0.9
        
        W(t+1) = W(t) + lr * V(t)
        
        V(t) = a * V(t-1) - cost
        
        """
    def update_grad(self, layer_name:str, layer, LR:float, have_db:bool):
        """

        Args:
            layer_name (str): _description_
            layer (_type_): layer(ex.)
            LR (float): Learning rate
            have_db (bool): layer에 dW외에 db가 있는지 유무, default=True
        """
        ################## edit here ###################
        

        return layer
        ################################################

    def save_velocity(self,layer_name, layer, have_db):
        
        ################## edit here ###################
        

        pass
        ################################################