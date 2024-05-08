"""
Problem:
Count the number of islands in a 2d matrix of boolean values (0 and 1)

Islands are defined as any adjacent 1s.
Adjacent is defined as a distance of 1 in any direction, including diagonally

Solution overview: Can be solved using either DFS or BFS
DFS is slightly more intuitive but Auxiliary Space is larger.

Where n and m are rows/columns-
DFS:
Time complexity: O(n * m)
Space complexity: worst case O(n * m) if each value is a 1 as the call stack will grow to each cell in the graph

BFS:
Time complexity: O(n * m)
Space complexity: O(min(n,m)) as the queue will grow to the size of whichever is smaller between n and m before you start popping things off

"""
import collections
import enum
import pprint


class SearchStrategy(enum.Enum):
    DFS = 0
    BFS = 1


# Program to count islands in boolean 2D matrix
class Graph:
    # These arrays are used to get row and
    # column numbers of 8 neighbours
    # of a given cell
    row_nbr = [-1, -1, -1,  0, 0,  1, 1, 1]
    col_nbr = [-1,  0,  1, -1, 1, -1, 0, 1]



    def __init__(self, g: list[list[int]]):
        self.ROW = len(graph)
        self.COL = len(graph[0])
        self.graph = g

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def is_safe(self, i: int, j: int, visited: list[list[int]]) -> bool:
        # row number is in range, column number
        # is in range and value is 1 (meaning it's land)
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])
              

    def dfs(self, i: int, j: int, visited: list[list[int]]):
        """
        A utility function to do DFS for a 2D
        boolean matrix. It only considers
        the 8 neighbours as adjacent vertices
        """

        # Mark this cell as visited
        visited[i][j] = True

        # Recurse for all connected neighbours
        for k in range(8):
            if self.is_safe(i + self.row_nbr[k], j + self.col_nbr[k], visited):
                self.dfs(i + self.row_nbr[k], j + self.col_nbr[k], visited)


    def bfs(self, i: int, j: int, visited: list[list[int]]):
        """
        visit all the adjacent cells that are land

        params:
        - i: starting point i
        - j: starting point j
        """
        queue = collections.deque()
        queue.append((i,j))


        while queue:
            row, col = queue.popleft()

            # Mark this cell as visited
            visited[row][col] = True

            # add all connected neighbours
            for k in range(8):
                if self.is_safe(row + self.row_nbr[k], col + self.col_nbr[k], visited):
                    queue.append((row + self.row_nbr[k], col + self.col_nbr[k]))


    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def count_islands(self, search_strategy: SearchStrategy) -> int:
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    if search_strategy == SearchStrategy.DFS:
                        self.dfs(i, j, visited)
                    else:
                        self.bfs(i, j, visited)
                    count += 1

        return count



graphs = [
             [[1, 1, 0, 0, 0],
              [0, 1, 0, 0, 1],
              [1, 0, 0, 1, 1],
              [0, 0, 0, 0, 0],
              [1, 0, 1, 0, 1]],

             [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]],

             [[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]],

             [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]],

             [[1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 1, 0, 0, 0],
              [1, 0, 0, 0, 1]]
        ]

for graph in graphs:
    g = Graph(graph)

    pprint.pp(graph)
    print("Number of islands using DFS is:", g.count_islands(SearchStrategy.DFS))
    print("Number of islands using BFS is:", g.count_islands(SearchStrategy.BFS))
    print()