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
parser.add_argument('--data', default='data/boil1.pickle')
parser.add_argument('-v', '--var', default='boiling_point')
parser.add_argument('--reveal', action='store_true', help='Reveal parameters')
parser.add_argument('--epochs', default=50, type=int, help='Number of epochs')
args = parser.parse_args()

with open(args.data, 'rb') as f:
    data = pickle.load(f)
    dataTrainY = torch.Tensor(data.pop(args.var))
    feature_names = data.keys()
    dataTrainX = torch.transpose(torch.Tensor(list(data.values())), 0, 1)

print(feature_names)
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

# dataTrainX = []
# dataTrainY = []
# for _ in range(100):
#     x = random.randint(0, 1000)
#     dataTrainX.append([x, x*x+5, 2])
#     dataTrainY.append(x+2*x*x+10)

# dataTrainX = torch.Tensor(dataTrainX)
# dataTrainY = torch.Tensor(dataTrainY)
# dataValidX = dataTrainX
# dataValidY = dataTrainY
# feature_names = ['a', 'b', 'c']

model.fit(
    (dataTrainX, dataTrainY),
    (dataValidX, dataValidY),
    epochs=args.epochs,
    feature_names=feature_names if args.reveal else None)