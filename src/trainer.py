#!/bin/python3

from model import Model
import argparse
import numpy as np
import torch
import torch.utils.data as tudata
import pickle
import random

TEST_COUNT = 200

parser = argparse.ArgumentParser(description='Molecules.')
parser.add_argument('model_params', help='Model parameters')
parser.add_argument('--dataX', default='data/treesX.pickle', help='Features')
parser.add_argument('--dataY', default='data/treesY.pickle', help='Predictions')
parser.add_argument('--epochs', default=50, type=int, help='Number of epochs')
args = parser.parse_args()

torch.manual_seed(0)
random_rows = torch.randperm(2776)

with open(args.dataY, 'rb') as f:
    dataTrainY = torch.Tensor(pickle.load(f))

with open(args.dataX, 'rb') as f:
    dataTrainX = torch.transpose(torch.Tensor(pickle.load(f)), 0, 1)

print(dataTrainY.shape)
print(dataTrainX.shape)
print(dataTrainX[0])

dataTrainX = dataTrainX[random_rows]
dataTrainY = dataTrainY[random_rows]
dataTestX = dataTrainX[:TEST_COUNT]
dataTestY = dataTrainY[:TEST_COUNT]
dataValidX = dataTrainX[TEST_COUNT:2*TEST_COUNT]
dataValidY = dataTrainY[TEST_COUNT:2*TEST_COUNT]
dataTrainX = dataTrainX[2*TEST_COUNT:]
dataTrainY = dataTrainY[2*TEST_COUNT:]
print('Test', dataTestX.shape, dataTestY.shape)
print('Valid', dataValidX.shape, dataValidY.shape)
print('Train', dataTrainX.shape, dataTrainY.shape)

model = Model(args.model_params)

# dataTrainX = torch.Tensor([[1,2,3], [-5, 4, 1], [-1,-2,-3]])
# dataTrainY = torch.Tensor([7, 9, -7])
# dataValidX = torch.Tensor([[90,0,1], [1, 2, -1]])
# dataValidY = torch.Tensor([1, 3])

# dataTrainX = torch.Tensor([[1,2,3], [-5, 4, 1]])
# dataTrainY = torch.Tensor([7, 9])
# dataValidX = torch.Tensor([[1, 2, 3]])
# dataValidY = torch.Tensor([7])

model.fit((dataTrainX, dataTrainY), (dataValidX, dataValidY), epochs=args.epochs)