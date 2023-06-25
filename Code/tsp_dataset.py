'''
    File name: tsp_data_generator.py
    Author: shirgur
    Source: https://github.com/shirgur/PointerNet
    Python Version: 3.10
    Description: Loads the TSP Problems.
'''

import os
import numpy as np
import torch
from torch.utils.data import Dataset


class TSPDataset(Dataset):
    """TSP dataset."""

    def __init__(self, path: str, set_size: int = None):
        """Initiate the TSP Dataset.
        
        Args:
            path (str): Path to the saved data.
            set_size (int): Max. number of data that should be used.
        """
        # check path
        if not os.path.exists(path) or len(os.listdir(path)) == 0:
            raise Exception(f'{path} does not exists or is empty!')

        loaded_tuple = self._load_data(path)

        # pick subset
        if set_size is not None and set_size > 0 and set_size < len(loaded_tuple[0]):
            set_idx = np.random.randint(0, len(loaded_tuple[0]), set_size)
            loaded_tuple = [tup[set_idx] for tup in loaded_tuple]
        
        # get data
        self.data = loaded_tuple[0]
        self.data_size = len(self.data)
        self.seq_len = self.data.shape[1]
        self.solved_data_idx = []
        
        if len(loaded_tuple) > 1:
            self.solved_data_idx, self.solutions, self.costs = list(loaded_tuple[1]), loaded_tuple[2], loaded_tuple[3]

        if set_size == self.data_size:
            # assume everything is solved (TSP)
            self.solved_data_idx = list(range(set_size))

    def _load_data(self, path: str) -> tuple:
        """Load data from path.
        
        Args:
            path (str): Path to the saved data.

        Returns:
            tuple: data, (solved_data_idx, solutions)
        """
        data = np.load(os.path.join(path, 'tsp_data.npy'))

        if os.path.exists(os.path.join(path, 'tsp_solution.npy')):
            solved_data_idx = np.load(os.path.join(path, 'tsp_solved_data_idx.npy'))
            solutions = np.load(os.path.join(path, 'tsp_solution.npy'))
            costs = np.load(os.path.join(path, 'tsp_sol_cost.npy'))
            return (data, solved_data_idx, solutions, costs)
        
        return (data,)

    def __len__(self):
        return self.data_size

    def __getitem__(self, idx: int):
        tensor = torch.from_numpy(self.data[idx]).to(torch.float64)
        res_sol, costs_sol = None, None

        if idx in self.solved_data_idx:
            # solution available
            solved_idx = self.solved_data_idx.index(idx)
            res_sol = torch.from_numpy(self.solutions[solved_idx]).to(torch.int64)
            costs_sol = self.costs[solved_idx]

        return {'Points': tensor, 'Solution': res_sol, 'Costs': costs_sol}
