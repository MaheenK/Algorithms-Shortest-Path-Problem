
import sys
import time
import numpy as np
import matplotlib.pyplot as plt 


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)
# g = Graph(5000)
# g.graph = np.random.randint(5, size=(5000, 5000))
# g.dijkstra(0)
# while True:
#     try:
#         start_time = time.time()
#         g.dijkstra(0)
#         end_time = time.time()
#         print("Total time = ", end_time - start_time)
#         break
#     except:
#         pass

# # Values of x and y are plotted after testing each case
# # x-axis values
# x = [25, 50, 100, 500, 1000, 2000, 3000, 4000, 5000]
# # # y-axis values
# y = [0.013002634048461914, 0.03902769088745117, 0.11808395385742188, 1.317941665649414, 
# 4.752390623092651,28.34447145462036, 69.9988374710083, 124.48891639709473, 146.03596019744873]
x = [25, 50, 100, 150, 200]
y = [0.013002634048461914, 0.03902769088745117, 0.11808395385742188, 0.24017548561096191, 0.32923436164855957]

# plotting points as a scatter plot
plt.plot(x, y, label="Time Taken Per n Vertices", color="red",
         marker="*")

# y-axis label
plt.ylabel('Time Taken By Dijkstra (in seconds)')
# x-axis label
plt.xlabel('Number of Vertices In The Graph')
# plot title
plt.title('Dijkstra Algorithm - Time Analysis')
# showing legend
plt.legend()

# function to show the plot
plt.show()
