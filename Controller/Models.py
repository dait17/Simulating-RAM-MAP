from functools import reduce


class RamBlock:

    def __init__(self, index: int, type_block: int, capacity):
        self.capacity = capacity
        self.type_block = type_block
        self.index = index

        self.start_cell: int | None = None
        self.end_cell: int | None = None

    def __add__(self, other) -> float | int:
        return self.capacity + other.capacity

    @staticmethod
    def sum_capacity(models: list):
        return reduce(lambda a, b: a + b, models)

    @staticmethod
    def normalize_model(models:list):
        models.sort(key=lambda model: model.index)

        cur_cell = 0
        for model in models:
            model.start_cell = int(cur_cell)
            model.end_cell = cur_cell+int(model.capacity)-1
            cur_cell = model.end_cell+1


class Process:
    def __init__(self, index: int, capacity: float | int):
        self.capacity = capacity
        self.index = index

    def __add__(self, other) -> float | int:
        return self.capacity + other.capacity

    @staticmethod
    def sum_capacity(models: list):
        return reduce(lambda a, b: a + b, models)


if __name__ == '__main__':
    a = RamBlock(0, 0, 12)
    b = RamBlock(1, 1, 8)

    print(RamBlock.sum_capacity([a, b]))
