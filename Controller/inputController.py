from PyQt5.QtCore import Qt

from Views import Ui_inputFrame, Ui_RamAreaInput, Ui_ProcessInput
from PyQt5.QtWidgets import QWidget
from .Models import *


class RamBlockEntry(QWidget):
    def __init__(self, index: int, type_block: int, capacity: float | int, up_func, down_func, del_func):
        super().__init__()
        self.index = index
        self.capacity = capacity
        self.type_block = type_block
        self.move_up = up_func
        self.move_down = down_func
        self.del_func = del_func

        self.ui = Ui_RamAreaInput()
        self.ui.setupUi(self)

        self.setup_ui()
        self.connect_action()

    def connect_action(self):
        self.ui.del_btn.clicked.connect(lambda: self.del_func(self.index))
        self.ui.up_btn.clicked.connect(lambda: self.move_up(self.index))
        self.ui.down_btn.clicked.connect(lambda: self.move_down(self.index))

    def append_css(self, css: str):
        old_css = self.styleSheet()
        new_css = old_css + '\n' + css
        self.setStyleSheet(new_css)

    def setup_ui(self):
        self.ui.capacity_lb.setText(RamBlockEntry.format_capacity(self.capacity))
        if self.type_block == 0:
            cs = '#bodyContainer{background-color: #229818}'
            self.append_css(cs)
        elif self.type_block == 1:
            cs = '#bodyContainer{background-color: #CB2F2F}'
            self.append_css(cs)

    def to_model(self):
        return RamBlock(self.index, self.type_block, self.capacity)

    @staticmethod
    def get_bg_color_of_type(t: int):
        if t == 0:
            return '#229818'
        elif t == 1:
            return '#CB2F2F'
        else:
            return '#ffffff'

    @staticmethod
    def valid_capacity_input(inp: str):
        sp = inp.split('.')
        if len(sp) == 2 and sp[0].isdecimal() and sp[1].isdecimal():
            return True
        elif len(sp) == 1 and sp[0].isdecimal():
            return True
        else:
            return False

    @staticmethod
    def convert_cap_to_float(cap: str):
        if RamBlockEntry.valid_capacity_input(cap):
            return float(cap)
        return 0

    @staticmethod
    def format_capacity(cap: float):
        str_cap = str(cap)
        cap = str_cap.split('.')
        if int(cap[1]) == 0:
            return cap[0]
        return str_cap


class ProcessEntry(QWidget):
    def __init__(self, index: int, capacity: float, up_func, down_func, del_func):
        super().__init__()
        self.index = index
        self.capacity = capacity
        self.move_up = up_func
        self.move_down = down_func
        self.del_func = del_func

        self.ui = Ui_ProcessInput()
        self.ui.setupUi(self)

        self.setup_obj()
        self.connect_action()

    def setup_obj(self):
        self.ui.capacity_lb.setText(RamBlockEntry.format_capacity(self.capacity))
        self.ui.index_lb.setText(str(self.index))

    def connect_action(self):
        self.ui.del_btn.clicked.connect(lambda: self.del_func(self.index))
        self.ui.up_btn.clicked.connect(lambda: self.move_up(self.index))
        self.ui.down_btn.clicked.connect(lambda: self.move_down(self.index))

    def set_index(self, index: int):
        self.index = index
        self.ui.index_lb.setText(str(self.index))

    def __delete_entry(self):
        try:
            self.deleteLater()
            self.update_index_func()
        except Exception as e:
            print(e)

    def to_model(self):
        return Process(self.index, self.capacity)


