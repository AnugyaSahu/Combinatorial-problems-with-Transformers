# Combinatorial-problems-with-Transformers
Solving complex real-world COPs with limited data / information and deep learning 
Here are some details about the project and what one can find in the report or repository.

1. Goal - Finding an optimal solution to Travelling Salesman Problem
2. TSP Instances - Contains data in form of coordinates as to show the positions of the cities
3. Input - Form of x and y coordinates
4. Output - Optimal cost or travelling from the starting city to the city at last, Optimal way of cities visited in order as a sequence.
5. Small introduction to different Combinatorial problems
6. Databases to find datasets for those COPs
7. As majority of datasets do not already have optimal solutions (the dataset we use have an optimal solution given) heuristic methods like Two-opt, City-swap, genetic, Simulated Annealing algorithms are taken into account to get a soution in order to compare the results of Pointer Networks with Transformers.
8. An explanation on Pointer Networks, Transformers Architecture and how both can be merged in order to get a working algorithm.
9. Conclusion - Transformers performed well in the training set but could not generalize well.
