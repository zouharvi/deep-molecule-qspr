#!/bin/python3

import torch
import torch.nn as nn
import numpy as np
from collections import OrderedDict

class RMSELoss(torch.nn.Module):
    def __init__(self):
        super(RMSELoss,self).__init__()

    def forward(self,x,y):
        criterion = nn.MSELoss()
        loss = torch.sqrt(criterion(x, y))
        return loss

class Model(nn.Module):
    def __init__(self, params):
        super().__init__()
        params = [tok.strip().split('-') for tok in params.split(',')]
        layers = []
        for param in params:
            if param[0] == 'l':
                layers.append(nn.Linear(int(param[1]), int(param[2])))

        self.layers = nn.Sequential(*layers)
        self.train(False)

    def forward(self, x):
        return self.layers(x)

    def fit(self, dataTrainX, dataTrainY, epochs=5):
        self.train(True)
        loss_fn = RMSELoss()
        opt = torch.optim.SGD(model.parameters(), lr=0.2)
        for epoch in range(epochs):
            pred = model(dataTrainX).reshape(-1)
            loss = loss_fn(pred, dataTrainY) 
            loss.backward()
            opt.step()
            opt.zero_grad()
            
            print(f'e{epoch:>2} | Train Loss: {loss.item()}')
        self.train(False)



dataTrain = torch.Tensor([[1, 2, 3, 6], [2, -1, 1, 2], [0, 0, 1, 1]])
dataTrainX = dataTrain[:, :3]
dataTrainY = dataTrain[:, 3]
print(dataTrainX.shape)
print(dataTrainY.shape)


model = Model("l-3-1")
model.fit(dataTrainX, dataTrainY, epochs=5)