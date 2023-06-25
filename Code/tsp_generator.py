'''
    File name: tsp_generator.py
    Author: shirgur
    Source: https://github.com/shirgur/PointerNet
    Python Version: 3.10
    Description: Generates random TSP Problems.
'''

import sys
import os
import numpy as np
from tqdm import tqdm

import tsp_solvers


class TSPGenerator:
    """Generates random TSP datasets."""

    def __init__(self, 
                 save_path: str,
                 data_size: int, 
                 seq_len: int, 
                 solver = None, 
                 solve_percentage: float = 0.):
        """Initiate the TSP Generator.
        
        Args:
            save_path (str): Path to the dataset.
            data_size (int): Number of TSP problems.
            seq_len (int): Number of points for each TSP problem.
            solver (function): Solver that can solve TSP problems.
            solve_percentage (float): How many of the generated data need a solution?
        """
        # check path
        os.makedirs(save_path, exist_ok=True)
        if len(os.listdir(save_path)) > 0:
            raise Exception(f'{save_path} not empty!')

        # set stuff
        self.rnd_gen = np.random.default_rng(1111)
        self.data_size = data_size
        self.seq_len = seq_len
        self.save_path = save_path
        self.solve = None
        self.data = self._generate_data()

        # solve part of the data
        if solve_percentage > 0. and solver is not None:
            data_idx = list(range(len(self.data)))
            self.data_solve_idx = self.rnd_gen.choice(data_idx, size=int(solve_percentage*len(self.data)), replace=False)
            # sort idx
            self.data_solve_idx = np.sort(self.data_solve_idx)

            # solve
            data_solve = self.data[self.data_solve_idx]
            self.solve, self.solve_cost = self._solve_data(data_solve, solver)

        self._save_data()

    def _save_data(self):
        """Saves data to dir"""
        np.save(os.path.join(self.save_path, 'tsp_data'), self.data)
        if self.solve is not None:
            np.save(os.path.join(self.save_path, 'tsp_solved_data_idx'), self.data_solve_idx)
            np.save(os.path.join(self.save_path, 'tsp_solution'), self.solve)
            np.save(os.path.join(self.save_path, 'tsp_sol_cost'), self.solve_cost)

    def _generate_data(self) -> np.array:
        """Generate data for the TSP problem, randomly.

        Returns:
            points_list: List of points.
        """
        points_list = []

        data_iter = tqdm(range(self.data_size), unit='tsp problems')

        for i, _ in enumerate(data_iter):
            data_iter.set_description('Data size %i/%i' % (i+1, self.data_size))
            points_list.append(self.rnd_gen.random((self.seq_len, 2)))

        return np.array(points_list)

    def _solve_data(self, data: np.array, solver) -> np.array:
        """Solve given data.

        Args:
            data (array): Data to solve.
            solver (function): Solver.

        Returns:
            solution_idx: Correct order of a found solution.
        """
        solution_idx, solution_cost = [], []

        data_iter = tqdm(data, unit='solved tsp problems')

        for i, sequence in enumerate(data_iter):
            data_iter.set_description('Data size %i/%i' % (i+1, self.data_size))
            best_route = solver(sequence)

            # unpack tuple
            if len(best_route) == 2: 
                best_route, _ = best_route

            best_costs = self._calc_costs_of_path(sequence[best_route])

            solution_idx.append(best_route)
            solution_cost.append(best_costs)

        return solution_idx, solution_cost

    def _calc_costs_of_path(self, sorting: np.array) -> float:
        """Computate TSP path costs for current sorting.
        
        Args:
            sorting (Tensor): Current sorting.

        Returns:
            path costs per batch
        """
        a_points = np.concatenate([sorting[1:], sorting[0:1]], axis=0)
        b_points = sorting[:, :]
        gen_cost = a_points - b_points

        return np.sqrt(np.power(gen_cost, 2).sum(1)).sum(0)

print('Create Val Set')
test_gen = TSPGenerator('TSP-5-opt_Dataset/val/', 100, 5, tsp_solvers.tsp_opt, 1.)
print(test_gen.data_size, test_gen.seq_len)
print('Create Test Set')
test_gen = TSPGenerator('TSP-5-opt_Dataset/test/', 1000, 5, tsp_solvers.tsp_opt, 1.)
print(test_gen.data_size, test_gen.seq_len)
print('Create Train Set')
test_gen = TSPGenerator('TSP-5-opt_Dataset/train/', 10000, 5, tsp_solvers.tsp_opt, 1.)
print(test_gen.data_size, test_gen.seq_len)
