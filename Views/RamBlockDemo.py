# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workspace\NTU_project\ThucTapCoSo\Simulating RAM MAP\Views\RamBlockDemo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RamBlockDemo(object):
    def setupUi(self, RamBlockDemo):
        RamBlockDemo.setObjectName("RamBlockDemo")
        RamBlockDemo.resize(520, 30)
        RamBlockDemo.setMinimumSize(QtCore.QSize(0, 30))
        RamBlockDemo.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalLayout = QtWidgets.QHBoxLayout(RamBlockDemo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainBodyContainer = QtWidgets.QFrame(RamBlockDemo)
        self.mainBodyContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainBodyContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainBodyContainer)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.mainBodyContainer)
        self.frame_2.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_2.setMaximumSize(QtCore.QSize(50, 1200))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.endCell_lb = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.endCell_lb.setFont(font)
        self.endCell_lb.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.endCell_lb.setObjectName("endCell_lb")
        self.verticalLayout.addWidget(self.endCell_lb)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.mainBodyContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.capacity_lb = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.capacity_lb.setFont(font)
        self.capacity_lb.setText("")
        self.capacity_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.capacity_lb.setObjectName("capacity_lb")
        self.horizontalLayout_3.addWidget(self.capacity_lb)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.mainBodyContainer)

        self.retranslateUi(RamBlockDemo)
        QtCore.QMetaObject.connectSlotsByName(RamBlockDemo)

    def retranslateUi(self, RamBlockDemo):
        _translate = QtCore.QCoreApplication.translate
        RamBlockDemo.setWindowTitle(_translate("RamBlockDemo", "Form"))
        self.endCell_lb.setText(_translate("RamBlockDemo", "400"))