class Spot:
    def __init__(self, row, col, width, height, total_rows, total_cols, colorset):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * height
        self.color = colorset["WHITE"]
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.total_cols = total_cols

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
