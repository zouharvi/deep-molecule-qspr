#!/bin/python3

import torch
import torch.nn as nn
import math
import torch.utils.data as tudata
import numpy as np
from collections import OrderedDict


class RMSELoss(torch.nn.Module):
    def __init__(self):
        super(RMSELoss, self).__init__()

    def forward(self, x, y):
        criterion = nn.MSELoss()
        loss = torch.sqrt(criterion(x, y))
        return loss


class Model(nn.Module):
    def __init__(self, params):
        super().__init__()
        params = [tok.strip().split('-') for tok in params.split(',')]
        layers = []
        for param_i, param in enumerate(params):
            if param[0] == 'L':
                layers.append(
                    nn.Linear(int(param[1]), int(param[2]), bias=True))
            if param[0] == 'D':
                layers.append(nn.Dropout(float(param[1])))
            if param_i != len(params):
                layers.append(nn.LeakyReLU())

        self.layers = nn.Sequential(*layers)
        self.train(False)

    def forward(self, x):
        return self.layers(x)

    def fit(self, dataTrain, dataValid, epochs, feature_names=None):
        self.train(True)
        loss_fn = torch.nn.MSELoss()
        opt = torch.optim.Adam(self.parameters(), lr=0.5)

        for epoch in range(epochs):
            self.train(True)

            pred = self(dataTrain[0]).reshape(-1)
            lossTrain = loss_fn(pred, dataTrain[1])
            lossTrain.backward()
            opt.step()
            opt.zero_grad()

            if epoch % 50 == 0:
                self.eval()
                pred = self(dataValid[0]).reshape(-1)
                lossValid = loss_fn(pred, dataValid[1])
                if feature_names is not None:
                    parameters = list(self.parameters())
                    first_layer = list(parameters[0].data[0]) + [parameters[1].data[0]]
                    # print(len(parameters[1].data[0]))
                    for val, name in zip(first_layer, list(feature_names) + ['bias']):
                        print(f'{name:>10}: {val:5.3f}')
                    print('---')
                print(f'e{epoch:<9}:', end='')
                print(f'{math.sqrt(lossTrain.item()):>7.3f} | {math.sqrt(lossValid.item()):>7.3f}')
        self.train(False)
