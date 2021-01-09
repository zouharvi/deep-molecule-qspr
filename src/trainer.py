#!/bin/python3

from model import Model
import argparse
import numpy as np
import torch
import torch.utils.data as tudata
import pickle
import random

torch.manual_seed(0)
TEST_COUNT = 200

parser = argparse.ArgumentParser(description='Molecules.')
parser.add_argument('model_params', help='Model parameters')
parser.add_argument('--data', default='data/boil2.pickle')
parser.add_argument('-v', '--var', default='boiling_point')
parser.add_argument('--epochs', default=50, type=int, help='Number of epochs')
args = parser.parse_args()


with open(args.data, 'rb') as f:
    data = pickle.load(f)
    dataTrainY = torch.Tensor(data.pop(args.var))
    dataTrainX = torch.transpose(torch.Tensor(list(data.values())), 0, 1)

print(dataTrainY.shape)
print(dataTrainX.shape)
print(dataTrainX[0])
random_rows = torch.randperm(len(dataTrainY))

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

model.fit((dataTrainX, dataTrainY),
          (dataValidX, dataValidY), epochs=args.epochs)
