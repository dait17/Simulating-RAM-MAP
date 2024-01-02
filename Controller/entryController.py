from PyQt5.QtWidgets import QWidget, QVBoxLayout

from Controller.Models import Process, RamBlock
from Views import Ui_RamAreaInput, Ui_ProcessInput, Ui_RamBlockDemo, Ui_ProcessDemo, Ui_ProcessOVEntry


class RamBlockEntry(QWidget):
    """
    Class dùng để hiển thị khối nhớ được thêm vào
    """
    def __init__(self, index: int, type_block: int, capacity: int, up_func, down_func, del_func):
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

        self.enterEvent = self.__hover_ui
        self.leaveEvent = self.__normal_ui

    def __normal_ui(self, event):
        """
        Thiết lập trạng thái bình thường (khi không được hover)
        """
        self.ui.up_btn.hide()
        self.ui.down_btn.hide()
        self.ui.del_btn.hide()

    def __hover_ui(self, event):
        """
        Thiết lập trạng thái khi đưc hover
        """
        self.ui.up_btn.show()
        self.ui.down_btn.show()
        self.ui.del_btn.show()

    def append_css(self, css: str):
        old_css = self.styleSheet()
        new_css = old_css + '\n' + css
        self.setStyleSheet(new_css)

    def setup_ui(self):
        """
        Thiết lập lại giao diện dựa trên loại khối nhớ
        """
        self.__normal_ui(None)
        self.ui.capacity_lb.setText(str(self.capacity))
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
        if inp.isdecimal():
            return True
        return False


class ProcessEntry(QWidget):
    """
    Class dùng để hiển thị tiến trình được thêm vào
    """
    def __init__(self, index: int, capacity: int, up_func, down_func, del_func):
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
        self.__normal_ui(None)

    def setup_obj(self):
        self.ui.capacity_lb.setText(str(self.capacity))
        self.ui.index_lb.setText(str(self.index+1))

    def __normal_ui(self, event):
        self.ui.up_btn.hide()
        self.ui.down_btn.hide()
        self.ui.del_btn.hide()

    def __hover_ui(self, event):
        self.ui.up_btn.show()
        self.ui.down_btn.show()
        self.ui.del_btn.show()

    def connect_action(self):
        self.ui.del_btn.clicked.connect(lambda: self.del_func(self.index))
        self.ui.up_btn.clicked.connect(lambda: self.move_up(self.index))
        self.ui.down_btn.clicked.connect(lambda: self.move_down(self.index))

        self.enterEvent = self.__hover_ui
        self.leaveEvent = self.__normal_ui

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


class RamBlockDemo(QWidget):
    """
    Class dùng để hiển thị khối nhớ khi mô phỏng
    """
    def __init__(self, model: RamBlock, min_ram_cap: int, demon: bool = False):
        super().__init__()
        self.model = model
        self.min_ram_cap = min_ram_cap

        if not demon:
            self.ui = Ui_RamBlockDemo()
            self.ui.setupUi(self)
            self.setup_ui()
        else:
            widget = QWidget()
            layout = QVBoxLayout(self)
            layout.addWidget(widget)
            # widget.setStyleSheet('background-color: #fff;')
            self.__set_height(round(30 + (self.model.capacity / self.min_ram_cap) * 2))

    def setup_ui(self):
        self.ui.capacity_lb.setText(str(self.model.capacity))
        self.__set_height(round(30 + (self.model.capacity / self.min_ram_cap) * 2))
        self.normal_effect()
        if self.model.type_block==0 or self.model.type_block==1:
            self.ui.endCell_lb.setText(str(self.model.free_index+1))
        else:
            self.ui.endCell_lb.setText('')

    def set_model(self, model: RamBlock):
        self.model = model
        self.setup_ui()

    def high_light_effect(self):
        """
        HIệu ứng làm nổi bật khối nhớ
        """
        if self.model.type_block == 0 or self.model.type_block == -1:
            self.__append_css('#mainBodyContainer {background-color: #2ec221;}')

        elif self.model.type_block == 1:
            pass

    def normal_effect(self):
        """
        Hiệu ứng bình thường
        :return:
        """
        if self.model.type_block == -1:
            self.__append_css('#mainBodyContainer {background-color: #72227a;}')
        elif self.model.type_block == 0:
            self.__append_css('#mainBodyContainer {background-color: #229818;}')
        elif self.model.type_block == 1:
            self.__append_css('#mainBodyContainer {background-color: #CB2F2F;}')
        elif self.model.type_block == 2:
            self.__append_css('#mainBodyContainer {background-color: #2b3f8c;}')

    def valid_effect(self):
        """
        Hiệu ứng khổi nhớ được đánh dấu là hợp lệ
        :return:
        """
        self.__append_css('#mainBodyContainer {background-color: #4ecf7f;}')

    def __set_default_css(self):
        css = ('* {'
               'font-weight: 500;'
               'color: #f0f0f0;'
               '}')
        self.setStyleSheet(css)

    def __append_css(self, css: str):
        self.__set_default_css()
        old_css = self.styleSheet()
        self.setStyleSheet(old_css + '\n' + css)

    def __set_height(self, h: int):
        if h > 100:
            h = 100
        self.setMinimumHeight(h)
        self.setMaximumHeight(h)


class ProcessDemo(QWidget):
    """
    Class dùng để hiển thị tiến trình khi mô phỏng
    """
    def __init__(self, model: Process, min_ram_cap: int):
        super().__init__()
        self.ui = Ui_ProcessDemo()
        self.ui.setupUi(self)
        self.model = model
        self.min_ram_cap = min_ram_cap

        self.setup_ui()

    def setup_ui(self):
        self.ui.index_lb.setText(str(self.model.index))
        self.ui.capacity_lb.setText(str(self.model.capacity))
        self.__set_height(round(30 + self.model.capacity / self.min_ram_cap))
        self.__append_css('#mainBodyContainer {background-color: #0000FF;}')

    def set_model(self, model: RamBlock):
        self.model = model
        self.setup_ui()

    def __set_default_css(self):
        css = ('* {'
               'font-weight: 500;'
               'color: #f0f0f0;'
               '}')
        self.setStyleSheet(css)

    def __append_css(self, css: str):
        self.__set_default_css()
        old_css = self.styleSheet()
        self.setStyleSheet(old_css + '\n' + css)

    def __set_height(self, h: int):
        if h >100:
            h = 100
        self.ui.mainBodyContainer.setMinimumHeight(h)
        self.ui.mainBodyContainer.setMaximumHeight(h)


class ProcessOVEntry(QWidget):
    """
    Class dùng để hiển thị thông báo trạng thái cấp phát của một tiến trình
    """
    def __init__(self, process_no, process_size, block_no):
        super().__init__()
        self.ui = Ui_ProcessOVEntry()
        self.ui.setupUi(self)

        self.ui.processNo_lb.setText(str(process_no))
        self.ui.processSize_lb.setText(str(process_size))
        self.ui.blockNo_lb.setText(str(block_no))


