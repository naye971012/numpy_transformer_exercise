from typing import Any
import numpy as np
import torch
import torch.nn as nn
import sys
import os

############## this block is just for import moudles ######
current_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)
###########################################################

from torch_models.activations.relu import Relu_th
from numpy_models.activations.relu import Relu_np

from torch_models.activations.sigmoid import Sigmoid_th
from numpy_models.activations.sigmoid import Sigmoid_np

from torch_models.losses.binary_ce import Binary_Cross_Entropy_th
from numpy_models.losses.binary_ce import Binary_Cross_Entropy_np

from torch_models.commons.linear import Linear_th
from numpy_models.commons.linear import Linear_np

from numpy_models.losses.ce import Cross_Entropy_np

from numpy_models.commons.cnn import Conv2d_np

class linear_model_th(nn.Module):
    def __init__(self, input_channel=28*28, output_channel=10) -> None:
        super().__init__()
        
        self.linear_1 = Linear_th(input_channel , 256)
        self.linear_2 = Linear_th(256, 128)
        self.linear_3 = Linear_th(128, output_channel)
        self.activation_1 = Relu_th()
        self.activation_2 = Relu_th()
        self.sigmoid = Sigmoid_th()
        
        
    def forward(self,x):
        #make x flatten [# of batch, 28*28 ]
        batch_size = x.size()[0]
        x = x.view(batch_size,-1)
        
        x = self.linear_1(x)
        x = self.activation_1(x)
        x = self.linear_2(x)
        x = self.activation_2(x)
        x = self.linear_3(x)
        x = self.sigmoid(x)
        
        return x

class linear_model_np():
    def __init__(self, input_channel=28*28, output_channel=10) -> None:
        
        self.linear_1 = Linear_np(input_channel , 256)
        self.linear_2 = Linear_np(256, 128)
        self.linear_3 = Linear_np(128, output_channel)
        self.activation_1 = Relu_np()
        self.activation_2 = Relu_np()
        self.sigmoid = Sigmoid_np()
        
        self.criterion = Cross_Entropy_np()
        
    def forward(self,x):
        
        #make x flatten [# of batch, 28*28 ]
            ######################   edit here   ##############################
            
            
            
            
            
            pass
            ###################################################################
    
    def loss(self,x,y):
            ######################   edit here   ##############################
            
            
            
            
            
            pass
            ###################################################################
    
    
    def backward(self):
            ######################   edit here   ##############################
            
            
            
            
            
            pass
            ###################################################################
    
    def update_grad(self, learning_rate, batch_size):
            ######################   edit here   ##############################
            
            
            
            
            
            pass
            ###################################################################    

class cnn_model_th(nn.Module):
    def __init__(self, input_channel=28*28, output_channel=10) -> None:
        super().__init__()
        
        self.cnn_1 = nn.Conv2d(1 , 8, kernel_size=(3,3), stride=(1,1),padding=(1,1)) #28,28 -> 28,28
        self.pooling1 = nn.MaxPool2d(kernel_size=(2,2), stride=(2,2)) #28,28 -> 14,14
        self.cnn_2 = nn.Conv2d(8 , 12, kernel_size=(3,3), stride=(1,1),padding=(1,1)) #14,14 -> 14,14
        self.pooling2 = nn.MaxPool2d(kernel_size=(2,2), stride=(2,2)) #14,14 -> 7.7
        
        self.linear1 = Linear_th( 7*7*12 , 300)
        self.linear2 = Linear_th(300, output_channel)
        
        self.activation_1 = Relu_th()
        self.activation_2 = Relu_th()
        self.activation_3 = Relu_th()
        self.sigmoid = Sigmoid_th()
        
    
    def forward(self,x):
        #change [# of batch, channel, x_shape, y_shape]
        batch_size = x.size()[0]
        x = x.view(-1,1,28,28)
        
        #cnn part
        x = self.cnn_1(x)
        x = self.activation_1(x)
        x = self.pooling1(x)
        x = self.cnn_2(x)
        x = self.activation_2(x)
        x = self.pooling2(x)
        
        #flatten
        x = x.view(batch_size, -1)
        
        #linear part
        x = self.linear1(x)
        x = self.activation_3(x)
        x = self.linear2(x)
        x = self.sigmoid(x)
        
        return x

class cnn_model_np():
    def __init__(self, input_channel=28*28, output_channel=10) -> None:
            ######################   edit here   ##############################
            
            
            
            
            
            pass
            ###################################################################
        
    def forward(self,x):
            ######################   edit here   ##############################
            
            
            
            
            
            pass
            ###################################################################
    
    def loss(self,x,y):
            ######################   edit here   ##############################
            
            
            
            
            
            pass
            ###################################################################
    
    
    def backward(self):
            ######################   edit here   ##############################
            
            
            
            
            
            pass
            ###################################################################
    
    def update_grad(self, learning_rate, batch_size):
            ######################   edit here   ##############################
            
            
            
            
            
            pass
            ###################################################################