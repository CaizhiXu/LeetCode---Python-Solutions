# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
## time - O(N), space - O(N)
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.dfs((0, 0), 0, visited, directions, robot)

    def dfs(self, pos, d, visited, directions, robot):
        x, y = pos
        robot.clean()
        visited.add(pos)
        for i in range(len(directions)):
            nd = (d + i) % 4
            dx, dy = directions[nd]
            nx, ny = x + dx, y + dy

            if (nx, ny) not in visited and robot.move():
                self.dfs((nx, ny), nd, visited, directions, robot)
                self.backtrack(robot)
            robot.turnRight()

    def backtrack(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()