from functools import reduce


class RamBlock:

    def __init__(self, index: int, type_block: int, capacity:int):
        """

        :param index:
        :param type_block:
        -1:khối nhớ bị phân mảnh sau khi cấp phát cho tiến tình;
        0:Khối nhớ trống;
        1:Khối nhớ đã được sử dụng trước đó;
        2:Khối nhớ được cacps phát cho tiến trình khi chạy mô phỏng
        :param capacity:
        """
        # Dung lượng khối nhớ
        self.capacity = capacity
        self.type_block = type_block
        self.index = index

        self.free_index = -1

        self.start_cell: int | None = None
        self.end_cell: int | None = None

    def copy(self):
        cp = RamBlock(self.index, self.type_block, self.capacity)
        cp.free_index = self.free_index
        cp.start_cell = self.start_cell
        cp.end_cell = self.end_cell
        return cp

    def __add__(self, other) -> int:
        return self.capacity + other.capacity

    @staticmethod
    def sum_capacity(models: list):
        return reduce(lambda a, b: a + b, models)

    @staticmethod
    def normalize_model(models: list):
        models.sort(key=lambda model: model.index)

        cur_cell = 0
        free_index = 0
        for model in models:
            model.start_cell = int(cur_cell)
            model.end_cell = cur_cell + int(model.capacity) - 1
            cur_cell = model.end_cell + 1

            if model.type_block == 0 or model.type_block==-1:
                model.free_index = free_index
                free_index += 1

    @staticmethod
    def update_block(models:list):
        models.sort(key=lambda model: model.index)
        cur_cell = 0
        for model in models:
            model.start_cell = int(cur_cell)
            model.end_cell = cur_cell + int(model.capacity) - 1
            cur_cell = model.end_cell + 1


    @staticmethod
    def get_min(ram_list: list):
        return min(ram_list, key=lambda oj: oj.capacity)

    @staticmethod
    def get_free_block(models: list):
        return [model for model in models if model.type_block == 0 or model.type_block == -1]

    @staticmethod
    def insert_model(model_list: list, index: int, model):
        model_list.insert(index, model)
        model.index = index
        index += 1
        for m in model_list[index:]:
            m.index = index
            index += 1


class Process:
    def __init__(self, index: int, capacity: int):
        self.capacity = capacity
        self.index = index

    def __add__(self, other) -> int:
        return self.capacity + other.capacity

    @staticmethod
    def normalize_model(models: list):
        models.sort(key=lambda model: model.index)

    @staticmethod
    def sum_capacity(models: list):
        return reduce(lambda a, b: a + b, models)

    @staticmethod
    def get_min(process_list: list):
        return min(process_list, key=lambda oj: oj.capacity)


