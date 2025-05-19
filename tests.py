import unittest
from maze import Maze
from canvas import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells2(self):
        num_cols = 22
        num_rows = 22
        m1 = Maze(1, 1, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m1._cells), 
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]), 
            num_rows
        )
    
    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        win = Window(800, 600)
        m1 = Maze(25, 25, num_rows, num_cols, 36, 36, win, 5)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0, 0)
        m1._reset_cells_visited()
        visit_reset_list = []
        for i in range(num_cols):
            for j in range(num_rows):
                visit_reset_list.append(m1._cells[i][j].visited)
        self.assertEqual(visit_reset_list, [False for _ in range(25)])

if __name__ == "__main__":
    unittest.main()