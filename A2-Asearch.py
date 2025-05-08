import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, end):
    open_list = []
    closed_list = set()

    start_node = Node(start)
    goal_node = Node(end)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        (x, y) = current_node.position
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]  # 4 directions

        for next_pos in neighbors:
            if (0 <= next_pos[0] < len(grid)) and (0 <= next_pos[1] < len(grid[0])):  # Within bounds
                if grid[next_pos[0]][next_pos[1]] == 1:  # Obstacle
                    continue
                if next_pos in closed_list:
                    continue

                neighbor = Node(next_pos, current_node)
                neighbor.g = current_node.g + 1
                neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
                neighbor.f = neighbor.g + neighbor.h

                if any(open_node.position == neighbor.position and neighbor.g >= open_node.g for open_node in open_list):
                    continue

                heapq.heappush(open_list, neighbor)

    return None  # No path found

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start = (0, 0)
    end = (4, 4)
    path = astar(grid, start, end)
    print("Path found:" if path else "No path found")
    print(path)
