from PyQt5.QtWidgets import QMainWindow
from Views import Ui_MainWindow
from .inputController import InputController
from .siController import SiController

from Controller.Models import *


class MainController(QMainWindow):
    def __init__(self):
        super(MainController, self).__init__()
        self.simulationFrame: SiController | None = None
        self.inputFrame: InputController | None = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__setup_input_frame()
        self.__setup_simulation_frame()

        self.ram_block_list: list[RamBlock] | None = None
        self.process_list: list[Process] | None = None

        self.setup_page()

    def __setup_input_frame(self):
        self.inputFrame = InputController()
        self.inputFrame.ui.completed_btn.clicked.connect(self.__complete_action)
        self.inputFrame.ui.start_btn.clicked.connect(self.__start_action)

    def __setup_simulation_frame(self):
        if self.simulationFrame is not None:
            self.simulationFrame.deleteLater()
        self.simulationFrame = SiController()
        self.simulationFrame.ui.back_btn.clicked.connect(self.__back_action)
        self.simulationFrame.ui.pause_btn.clicked.connect(self.simulationFrame.pause_)

    def setup_page(self):
        self.ui.mainBodyContainer.addWidget(self.inputFrame)
        self.ui.mainBodyContainer.addWidget(self.simulationFrame)
        self.ui.mainBodyContainer.setCurrentIndex(0)

    def __setup_data(self):
        self.ram_block_list = self.inputFrame.get_ram_model_list()
        self.process_list = self.inputFrame.get_process_model_list()

    def __complete_action(self):
        self.__setup_data()
        self.ui.mainBodyContainer.setCurrentIndex(1)
        self.simulationFrame.set_data(self.ram_block_list, self.process_list)

    def __start_action(self):
        self.__setup_data()
        self.ui.mainBodyContainer.setCurrentIndex(1)
        self.simulationFrame.run_()

    def __back_action(self):
        self.ui.mainBodyContainer.setCurrentIndex(0)
        self.__setup_simulation_frame()
