import torch
import os
os.system("screen python print((torch.rand(100000, 3).cuda()) * 2.0 - 1.0)")
