from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from Views import Ui_DemoFrame, Ui_RamBlockDemo
from .Models import *


class RamBlockDemo(QWidget):
    def __init__(self, minimum_cap: float | int, model: RamBlock):
        super().__init__()
        self.ui = Ui_RamBlockDemo()
        self.ui.setupUi(self)

        self.mini_cap = minimum_cap
        self.model = model

        self.setup_ui()

    def setup_ui(self):
        # Thiết lập chiều cao
        height = 30 + round(self.model.capacity / self.mini_cap)
        self.__set_height(height)

        # thiết lập màu nền
        css = ''
        if self.model.type_block == 0:
            css = '#bodyContainer{background-color: #229818}'
        elif self.model.type_block == 1:
            css = '#bodyContainer{background-color: #CB2F2F}'
        self.setStyleSheet(css)

        # Hiển thị thông tin dung lươợng
        self.ui.capacity_lb.setText(str(self.model.capacity))

        # Hiển thị thông tin ô cuối cùng được cấp phát trong bộ nhớ
        if self.model.end_cell is not None:
            self.ui.endCell_lb.setText(str(self.model.end_cell))

    def __set_height(self, h: int):
        self.setMinimumHeight(h)
        self.setMaximumHeight(h)

    def set_model(self, model: RamBlock):
        self.model = model
        self.setup_ui()


class SiController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DemoFrame()
        self.ui.setupUi(self)

        self.ui_turning()
        self.connect_action()
        self.ram_block_list: list[RamBlock] | None = None
        self.process_list: list[Process] | None = None
        self.speed = 1000

    def ui_turning(self):
        self.ui.ramBar_lo.setAlignment(Qt.AlignTop)
        self.ui.processBar_lo.setAlignment(Qt.AlignTop)
        self.ui.tempBar_lo.setAlignment(Qt.AlignTop)

    def setup_data(self, data):
        pass

    def connect_action(self):
        self.ui.speed075_btn.clicked.connect(self.__set_speed_x075)
        self.ui.speed1_btn.clicked.connect(self.__set_speed_x1)
        self.ui.speed125_btn.clicked.connect(self.__set_speed_x125)

    def __set_speed_btn_default_css(self):
        self.ui.speed075_btn.setStyleSheet('background-color: #666666;')
        self.ui.speed1_btn.setStyleSheet('background-color: #666666;')
        self.ui.speed125_btn.setStyleSheet('background-color: #666666;')

    def __set_speed_x075(self):
        self.speed = 750
        self.__set_speed_btn_default_css()
        self.ui.speed075_btn.setStyleSheet('background-color: #999999;')

    def __set_speed_x1(self):
        self.speed = 1000
        self.__set_speed_btn_default_css()
        self.ui.speed1_btn.setStyleSheet('background-color: #999999;')

    def __set_speed_x125(self):
        self.speed = 1250
        self.__set_speed_btn_default_css()
        self.ui.speed125_btn.setStyleSheet('background-color: #999999;')

