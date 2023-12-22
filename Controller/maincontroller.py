from PyQt5.QtWidgets import QMainWindow
from Views import Ui_MainWindow
from .inputController import InputController
from .siController import SiController


class MainController(QMainWindow):
    def __init__(self):
        super(MainController, self).__init__()
        self.simulationFrame = None
        self.inputFrame = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__setup_input_frame()
        self.__setup_simulation_frame()

        self.setup_page()

    def __setup_input_frame(self):
        self.inputFrame = InputController()
        self.inputFrame.ui.completed_btn.clicked.connect(self.__complete_action)
        self.inputFrame.ui.start_btn.clicked.connect(self.__start_action)

    def __setup_simulation_frame(self):
        self.simulationFrame = SiController()

    def setup_page(self):
        self.ui.mainBodyContainer.addWidget(self.inputFrame)
        self.ui.mainBodyContainer.addWidget(self.simulationFrame)
        self.ui.mainBodyContainer.setCurrentIndex(0)

    def __complete_action(self):
        self.ui.mainBodyContainer.setCurrentIndex(1)

    def __start_action(self):
        self.ui.mainBodyContainer.setCurrentIndex(1)

    def __back_action(self):
        pass

