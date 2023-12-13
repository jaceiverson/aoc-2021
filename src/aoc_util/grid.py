"""
grid class 

inspired by 
 - https://gist.github.com/seeinglogic/65f59c5a8b19be9bbb0013253067c64f
 - some other grid classes I have tried to implement in the past
"""
import math
from dataclasses import dataclass

from rich import print


@dataclass
class Point:
    x: int
    y: int


class Grid:
    def __init__(self, rows: list[str] | None = None) -> None:
        # 0 based index so start at -1
        self.height = -1
        self.width = -1

        self.rows: list[list] = []

        if rows is not None:
            [self._add_line(x) for x in rows]
            self.finish()

    def __str__(self) -> str:
        return f"Grid. H: {self.height}. W: {self.width}"

    def show(self) -> None:
        """prints the grid"""
        for r in self.rows:
            print(r)

    @property
    def dimensions(self) -> tuple:
        """returns dimensions of grid as tuple (height,width)"""
        return self.height, self.width

    def _add_line(self, line: str) -> None:
        """adds a row to the bottom"""
        self.rows.append(line.strip())

    def finish(self) -> None:
        """finish making grid, mark height and width"""
        self.height = len(self.rows)
        self.width = len(self.rows[0])

    def get(self, pos: Point | tuple) -> str:
        """return a value at a given point"""
        x, y = (pos.x, pos.y) if isinstance(pos, Point) else pos
        return self.rows[y][x]

    def get_row(self, row_index: int) -> list[Point]:
        """return a list of Points for a given row index"""
        if row_index < self.height:
            return self.rows[row_index]
        raise IndexError(
            "Row Index out of Range. Max Index (Height): "
            f"{self.height}. Requested Row: {row_index}"
        )

    def get_column(self, column_index: int) -> list[Point]:
        """return a list of Points for a given column index"""
        if column_index < self.width:
            return [x[column_index] for x in self.rows]
        raise IndexError(
            "Column Index out of Range. Max Index (Width): "
            f"{self.width}. Requested Column: {column_index}"
        )

    def add_row(self, new_values: list[str], row_index: int) -> None:
        """adds a row at the given index"""
        if len(new_values) != self.width:
            raise IndexError(
                "New Values don't match current width.\n"
                f"New Values: {new_values} Length: {len(new_values)}\n"
                f"Grid Width: {self.width}"
            )
        self.rows.insert(row_index, new_values)
        self.height += 1

    def add_column(self, new_values: list[str], column_index: int) -> None:
        """adds a column at the given index"""
        if len(new_values) != self.height:
            raise IndexError(
                "New Values don't match current height.\n"
                f"New Values: {new_values} Length: {len(new_values)}\n"
                f"Grid Height: {self.height}"
            )
        for idx_, v in enumerate(new_values):
            self.rows[idx_] = list(self.rows[idx_])
            self.rows[idx_].insert(column_index, v)
            self.rows[idx_] = "".join(self.rows[idx_])

        self.width += 1

    def scan_surroundings(
        self,
        pos: Point | tuple,
        check_diagnals: bool = True,
        check_self: bool = False,
    ) -> list[Point]:
        """scans the 4 or 8 values around a point and returns a list of those values"""
        dir_deltas = [
            Point(-1, 0),
            Point(0, -1),
            Point(0, 1),
            Point(1, 0),
        ]
        if check_diagnals:
            dir_deltas += [
                Point(-1, -1),
                Point(-1, 1),
                Point(1, -1),
                Point(1, 1),
            ]
        if check_self:
            dir_deltas.append(Point(0, 0))

        if not isinstance(pos, Point):
            pos = Point(pos[0], pos[1])

        adjacent_positions = {
            (delta.x, delta.y): self.get(Point(pos.x + delta.x, pos.y + delta.y))
            for delta in dir_deltas
            if not (
                pos.x + delta.x < 0
                or pos.x + delta.x >= self.width
                or pos.y + delta.y < 0
                or pos.y + delta.y >= self.height
            )
        }

        return adjacent_positions

    def search_surroundings(
        self,
        pos: Point | tuple,
        mapping_function: callable = None,
        check_diagnals: bool = True,
        check_self: bool = False,
    ):
        if not isinstance(pos, Point):
            pos = Point(pos)
        return [
            x
            for x in self.scan_surroundings(pos, check_diagnals, check_self)
            if mapping_function(x)
        ]

    def get_all_positions(self) -> None:
        """returns all values as a generator"""
        for y in range(self.height):
            for x in range(self.width):
                yield self.get(Point(x, y))

    def search_grid(self, mapping_function: callable):
        """search entire grid, return dictionary of points and values"""
        for y in range(self.height):
            for x in range(self.width):
                if mapping_function(self.get(Point(x, y))):
                    yield {(x, y): self.get(Point(x, y))}

    @staticmethod
    def manhattan_distance(a: Point | tuple, b: Point | tuple) -> int:
        """calculate manhattan distance between 2 points"""
        if not isinstance(a, Point):
            a = Point(a[0], a[1])
        if not isinstance(b, Point):
            b = Point(b[0], b[1])

        return abs(a.x - b.x) + abs(a.y - b.y)

    @staticmethod
    def euclidean_distance(a: Point | tuple, b: Point | tuple) -> float:
        """calculate the euclidean distance between 2 points"""
        if not isinstance(a, Point):
            a = Point(a[0], a[1])
        if not isinstance(b, Point):
            b = Point(b[0], b[1])

        return math.sqrt(abs(a.x - b.x) ** 2 + abs(a.y - b.y) ** 2)
