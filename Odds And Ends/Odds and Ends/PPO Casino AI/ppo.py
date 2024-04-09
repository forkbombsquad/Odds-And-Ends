from collections import defaultdict

from collections import defaultdict

import matplotlib.pyplot as plt
import torch
from tensordict.nn import TensorDictModule
from tensordict.nn.distributions import NormalParamExtractor
from torch import nn
from torchrl.collectors import SyncDataCollector
from torchrl.data.replay_buffers import ReplayBuffer
from torchrl.data.replay_buffers.samplers import SamplerWithoutReplacement
from torchrl.data.replay_buffers.storages import LazyTensorStorage
from torchrl.envs import (Compose, DoubleToFloat, ObservationNorm, StepCounter, TransformedEnv)
from torchrl.envs.libs.gym import GymEnv
from torchrl.envs.utils import check_env_specs, set_exploration_mode
from torchrl.modules import ProbabilisticActor, TanhNormal, ValueOperator
from torchrl.objectives import ClipPPOLoss
from torchrl.objectives.value import GAE
from tqdm import tqdm

device = "cpu" if not torch.cuda.is_available() else "cuda:0"
numCells = 256 # number of cells in each layer i.e. output dim
lr = 3e-4
maxGradNorm = 1.0

frameSkip = 1
framesPerBatch = 1000 // frameSkip
# For complete training, need 1M frames
totalFrames = 50_000 // frameSkip

subBatchSize = 64 # cardinality of the sub samples gathered from teh current data in the inner loop
numEpochs = 10 # optimization steps per batch of data
clipEpsilon = (0.2) # clip value for PPO loss
gamma = 0.99
lmbda = 0.95
entropyEps = 1e-4

# Define Env
baseEnv = GymEnv("CasinoAI-v1", device=device, frame_skip=frameSkip)

env = TransformedEnv(baseEnv, Compose(ObservationNorm(in_keys=["observation"]), DoubleToFloat(in_keys=["observation"]), StepCounter(),),)
env.transform[0].init_stats(num_iter=1000, reduce_dim=0, cat_dim=0)

print("normalization constant shape:", env.transform[0].loc.shape)