class InputController(QWidget):
    re_update_ram_index = False
    re_update_process_index = False

    def __init__(self):
        super().__init__()
        self.ui = Ui_inputFrame()
        self.ui.setupUi(self)

        self.ui_turning()
        self.connect_action()

    def ui_turning(self):
        self.ui.ramInsert_lo.setAlignment(Qt.AlignTop)
        self.ui.processInsert_lo.setAlignment(Qt.AlignTop)

    def connect_action(self):
        self.ui.ramInput_le.textChanged.connect(self.__control_ram_input)
        self.ui.green_btn.clicked.connect(lambda: self.add_ram_block(0))
        self.ui.red_btn.clicked.connect(lambda: self.add_ram_block(1))
        self.ui.blue_btn.clicked.connect(self.add_process_input)

    def __control_ram_input(self):
        capacity = self.ui.ramInput_le.text()
        if RamBlockEntry.valid_capacity_input(capacity):
            self.ui.errorMess_lb.setText("")

        else:
            self.ui.errorMess_lb.setText("Chỉ nhập số")

    def count_ram(self):
        return self.ui.ramInsert_lo.count()

    def count_process(self):
        return self.ui.processInsert_lo.count()

    def __move_ram_up(self, cur_index: int):
        if cur_index > 0:
            self.__swap_ram(cur_index - 1, cur_index)

    def __move_ram_down(self, cur_index: int):
        if cur_index < self.count_ram() - 1:
            self.__swap_ram(cur_index, cur_index + 1)
        pass

    def __swap_ram(self, id1: int, id2: int):
        self.update_ram_index()

        widget1 = self.ui.ramInsert_lo.itemAt(id1).widget()
        widget2 = self.ui.ramInsert_lo.itemAt(id2).widget()

        self.ui.ramInsert_lo.removeWidget(widget1)
        self.ui.ramInsert_lo.removeWidget(widget2)

        self.ui.ramInsert_lo.insertWidget(id1, widget2)
        self.ui.ramInsert_lo.insertWidget(id2, widget1)

        self.update_ram_index()

    def __move_process_up(self, cur_index: int):
        if cur_index > 0:
            self.__swap_process(cur_index - 1, cur_index)

    def __move_process_down(self, cur_index: int):
        if cur_index < self.count_process() - 1:
            self.__swap_process(cur_index, cur_index + 1)
        pass

    def __swap_process(self, id1: int, id2: int):
        self.update_process_index()

        widget1 = self.ui.processInsert_lo.itemAt(id1).widget()
        widget2 = self.ui.processInsert_lo.itemAt(id2).widget()

        self.ui.processInsert_lo.removeWidget(widget1)
        self.ui.processInsert_lo.removeWidget(widget2)

        self.ui.processInsert_lo.insertWidget(id1, widget2)
        self.ui.processInsert_lo.insertWidget(id2, widget1)

        self.update_process_index()

    def add_ram_block(self, t: int):
        capacity = self.ui.ramInput_le.text()
        if RamBlockEntry.valid_capacity_input(capacity):
            if InputController.re_update_ram_index:
                self.update_ram_index()

            capacity = float(capacity)
            entry = RamBlockEntry(self.count_ram(), t, capacity, self.__move_ram_up, self.__move_ram_down,
                                  self.delete_ram_entry)
            self.ui.ramInsert_lo.addWidget(entry)

            self.ui.ramInput_le.clear()

    def add_process_input(self):
        capacity = self.ui.processInput_le.text()
        if RamBlockEntry.valid_capacity_input(capacity):
            if InputController.re_update_process_index:
                self.update_process_index()

            capacity = float(capacity)

            entry = ProcessEntry(self.count_process(), capacity, self.__move_process_up, self.__move_process_down,
                                 self.delete_process_entry)
            self.ui.processInsert_lo.addWidget(entry)

            self.ui.processInput_le.clear()

    def delete_ram_entry(self, index: int):
        widget = self.ui.ramInsert_lo.itemAt(index).widget()
        self.ui.ramInsert_lo.removeWidget(widget)
        self.update_ram_index()
        widget.deleteLater()

    def delete_process_entry(self, index: int):
        widget = self.ui.processInsert_lo.itemAt(index).widget()
        self.ui.processInsert_lo.removeWidget(widget)
        self.update_process_index()

        widget.deleteLater()

    def total_ram_capacity(self):
        total_capacity = 0
        for i in range(self.ui.ramInsert_lo.count()):
            item = self.ui.ramInsert_lo.itemAt(i)
            wi = item.widget()
            total_capacity += float(wi.capacity_lb.text())
        return total_capacity

    def update_ram_index(self):
        for i in range(self.ui.ramInsert_lo.count()):
            item = self.ui.ramInsert_lo.itemAt(i)
            wi = item.widget()
            wi.index = i

    def update_process_index(self):
        for i in range(self.ui.processInsert_lo.count()):
            item = self.ui.processInsert_lo.itemAt(i)
            wi = item.widget()
            wi.set_index(i)

    def update_total_ram_capacity_label(self):
        pass

    def get_ram_model_list(self) -> list[RamBlock]:
        model_list = []
        for i in range(self.ui.ramInsert_lo.count()):
            item = self.ui.ramInsert_lo.itemAt(i)
            wi = item.widget()
            model_list.append(wi.to_model())
        RamBlock.normalize_model(model_list)
        return model_list

    def get_process_model_list(self) -> list[Process]:
        model_list = []
        for i in range(self.ui.processInsert_lo.count()):
            item = self.ui.processInsert_lo.itemAt(i)
            wi = item.widget()
            model_list.append(wi.to_model())
        return model_list

    def print_widget(self):
        print('*' * 60)
        for i in range(self.ui.ramInsert_lo.count()):
            item = self.ui.ramInsert_lo.itemAt(i)
            wi = item.widget()
            print(f'{wi.index}: {wi.ui.capacity_lb.text()}')
        print('*' * 60, end='\n\n')


if __name__ == '__main__':
    print(str(2.3))
