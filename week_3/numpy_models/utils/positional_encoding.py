import numpy as np

def positional_encoding(max_position:int, d_model:int, min_freq:int=1e-4) -> np.array:
        
        ################## edit here ###################
        

        pass
        ################################################

class Embedding_with_positional_encoding_np:
    def __init__(self, num_emb:int, num_dim:int) -> None:
        self.num_emb = num_emb
        self.num_dim = num_dim
        
        self.forward_input = None
        self.pos_enc = positional_encoding(num_emb,num_dim)
        
        limit = np.sqrt(2 / float(num_dim))
        self.W = np.random.normal(0.0, limit, size=(num_emb,num_dim))

    def forward(self,x:np.array) -> np.array:
        """

        Args:
            x (np.array[int]): [# of batch, # of vocab(int) ]

        Returns:
            np.array: [# of batch, # of vocab, embedding_dim ]
        """
        
        ################## edit here ###################
        

        pass
        ################################################
        
    def backward(self,d_prev:np.array) -> np.array:
        """

        self.W = [# of embedding , embedding_dim]
        
        Args:
            d_prev (np.array): [# of batch, # of vocab, embedding_dim]

        Returns:
            np.array: _description_
        """
        ################## edit here ###################
        

        pass
        ################################################
    
    def __call__(self,x):
        return self.forward(x)

if __name__=="__main__":
    
    model = Embedding_with_positional_encoding_np(10,20)
    x = np.random.randint(0,9, size=(1,5))
    output = model(x)
    model.backward(output)

    """
    import matplotlib.pyplot as plt
    ### Plotting ####
    d_model = 128
    max_pos = 256
    mat = positional_encoding(max_pos, d_model)
    plt.pcolormesh(mat, cmap='copper')
    plt.xlabel('Depth')
    plt.xlim((0, d_model))
    plt.ylabel('Position')
    plt.title("PE matrix heat map")
    plt.colorbar()
    plt.show()
    """