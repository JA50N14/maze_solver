from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
        ):
            self.x1 = x1
            self.y1 = y1
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.cell_size_x = cell_size_x
            self.cell_size_y = cell_size_y
            self._win = win
            self.seed = seed
            if self.seed is not None:
                random.seed(self.seed)
            self._cells = []

            self._create_cells()
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
            self._reset_cells_visited()
            

    def _create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                new_cell = Cell(self._win)
                self._cells[i].append(new_cell)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell = self._cells[i][j]
        cell_x1 = (i * self.cell_size_x) + self.x1
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y1 = (j * self.cell_size_y) + self.y1
        cell_y2 = cell_y1 + self.cell_size_y
        cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    
    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self.num_cols - 1][self.num_rows - 1]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell.has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)


    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            unvisited = []
            if j != 0 and self._cells[i][j - 1].visited is False:
                unvisited.append((i, j - 1))
            if i < (self.num_cols - 1) and self._cells[i + 1][j].visited is False:
                unvisited.append((i + 1, j))
            if j < (self.num_rows - 1) and self._cells[i][j + 1].visited is False:
                unvisited.append((i, j + 1))
            if i != 0 and self._cells[i - 1][j].visited is False:
                unvisited.append((i - 1, j))

            if len(unvisited) == 0:
                self._draw_cell(i, j)
                return 

            chosen_coords = unvisited[random.randint(0, len(unvisited) - 1)]
            chosen_cell = self._cells[chosen_coords[0]][chosen_coords[1]]

            if j - 1 == chosen_coords[1]:
                current.has_top_wall = False
                chosen_cell.has_bottom_wall = False
            if i + 1 == chosen_coords[0]:
                current.has_right_wall = False
                chosen_cell.has_left_wall = False
            if j + 1 == chosen_coords[1]:
                current.has_bottom_wall = False
                chosen_cell.has_top_wall = False
            if i - 1 == chosen_coords[0]:
                current.has_left_wall = False
                chosen_cell.has_right_wall = False

            self._break_walls_r(chosen_coords[0], chosen_coords[1])


    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def _solve(self):
        return self._solve_r(0, 0)


    def _solve_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        while True:
            unvisited = []
            if j != 0 and self._cells[i][j - 1].has_bottom_wall == False and self._cells[i][j - 1].visited == False:
                unvisited.append((i, j - 1))
            if i != self.num_cols - 1 and self._cells[i + 1][j].has_left_wall == False and self._cells[i + 1][j].visited == False:
                unvisited.append((i + 1, j))
            if j != self.num_rows - 1 and self._cells[i][j + 1].has_top_wall == False and self._cells[i][j + 1].visited == False:
                unvisited.append((i, j + 1))
            if i != 0 and self._cells[i - 1][j].has_right_wall == False and self._cells[i - 1][j].visited == False:
                unvisited.append((i - 1, j))
            
            if not unvisited:
                return

            chosen_coords = unvisited[random.randint(0, len(unvisited) - 1)]
            chosen_cell = self._cells[chosen_coords[0]][chosen_coords[1]]
            current.draw_move(chosen_cell)
            self._animate()
            if self._solve_r(chosen_coords[0], chosen_coords[1]):
                return True
            current.draw_move(chosen_cell, True)
            self._animate()






        
