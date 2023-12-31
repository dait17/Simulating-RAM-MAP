from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from Views import Ui_DemoFrame, Ui_RamBlockDemo
from .Models import *
from .fitController import BaseFit, FirstFit, NextFit


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
        self.__cur_fit_id = 0

        self.__pausing = False

    def ui_turning(self):
        self.ui.ramBar_lo.setAlignment(Qt.AlignTop)
        self.ui.processBar_lo.setAlignment(Qt.AlignTop)
        self.ui.tempBar_lo.setAlignment(Qt.AlignTop)

    def set_data(self, ram_block_list, process_list):
        self.ram_block_list = ram_block_list
        self.process_list = process_list

    def connect_action(self):
        self.ui.speed075_btn.clicked.connect(self.__set_speed_x075)
        self.ui.speed1_btn.clicked.connect(self.__set_speed_x1)
        self.ui.speed125_btn.clicked.connect(self.__set_speed_x125)

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

    def run_(self):
        if self.ram_block_list is not None and self.process_list is not None and len(self.ram_block_list) != 0 and len(
                self.process_list) != 0:
            try:
                self.next_fit()
            except Exception as e:
                print(e)

    def __control_fit(self):
        if self.__cur_fit_id<len(self.__fit_list):
            if self.cur_fit is None or not self.cur_fit.simulating:
                self.cur_fit = self.__get_fit(self.__fit_list[self.__cur_fit_id])
                self.__cur_fit_id += 1

    def next_fit(self):
        if self.cur_fit is not None:
            self.cur_fit.kill_oj()
        if self.__cur_fit_id<len(self.__fit_list):
            self.__cur_fit_id += 1
            self.cur_fit = self.cur_fit = self.__get_fit(self.__fit_list[self.__cur_fit_id])
            self.cur_fit._set_data(self.ram_block_list, self.process_list)
            self.cur_fit.start(self.speed)

    def __get_fit(self, fit_name:str):
        fit_name = fit_name.lower()
        if fit_name=='first_fit':
            pass
        elif fit_name=='next_fit':
            pass
        elif fit_name=='best_fit':
            pass
        elif fit_name=='worst_fit':
            pass
        return FirstFit(self)

    def pause_(self):
        if self.cur_fit is not None:
            if not self.__pausing:
                self.cur_fit.pause()
                self.ui.pause_btn.setText("Tiếp tục")
                self.__pausing =True

            else:
                self.cur_fit.play()
                self.ui.pause_btn.setText("Tạm dừng")
                self.__pausing = False




    def kill_oj(self):
        if self.cur_fit is not None:
            self.cur_fit.kill_oj()
