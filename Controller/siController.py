from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget

from Views import Ui_DemoFrame, Ui_RamBlockDemo
from .Models import *
from .fitController import BaseFit, FirstFit, NextFit, BestFit, WorstFit
from .entryController import ProcessOVEntry


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

        self.cur_fit: BaseFit | None = None
        self.__fit_list = ['first_fit', 'next_fit', 'best_fit', 'worst_fit']
        self.__cur_fit_id = -1

        self.__pausing = False
        self.auto_run = True

    def ui_turning(self):
        self.ui.ramBar_lo.setAlignment(Qt.AlignTop)
        self.ui.processBar_lo.setAlignment(Qt.AlignTop)
        self.ui.tempBar_lo.setAlignment(Qt.AlignTop)
        self.ui.processOVBar_lo.setAlignment(Qt.AlignTop)
        self.ui.autoRun_checkbox.setChecked(True)

    def set_data(self, ram_block_list, process_list):
        self.ram_block_list = ram_block_list
        self.process_list = process_list

    def connect_action(self):
        # Kết nối nút tốc độ
        self.ui.speed075_btn.clicked.connect(self.__set_speed_x075)
        self.ui.speed1_btn.clicked.connect(self.__set_speed_x1)
        self.ui.speed125_btn.clicked.connect(self.__set_speed_x125)

        # Kết nối nút tạm dừng
        self.ui.pause_btn.clicked.connect(self.pause_)

        # Kết nối nút tự động chạy
        self.ui.autoRun_checkbox.stateChanged.connect(self._change_autorun)

        # Kết nối nút 'chiến lược'

        self.ui.firstFit_btn.clicked.connect(self.set_first_fit)
        self.ui.nextFit_btn.clicked.connect(self.set_next_fit)
        self.ui.bestFit_btn.clicked.connect(self.set_best_fit)
        self.ui.worstFit_btn.clicked.connect(self.set_worst_fit)

    def __set_speed_btn_default_css(self):
        self.ui.speed075_btn.setStyleSheet('background-color: #666666;')
        self.ui.speed1_btn.setStyleSheet('background-color: #666666;')
        self.ui.speed125_btn.setStyleSheet('background-color: #666666;')

    def __set_speed_x075(self):
        self.speed = 1250
        self.__set_speed_btn_default_css()
        self.ui.speed075_btn.setStyleSheet('background-color: #999999;')
        if self.cur_fit is not None:
            self.cur_fit.set_time(self.speed)

    def __set_speed_x1(self):
        self.speed = 1000
        self.__set_speed_btn_default_css()
        self.ui.speed1_btn.setStyleSheet('background-color: #999999;')
        if self.cur_fit is not None:
            self.cur_fit.set_time(self.speed)

    def __set_speed_x125(self):
        self.speed = 750
        self.__set_speed_btn_default_css()
        self.ui.speed125_btn.setStyleSheet('background-color: #999999;')
        if self.cur_fit is not None:
            self.cur_fit.set_time(self.speed)

    def __set_fit_btn_default(self):
        css = ('border-radius: 6px;'
               'padding: 4px 6px;'
               'background-color: #4e4e4e;')

        self.ui.firstFit_btn.setStyleSheet(css)
        self.ui.nextFit_btn.setStyleSheet(css)
        self.ui.bestFit_btn.setStyleSheet(css)
        self.ui.worstFit_btn.setStyleSheet(css)

    def __highlight_first_btn(self):
        self.__set_fit_btn_default()
        self.ui.firstFit_btn.setStyleSheet('background-color: #6e6e6e;')

    def __highlight_next_btn(self):
        self.__set_fit_btn_default()
        self.ui.nextFit_btn.setStyleSheet('background-color: #6e6e6e;')

    def __highlight_best_btn(self):
        self.__set_fit_btn_default()
        self.ui.bestFit_btn.setStyleSheet('background-color: #6e6e6e;')

    def __highlight_worst_btn(self):
        self.__set_fit_btn_default()
        self.ui.worstFit_btn.setStyleSheet('background-color: #6e6e6e;')

    def __set_highlight_fit_btn(self, name: str):
        name = name.lower()
        if name == 'first_fit':
            self.__highlight_first_btn()
        elif name == 'next_fit':
            self.__highlight_next_btn()
        elif name == 'best_fit':
            self.__highlight_best_btn()
        elif name == 'worst_fit':
            self.__highlight_worst_btn()

    def _change_autorun(self):
        self.auto_run = self.ui.autoRun_checkbox.isChecked()

    def set_first_fit(self):
        self.__cur_fit_id = 0
        self.setup_cur_fit()
        self.__restart_fit()

    def set_next_fit(self):
        self.__cur_fit_id = 1
        self.setup_cur_fit()
        self.__restart_fit()

    def set_best_fit(self):
        self.__cur_fit_id = 2
        self.setup_cur_fit()
        self.__restart_fit()

    def set_worst_fit(self):
        self.__cur_fit_id = 3
        self.setup_cur_fit()
        self.__restart_fit()

    def __restart_fit(self):
        self.cur_fit.restart(self.ram_block_list, self.process_list)
        self.cur_fit.pause()
        self.__pausing = True
        self.ui.pause_btn.setText('Bắt đầu')

    def run_(self):
        if self.ram_block_list is not None and self.process_list is not None and len(self.ram_block_list) != 0 and len(
                self.process_list) != 0:
            try:
                self.following_fit()
            except Exception as e:
                print(e)

    def __control_fit(self):
        if self.__cur_fit_id < len(self.__fit_list):
            if self.cur_fit is None or not self.cur_fit.simulating:
                self.cur_fit = self.__get_fit(self.__fit_list[self.__cur_fit_id])
                self.__cur_fit_id += 1

    def setup_cur_fit(self):
        if self.cur_fit is not None:
            self.cur_fit.kill_oj()

        name = self.__fit_list[self.__cur_fit_id].title()
        self.ui.fitTitle_lb.setText(name.title())
        self.__set_highlight_fit_btn(name)
        self.cur_fit = self.cur_fit = self.__get_fit(name)
        self.cur_fit.set_data(self.ram_block_list, self.process_list)
        self.cur_fit.start(self.speed)

    def __connect_timer(self, func, t:int|None=None):
        if t is None:
            t = self.speed
        timer = QTimer(self)
        timer.timeout.connect(func)
        timer.setSingleShot(True)
        timer.start(t)

    def following_fit(self):
        """
        Thiết lập chiến lược tiếp theo để mô phỏng
        """
        if self.__cur_fit_id < len(self.__fit_list) - 1:
            self.__cur_fit_id += 1
            self.__connect_timer(self.setup_cur_fit)
            # self.setup_cur_fit()
        else:
            self.cur_fit.pause()

    def __get_fit(self, fit_name: str):
        fit_name = fit_name.lower()
        if fit_name == 'first_fit':
            return FirstFit(self)
        elif fit_name == 'next_fit':
            return NextFit(self)
        elif fit_name == 'best_fit':
            return BestFit(self)
        elif fit_name == 'worst_fit':
            return WorstFit(self)

    def pause_(self):
        if self.cur_fit is not None:
            if self.cur_fit is not None and not self.cur_fit.simulating:
                self.cur_fit.restart(self.ram_block_list, self.process_list)
                self.ui.pause_btn.setText("Tạm dừng")
                self.__pausing = False
            elif not self.__pausing:
                self.cur_fit.pause()
                self.ui.pause_btn.setText("Tiếp tục")
                self.__pausing = True
            else:
                self.cur_fit.play()
                self.ui.pause_btn.setText("Tạm dừng")
                self.__pausing = False

    def kill_oj(self):
        if self.cur_fit is not None:
            self.cur_fit.kill_oj()
