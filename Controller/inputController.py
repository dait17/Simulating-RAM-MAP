from PyQt5.QtCore import Qt

from Controller.entryController import RamBlockEntry, ProcessEntry
from Views import Ui_inputFrame, Ui_RamAreaInput, Ui_ProcessInput
from PyQt5.QtWidgets import QWidget
from .Models import *
import random


class InputController(QWidget):

    """
    Class dùng để kiểm soát và xử lý giao diện nhập dữ liệu
    """
    re_update_ram_index = False
    re_update_process_index = False

    def __init__(self):
        super().__init__()
        self.ui = Ui_inputFrame()
        self.ui.setupUi(self)

        self.ui_turning()
        self.connect_action()
        self.init_data()

    def ui_turning(self):
        """
        Tinh chỉnh lại giao diện
        """
        self.ui.ramInsert_lo.setAlignment(Qt.AlignTop)
        self.ui.processInsert_lo.setAlignment(Qt.AlignTop)

    def connect_action(self):
        """
        Kết nối sự kiện cho các nút bấm
        """
        self.ui.ramInput_le.textChanged.connect(self.__control_ram_input)
        self.ui.processInput_le.textChanged.connect(self.__control_process_input)
        self.ui.green_btn.clicked.connect(lambda: self.add_ram_block(0))
        self.ui.red_btn.clicked.connect(lambda: self.add_ram_block(1))
        self.ui.blue_btn.clicked.connect(self.add_process_input)

    def init_data(self):
        """
        Khởi tạo sẵn một kịch bản
        :return:
        """
        kb_ram = [
            [1, 300],
            [0, 550],
            [1, 200],
            [0, 720],
            [1, 100],
            [0, 780]
        ]

        kb_process = [400, 120, 600, 300]

        for c in kb_ram:
            wg = RamBlockEntry(self.count_ram(), c[0], c[1], self.__move_ram_up, self.__move_ram_down,
                               self.delete_ram_entry)
            self.ui.ramInsert_lo.addWidget(wg)

        for p in kb_process:
            wg = ProcessEntry(self.count_process(), p, self.__move_process_up,
                              self.__move_process_down,
                              self.delete_process_entry)
            self.ui.processInsert_lo.addWidget(wg)

    def __control_ram_input(self):
        """
        Kiểm soát dữ liệu nhập vào của khối nhớ
        :return:
        """
        capacity = self.ui.ramInput_le.text()
        if RamBlockEntry.valid_capacity_input(capacity):
            self.ui.errorMess_lb.setText("")

        else:
            self.ui.errorMess_lb.setText("Chỉ nhập số nguyên")

    def __control_process_input(self):
        """
        Kiểm soát dữ liệu nhập vào của tiến trình
        """
        capacity = self.ui.processInput_le.text()
        if capacity.isdecimal():
            self.ui.procesLEError_lb.setText("")

        else:
            self.ui.procesLEError_lb.setText("Chỉ nhập số nguyên")

    def count_ram(self):
        """
        Đếm số lượng khối nhớ được nhập vào
        """
        return self.ui.ramInsert_lo.count()

    def count_process(self):
        """
        Đếm số lượng tiến trình được nhập vào
        """
        return self.ui.processInsert_lo.count()

    def __move_ram_up(self, cur_index: int):
        """
        Di chuyển khối nhớ lến trên 1 vị trí
        """
        if cur_index > 0:
            self.__swap_ram(cur_index - 1, cur_index)

    def __move_ram_down(self, cur_index: int):
        """
        Di chuyển khối nhớ xuống 1 vị trí
        """
        if cur_index < self.count_ram() - 1:
            self.__swap_ram(cur_index, cur_index + 1)
        pass

    def __swap_ram(self, id1: int, id2: int):
        """
        Giúp tráo đổi vị trí của 2 khối nhớ liền kề
        """
        self.update_ram_index()

        widget1 = self.ui.ramInsert_lo.itemAt(id1).widget()
        widget2 = self.ui.ramInsert_lo.itemAt(id2).widget()

        self.ui.ramInsert_lo.removeWidget(widget1)
        self.ui.ramInsert_lo.removeWidget(widget2)

        self.ui.ramInsert_lo.insertWidget(id1, widget2)
        self.ui.ramInsert_lo.insertWidget(id2, widget1)

        self.update_ram_index()

    def __move_process_up(self, cur_index: int):
        """
        Di chuyển tiến trình lên 1 vị trí
        """
        if cur_index > 0:
            self.__swap_process(cur_index - 1, cur_index)

    def __move_process_down(self, cur_index: int):
        """
        Di chuyển tiến trình xuống 1 vị trí
        """
        if cur_index < self.count_process() - 1:
            self.__swap_process(cur_index, cur_index + 1)
        pass

    def __swap_process(self, id1: int, id2: int):
        """
        Tráo đổi vị trí của 2 tiến trình liền kề
        """
        self.update_process_index()

        widget1 = self.ui.processInsert_lo.itemAt(id1).widget()
        widget2 = self.ui.processInsert_lo.itemAt(id2).widget()

        self.ui.processInsert_lo.removeWidget(widget1)
        self.ui.processInsert_lo.removeWidget(widget2)

        self.ui.processInsert_lo.insertWidget(id1, widget2)
        self.ui.processInsert_lo.insertWidget(id2, widget1)

        self.update_process_index()

    def add_ram_block(self, type_block: int):
        """
        Thêm khối nhớ
        """
        capacity = self.ui.ramInput_le.text()
        if RamBlockEntry.valid_capacity_input(capacity):
            if InputController.re_update_ram_index:
                self.update_ram_index()

            capacity = int(capacity)
            entry = RamBlockEntry(self.count_ram(), type_block, capacity, self.__move_ram_up, self.__move_ram_down,
                                  self.delete_ram_entry)
            self.ui.ramInsert_lo.addWidget(entry)
            self.ui.ramInput_le.clear()

    def add_process_input(self):
        """
        Thêm tiến trình
        """
        capacity = self.ui.processInput_le.text()
        if RamBlockEntry.valid_capacity_input(capacity):
            if InputController.re_update_process_index:
                self.update_process_index()

            capacity = int(capacity)

            entry = ProcessEntry(self.count_process(), capacity, self.__move_process_up, self.__move_process_down,
                                 self.delete_process_entry)
            self.ui.processInsert_lo.addWidget(entry)

            self.ui.processInput_le.clear()

    def delete_ram_entry(self, index: int):
        """
        Xoá khối nhớ
        :return:
        """
        widget = self.ui.ramInsert_lo.itemAt(index).widget()
        self.ui.ramInsert_lo.removeWidget(widget)
        self.update_ram_index()
        widget.deleteLater()

    def delete_process_entry(self, index: int):
        """
        Xoá tiến trình
        """
        widget = self.ui.processInsert_lo.itemAt(index).widget()
        self.ui.processInsert_lo.removeWidget(widget)
        self.update_process_index()
        widget.deleteLater()

    def total_ram_capacity(self):
        """
        Tính tồng dùng lượng bộ nhớ từ các khối nhớ được thêm vào
        """
        total_capacity = 0
        for i in range(self.ui.ramInsert_lo.count()):
            item = self.ui.ramInsert_lo.itemAt(i)
            wi = item.widget()
            total_capacity += float(wi.capacity_lb.text())
        return total_capacity

    def update_ram_index(self):
        """
        Cập nhật lại vị trí của các khối nhớ theo đúng thứ tự
        (khi một khối nhớ di chuyển hoặc bị xoá)
        """
        for i in range(self.ui.ramInsert_lo.count()):
            item = self.ui.ramInsert_lo.itemAt(i)
            wi = item.widget()
            wi.index = i

    def update_process_index(self):
        """
        Cập nhật lại vị trí của các tiến trình theo đúng thứ tự
        (khi một khối nhớ di chuyển hoặc bị xoá)
        """
        for i in range(self.ui.processInsert_lo.count()):
            item = self.ui.processInsert_lo.itemAt(i)
            wi = item.widget()
            wi.set_index(i)

    def update_total_ram_capacity_label(self):
        pass

    def get_ram_model_list(self) -> list[RamBlock]:
        """
        Trả về một danh sách các model dựa trên các khối nhớ được nhập vào
        """
        model_list = []
        for i in range(self.ui.ramInsert_lo.count()):
            item = self.ui.ramInsert_lo.itemAt(i)
            wi = item.widget()
            model_list.append(wi.to_model())
        RamBlock.normalize_model(model_list)
        return model_list

    def get_process_model_list(self) -> list[Process]:
        """
        Trả về một danh sách các model dựa trên các tến trình được nhập vào
        """
        model_list = []
        for i in range(self.ui.processInsert_lo.count()):
            item = self.ui.processInsert_lo.itemAt(i)
            wi = item.widget()
            model_list.append(wi.to_model())
        return model_list


