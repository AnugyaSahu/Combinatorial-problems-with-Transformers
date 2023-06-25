import shutil
import numpy as np

def extract_tar_gz(tar_gz_path, extract_path):
    shutil.unpack_archive(tar_gz_path, extract_path, "gztar")

test = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\Datasets\tsp_unif_test.tar.gz"
train = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\Datasets\tsp_unif_training.tar.gz"

extract_path = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\TSP instances"


extract_tar_gz(test, extract_path)
extract_tar_gz(train, extract_path)

def read_coordinates_from_file(file_path):
    coordinates = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                except(ValueError):
                    continue
                coordinates.append((x, y))
    return coordinates

file_path_test_50 = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\TSP instances\tsp_unif_test50_100_100000.txt"
file_path_train_50 = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\TSP instances\tsp_unif50_10000_100000_1000.txt"
file_path_test_100 = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\TSP instances\tsp_unif_test100_100_100000.txt"
file_path_train_100 = r"C:\Users\anshu\OneDrive\Desktop\FAU\Project\TSP instances\tsp_unif100_10000_100000_1000.txt"

coordinates_test50 = read_coordinates_from_file(file_path_test_50)
test50 = np.array(coordinates_test50)
coordinates_train50 = read_coordinates_from_file(file_path_train_50)
train50 = np.array(coordinates_train50)
coordinates_test100 = read_coordinates_from_file(file_path_test_100)
test100 = np.array(coordinates_test100)
coordinates_train100 = read_coordinates_from_file(file_path_train_100)
train100 = np.array(coordinates_train100)

print(test50.shape, train50.shape, test100.shape, train100.shape)

testinstances50 = []
for i in range(0, 5000, 50):
    testinstances50.append(test50[i:i+50, :])
testinstances50 = np.array(testinstances50)
optimal_distances_test50 = []
for i in range(testinstances50.shape[0]):
    distance = 0
    for j in range(testinstances50.shape[1]-1):
        distance += np.linalg.norm(testinstances50[i][j] -  testinstances50[i][j+1])
    optimal_distances_test50.append(distance)
optimal_distances_test50 = np.array(optimal_distances_test50)

traininstances50 = []
for i in range(0, 1500000, 50):
    traininstances50.append(train50[i:i+50, :])
traininstances50 = np.array(traininstances50)
optimal_distances_train50 = []
for i in range(traininstances50.shape[0]):
    distance = 0
    for j in range(traininstances50.shape[1]-1):
        distance += np.linalg.norm(traininstances50[i][j] -  traininstances50[i][j+1])
    optimal_distances_train50.append(distance)
optimal_distances_train50 = np.array(optimal_distances_train50)

testinstances100 = []
for i in range(0, 10000, 100):
    testinstances100.append(test100[i:i+100, :])
testinstances100 = np.array(testinstances100)
optimal_distances_test100 = []
for i in range(testinstances100.shape[0]):
    distance = 0
    for j in range(testinstances100.shape[1]-1):
        distance += np.linalg.norm(testinstances100[i][j] -  testinstances100[i][j+1])
    optimal_distances_test100.append(distance)
optimal_distances_test100 = np.array(optimal_distances_test100)

traininstances100 = []
for i in range(0, 1000000, 100):
    traininstances100.append(train100[i:i+100, :])
traininstances100 = np.array(traininstances100)
optimal_distances_train100 = []
for i in range(traininstances100.shape[0]):
    distance = 0
    for j in range(traininstances100.shape[1]-1):
        distance += np.linalg.norm(traininstances100[i][j] -  traininstances100[i][j+1])
    optimal_distances_train100.append(distance)
optimal_distances_train100 = np.array(optimal_distances_train100)

