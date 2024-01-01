# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workspace\NTU_project\ThucTapCoSo\Simulating RAM MAP\Views\DemoFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DemoFrame(object):
    def setupUi(self, DemoFrame):
        DemoFrame.setObjectName("DemoFrame")
        DemoFrame.resize(1400, 610)
        DemoFrame.setStyleSheet("\n"
"* {\n"
"    color: #f0f0f0;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
".QPushButton {\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#back_btn, #pause_btn {\n"
"    background-color: #6e5f5f;\n"
"}\n"
"\n"
"#bodyContainer {\n"
"    background-color: #3D3D3D;\n"
"}\n"
"\n"
"\n"
"#speed075_btn, #speed125_btn  {\n"
"    background-color: #666666;\n"
"}\n"
"\n"
"#speed1_btn {\n"
"    background-color: #999999;\n"
"}\n"
"\n"
"\n"
"\n"
"#detailBox_fr {\n"
"    background-color: #4B4B4B;\n"
"    border-radius: 6px;\n"
"    border: 1px solid #262626;\n"
"}\n"
"\n"
"#animationContainer {\n"
"    border-radius: 6px;\n"
"    background-color: #939393;\n"
"}\n"
"\n"
"#animationMainBox {\n"
"    background-color: #696969;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#bestfit_lb, #worstfit_lb, #firstfit_lb, #nextfit_lb {\n"
"    border-radius: 6px;\n"
"    padding: 4px 6px;\n"
"    background-color: #4e4e4e;\n"
"}\n"
"\n"
"#ramScrollArea, #ramBar_w, #tempScrollArea, #tempBar_w, #bottomScrollArea, #bottomBar_w, #fragmentOVBar, #processOVBar, #processOVScroll, #fragmentScroll {\n"
"    background-color: rgba(255,255,255,0);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#processScrollArea, #processBar_w {\n"
"    background-color: #5C5959;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::vertical {\n"
"    background : lightgrey; \n"
"    width: 4px;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(DemoFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bodyContainer = QtWidgets.QWidget(DemoFrame)
        self.bodyContainer.setObjectName("bodyContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bodyContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.navbar = QtWidgets.QWidget(self.bodyContainer)
        self.navbar.setMinimumSize(QtCore.QSize(0, 60))
        self.navbar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.navbar.setObjectName("navbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.navbar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.navbar)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back_btn = QtWidgets.QPushButton(self.frame)
        self.back_btn.setMinimumSize(QtCore.QSize(80, 36))
        self.back_btn.setMaximumSize(QtCore.QSize(100, 46))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(62)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_2.addWidget(self.back_btn)
        self.pause_btn = QtWidgets.QPushButton(self.frame)
        self.pause_btn.setMinimumSize(QtCore.QSize(80, 36))
        self.pause_btn.setMaximumSize(QtCore.QSize(100, 46))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(62)
        self.pause_btn.setFont(font)
        self.pause_btn.setObjectName("pause_btn")
        self.horizontalLayout_2.addWidget(self.pause_btn)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.navbar)
        self.contentContainer = QtWidgets.QWidget(self.bodyContainer)
        self.contentContainer.setObjectName("contentContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.contentContainer)
        self.horizontalLayout_3.setContentsMargins(0, 20, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.contentContainer)
        self.frame_2.setMinimumSize(QtCore.QSize(600, 514))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_9.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(52)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.speed075_btn = QtWidgets.QPushButton(self.frame_9)
        self.speed075_btn.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(62)
        self.speed075_btn.setFont(font)
        self.speed075_btn.setObjectName("speed075_btn")
        self.horizontalLayout_5.addWidget(self.speed075_btn)
        self.speed1_btn = QtWidgets.QPushButton(self.frame_9)
        self.speed1_btn.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(62)
        self.speed1_btn.setFont(font)
        self.speed1_btn.setObjectName("speed1_btn")
        self.horizontalLayout_5.addWidget(self.speed1_btn)
        self.speed125_btn = QtWidgets.QPushButton(self.frame_9)
        self.speed125_btn.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(62)
        self.speed125_btn.setFont(font)
        self.speed125_btn.setObjectName("speed125_btn")
        self.horizontalLayout_5.addWidget(self.speed125_btn)
        self.horizontalLayout_6.addWidget(self.frame_9)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 600))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setContentsMargins(0, 40, 0, 100)
        self.verticalLayout_5.setSpacing(40)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.firstfit_lb = QtWidgets.QLabel(self.frame_8)
        self.firstfit_lb.setMinimumSize(QtCore.QSize(0, 36))
        self.firstfit_lb.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(62)
        self.firstfit_lb.setFont(font)
        self.firstfit_lb.setObjectName("firstfit_lb")
        self.verticalLayout_5.addWidget(self.firstfit_lb)
        self.nextfit_lb = QtWidgets.QLabel(self.frame_8)
        self.nextfit_lb.setMinimumSize(QtCore.QSize(0, 36))
        self.nextfit_lb.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(62)
        self.nextfit_lb.setFont(font)
        self.nextfit_lb.setObjectName("nextfit_lb")
        self.verticalLayout_5.addWidget(self.nextfit_lb)
        self.bestfit_lb = QtWidgets.QLabel(self.frame_8)
        self.bestfit_lb.setMinimumSize(QtCore.QSize(0, 36))
        self.bestfit_lb.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(62)
        self.bestfit_lb.setFont(font)
        self.bestfit_lb.setObjectName("bestfit_lb")
        self.verticalLayout_5.addWidget(self.bestfit_lb)
        self.worstfit_lb = QtWidgets.QLabel(self.frame_8)
        self.worstfit_lb.setMinimumSize(QtCore.QSize(0, 36))
        self.worstfit_lb.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(62)
        self.worstfit_lb.setFont(font)
        self.worstfit_lb.setObjectName("worstfit_lb")
        self.verticalLayout_5.addWidget(self.worstfit_lb)
        self.verticalLayout_4.addWidget(self.frame_8, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.detailBox_fr = QtWidgets.QFrame(self.frame_5)
        self.detailBox_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detailBox_fr.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.detailBox_fr.setObjectName("detailBox_fr")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.detailBox_fr)
        self.verticalLayout_6.setContentsMargins(0, 10, 10, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_10 = QtWidgets.QFrame(self.detailBox_fr)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(62)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.verticalLayout_6.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.detailBox_fr)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.processOVScroll = QtWidgets.QScrollArea(self.frame_13)
        self.processOVScroll.setWidgetResizable(True)
        self.processOVScroll.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.processOVScroll.setObjectName("processOVScroll")
        self.processOVBar = QtWidgets.QWidget()
        self.processOVBar.setGeometry(QtCore.QRect(0, 0, 512, 392))
        self.processOVBar.setObjectName("processOVBar")
        self.processOVBar_lo = QtWidgets.QVBoxLayout(self.processOVBar)
        self.processOVBar_lo.setContentsMargins(12, 6, 12, -1)
        self.processOVBar_lo.setObjectName("processOVBar_lo")
        self.processOVScroll.setWidget(self.processOVBar)
        self.verticalLayout_10.addWidget(self.processOVScroll)
        self.verticalLayout_8.addWidget(self.frame_13)
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8.addWidget(self.frame_12)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.horizontalLayout_4.addWidget(self.detailBox_fr)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.animationArea = QtWidgets.QFrame(self.contentContainer)
        self.animationArea.setMinimumSize(QtCore.QSize(600, 0))
        self.animationArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.animationArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.animationArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.animationArea.setObjectName("animationArea")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.animationArea)
        self.verticalLayout_11.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.animationContainer = QtWidgets.QFrame(self.animationArea)
        self.animationContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.animationContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.animationContainer.setObjectName("animationContainer")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.animationContainer)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.animationMainBox = QtWidgets.QFrame(self.animationContainer)
        self.animationMainBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.animationMainBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.animationMainBox.setObjectName("animationMainBox")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.animationMainBox)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_17 = QtWidgets.QFrame(self.animationMainBox)
        self.frame_17.setMinimumSize(QtCore.QSize(210, 0))
        self.frame_17.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_13.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.ramScrollArea = QtWidgets.QScrollArea(self.frame_17)
        self.ramScrollArea.setWidgetResizable(True)
        self.ramScrollArea.setObjectName("ramScrollArea")
        self.ramBar_w = QtWidgets.QWidget()
        self.ramBar_w.setGeometry(QtCore.QRect(0, 0, 168, 386))
        self.ramBar_w.setObjectName("ramBar_w")
        self.ramBar_lo = QtWidgets.QVBoxLayout(self.ramBar_w)
        self.ramBar_lo.setContentsMargins(0, 0, 0, 0)
        self.ramBar_lo.setSpacing(0)
        self.ramBar_lo.setObjectName("ramBar_lo")
        self.ramScrollArea.setWidget(self.ramBar_w)
        self.verticalLayout_13.addWidget(self.ramScrollArea)
        self.horizontalLayout_9.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.animationMainBox)
        self.frame_18.setMinimumSize(QtCore.QSize(210, 0))
        self.frame_18.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.tempScrollArea = QtWidgets.QScrollArea(self.frame_18)
        self.tempScrollArea.setWidgetResizable(True)
        self.tempScrollArea.setObjectName("tempScrollArea")
        self.tempBar_w = QtWidgets.QWidget()
        self.tempBar_w.setGeometry(QtCore.QRect(0, 0, 190, 388))
        self.tempBar_w.setObjectName("tempBar_w")
        self.tempBar_lo = QtWidgets.QVBoxLayout(self.tempBar_w)
        self.tempBar_lo.setContentsMargins(0, 0, 0, 0)
        self.tempBar_lo.setSpacing(0)
        self.tempBar_lo.setObjectName("tempBar_lo")
        self.tempScrollArea.setWidget(self.tempBar_w)
        self.verticalLayout_15.addWidget(self.tempScrollArea)
        self.horizontalLayout_9.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.animationMainBox)
        self.frame_19.setMinimumSize(QtCore.QSize(210, 0))
        self.frame_19.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.processScrollArea = QtWidgets.QScrollArea(self.frame_19)
        self.processScrollArea.setWidgetResizable(True)
        self.processScrollArea.setObjectName("processScrollArea")
        self.processBar_w = QtWidgets.QWidget()
        self.processBar_w.setGeometry(QtCore.QRect(0, 0, 190, 388))
        self.processBar_w.setObjectName("processBar_w")
        self.processBar_lo = QtWidgets.QVBoxLayout(self.processBar_w)
        self.processBar_lo.setContentsMargins(0, 0, 0, 0)
        self.processBar_lo.setSpacing(12)
        self.processBar_lo.setObjectName("processBar_lo")
        self.processScrollArea.setWidget(self.processBar_w)
        self.verticalLayout_14.addWidget(self.processScrollArea)
        self.horizontalLayout_9.addWidget(self.frame_19)
        self.verticalLayout_12.addWidget(self.animationMainBox)
        self.animationBottomBox = QtWidgets.QFrame(self.animationContainer)
        self.animationBottomBox.setMinimumSize(QtCore.QSize(0, 80))
        self.animationBottomBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.animationBottomBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.animationBottomBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.animationBottomBox.setObjectName("animationBottomBox")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.animationBottomBox)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.bottomScrollArea = QtWidgets.QScrollArea(self.animationBottomBox)
        self.bottomScrollArea.setWidgetResizable(True)
        self.bottomScrollArea.setObjectName("bottomScrollArea")
        self.bottomBar_w = QtWidgets.QWidget()
        self.bottomBar_w.setGeometry(QtCore.QRect(0, 0, 668, 98))
        self.bottomBar_w.setObjectName("bottomBar_w")
        self.bottomBar_lo = QtWidgets.QHBoxLayout(self.bottomBar_w)
        self.bottomBar_lo.setContentsMargins(20, 0, 20, 0)
        self.bottomBar_lo.setObjectName("bottomBar_lo")
        self.bottomScrollArea.setWidget(self.bottomBar_w)
        self.horizontalLayout_10.addWidget(self.bottomScrollArea)
        self.verticalLayout_12.addWidget(self.animationBottomBox)
        self.verticalLayout_11.addWidget(self.animationContainer)
        self.horizontalLayout_3.addWidget(self.animationArea)
        self.verticalLayout_2.addWidget(self.contentContainer)
        self.verticalLayout.addWidget(self.bodyContainer)

        self.retranslateUi(DemoFrame)
        QtCore.QMetaObject.connectSlotsByName(DemoFrame)

    def retranslateUi(self, DemoFrame):
        _translate = QtCore.QCoreApplication.translate
        DemoFrame.setWindowTitle(_translate("DemoFrame", "Form"))
        self.back_btn.setText(_translate("DemoFrame", "Quay lại"))
        self.pause_btn.setText(_translate("DemoFrame", "Tạm dừng"))
        self.speed075_btn.setText(_translate("DemoFrame", "x0.75"))
        self.speed1_btn.setText(_translate("DemoFrame", "x1"))
        self.speed125_btn.setText(_translate("DemoFrame", "x1.25"))
        self.firstfit_lb.setText(_translate("DemoFrame", "First Fit"))
        self.nextfit_lb.setText(_translate("DemoFrame", "Next Fit"))
        self.bestfit_lb.setText(_translate("DemoFrame", "Best Fit"))
        self.worstfit_lb.setText(_translate("DemoFrame", "Worst Fit"))
        self.label_5.setText(_translate("DemoFrame", "Chi tiết"))
from Views import resourse_rc
