## move, time - O(1), space - O(n)
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake = deque([(0, 0)])
        self.posSet = set([(0, 0)])
        self.width = width
        self.height = height
        self.food = food
        self.currFoodIdx = 0
        self.dir = {'U': [-1, 0], 'R': [0, 1], 'D': [1, 0], 'L': [0, -1]}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.snake[-1]
        tail = self.snake.popleft()
        self.posSet.remove(tail)
        new_head = (head[0] + self.dir[direction][0], head[1] + self.dir[direction][1])
        if not (0 <= new_head[0] < self.height) or not (0 <= new_head[1] < self.width) \
                or new_head in self.posSet:
            return -1

        self.snake.append(new_head)
        self.posSet.add(new_head)
        if self.currFoodIdx < len(self.food) and [new_head[0], new_head[1]] == self.food[self.currFoodIdx]:
            self.snake.appendleft(tail)
            self.posSet.add(tail)
            self.currFoodIdx += 1

        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)