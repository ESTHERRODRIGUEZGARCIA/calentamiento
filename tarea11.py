import random
import seaborn as sns
import matplotlib.pyplot as plt

iterations = 1000
variables = ["work", "salary", "conditions", "career_advancement", "social impact", "job security", "life_balance", "location", "atmosphere", "travel"]

def Monte_Carlo(grade):
    final_results = []
    weight = [0.15, 0.09, 0.11, 0.12, 0.02, 0.11, 0.07, 0.1, 0.11]
    for n in range(iterations):
        results = []
        for i in range(len(variables)):
            value = weight[i] * (random.uniform(grade[i][0], grade [i][1]))
            results.append(value)

        final_results.append(sum(results))
    return final_results
a = Monte_Carlo([[4,9],[8.5,10],[5,9],[8.5,9.5],[3,7],[4,9],[3,8],[7.5,8],[5,9],[0,6]])
