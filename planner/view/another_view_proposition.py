# -*- coding: utf-8 -*-

################################################################################
## ClassesType generated from reading UI file 'uni_planner_2FMOlIv.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGroupBox,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 696)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_plan = QWidget(self.centralwidget)
        self.widget_plan.setObjectName(u"widget_plan")
        self.widget_plan.setGeometry(QRect(30, 9, 925, 610))
        self.plainTextEdit_6 = QPlainTextEdit(self.widget_plan)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setGeometry(QRect(0, 0, 50, 20))
        self.plainTextEdit_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_6.setReadOnly(True)
        self.plainTextEdit_8 = QPlainTextEdit(self.widget_plan)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setGeometry(QRect(175, 0, 125, 20))
        font = QFont()
        font.setPointSize(8)
        self.plainTextEdit_8.setFont(font)
        self.plainTextEdit_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_9 = QPlainTextEdit(self.widget_plan)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setGeometry(QRect(300, 0, 125, 20))
        self.plainTextEdit_9.setFont(font)
        self.plainTextEdit_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_10 = QPlainTextEdit(self.widget_plan)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        self.plainTextEdit_10.setGeometry(QRect(50, 0, 125, 20))
        self.plainTextEdit_10.setFont(font)
        self.plainTextEdit_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_11 = QPlainTextEdit(self.widget_plan)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_11.setGeometry(QRect(425, 0, 125, 20))
        self.plainTextEdit_11.setFont(font)
        self.plainTextEdit_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_12 = QPlainTextEdit(self.widget_plan)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")
        self.plainTextEdit_12.setGeometry(QRect(550, 0, 125, 20))
        self.plainTextEdit_12.setFont(font)
        self.plainTextEdit_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_13 = QPlainTextEdit(self.widget_plan)
        self.plainTextEdit_13.setObjectName(u"plainTextEdit_13")
        self.plainTextEdit_13.setGeometry(QRect(675, 0, 125, 20))
        self.plainTextEdit_13.setFont(font)
        self.plainTextEdit_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_14 = QPlainTextEdit(self.widget_plan)
        self.plainTextEdit_14.setObjectName(u"plainTextEdit_14")
        self.plainTextEdit_14.setGeometry(QRect(800, 0, 125, 20))
        self.plainTextEdit_14.setFont(font)
        self.plainTextEdit_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.widget_3 = QWidget(self.widget_plan)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(50, 20, 125, 118))
        self.plainTextEdit_7 = QPlainTextEdit(self.widget_3)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setGeometry(QRect(0, 0, 121, 21))
        self.plainTextEdit_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.widget_4 = QWidget(self.widget_plan)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(175, 20, 125, 118))
        self.plainTextEdit_15 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_15.setObjectName(u"plainTextEdit_15")
        self.plainTextEdit_15.setGeometry(QRect(0, 0, 121, 21))
        self.plainTextEdit_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.widget_5 = QWidget(self.widget_plan)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(300, 20, 125, 118))
        self.plainTextEdit_16 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_16.setObjectName(u"plainTextEdit_16")
        self.plainTextEdit_16.setGeometry(QRect(0, 0, 121, 21))
        self.plainTextEdit_16.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_16.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_17 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_17.setObjectName(u"plainTextEdit_17")
        self.plainTextEdit_17.setGeometry(QRect(0, 21, 121, 21))
        self.plainTextEdit_17.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_17.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.widget_6 = QWidget(self.widget_plan)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(425, 20, 125, 118))
        self.widget_6.setMouseTracking(False)
        self.widget_7 = QWidget(self.widget_plan)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(550, 20, 125, 118))
        self.widget_8 = QWidget(self.widget_plan)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(675, 20, 125, 118))
        self.widget_9 = QWidget(self.widget_plan)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(800, 20, 125, 118))
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 30, 50, 590))
        self.plainTextEdit = QPlainTextEdit(self.widget_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 0, 50, 118))
        font1 = QFont()
        font1.setFamilies([u"Sitka Heading Semibold"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit_2 = QPlainTextEdit(self.widget_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(0, 118, 50, 118))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_3 = QPlainTextEdit(self.widget_2)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(0, 236, 50, 118))
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_4 = QPlainTextEdit(self.widget_2)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(0, 354, 50, 118))
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_5 = QPlainTextEdit(self.widget_2)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(0, 472, 50, 118))
        self.plainTextEdit_5.setReadOnly(True)
        self.widget_courses = QWidget(self.centralwidget)
        self.widget_courses.setObjectName(u"widget_courses")
        self.widget_courses.setGeometry(QRect(970, 20, 351, 531))
        self.group_box_select_courses = QGroupBox(self.widget_courses)
        self.group_box_select_courses.setObjectName(u"group_box_select_courses")
        self.group_box_select_courses.setGeometry(QRect(10, 10, 331, 361))
        self.comboBox = QComboBox(self.group_box_select_courses)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 50, 300, 20))
        self.listWidget = QListWidget(self.group_box_select_courses)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 90, 300, 20))
        self.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_2 = QListWidget(self.group_box_select_courses)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(20, 130, 300, 80))
        self.listWidget_2.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_2.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_3 = QListWidget(self.group_box_select_courses)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setGeometry(QRect(20, 230, 300, 80))
        self.listWidget_3.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_3.setDefaultDropAction(Qt.MoveAction)
        self.label_2 = QLabel(self.group_box_select_courses)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 49, 16))
        self.label_3 = QLabel(self.group_box_select_courses)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 171, 20))
        self.label_4 = QLabel(self.group_box_select_courses)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 70, 171, 16))
        self.label_5 = QLabel(self.group_box_select_courses)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 110, 171, 16))
        self.label_6 = QLabel(self.group_box_select_courses)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 210, 171, 16))
        self.label = QLabel(self.widget_courses)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 380, 311, 16))
        self.widget_detailed_course_information = QWidget(self.widget_courses)
        self.widget_detailed_course_information.setObjectName(u"widget_detailed_course_information")
        self.widget_detailed_course_information.setGeometry(QRect(10, 400, 331, 111))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1190, 570, 121, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1350, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.plainTextEdit_8.setPlainText(QCoreApplication.translate("MainWindow", u" 9:15      10:00     10:45\n"
"", None))
        self.plainTextEdit_9.setPlainText(QCoreApplication.translate("MainWindow", u"11:15     12:00     12:45", None))
        self.plainTextEdit_10.setPlainText(QCoreApplication.translate("MainWindow", u" 7:30       8:15       9:00", None))
        self.plainTextEdit_11.setPlainText(QCoreApplication.translate("MainWindow", u"11:15     12:00     12:45", None))
        self.plainTextEdit_12.setPlainText(QCoreApplication.translate("MainWindow", u"11:15     12:00     12:45", None))
        self.plainTextEdit_13.setPlainText(QCoreApplication.translate("MainWindow", u"11:15     12:00     12:45", None))
        self.plainTextEdit_14.setPlainText(QCoreApplication.translate("MainWindow", u"11:15     12:00     12:45", None))
        self.plainTextEdit_7.setPlainText(QCoreApplication.translate("MainWindow", u"K01-29a", None))
        self.plainTextEdit_15.setPlainText(QCoreApplication.translate("MainWindow", u"K01-29a", None))
        self.plainTextEdit_16.setPlainText(QCoreApplication.translate("MainWindow", u"K01-29a", None))
        self.plainTextEdit_17.setPlainText(QCoreApplication.translate("MainWindow", u"K01-29a", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"MON\n"
"", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"TUE", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"WEN", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("MainWindow", u"THU", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("MainWindow", u"FRI", None))
        self.group_box_select_courses.setTitle(QCoreApplication.translate("MainWindow", u"Select Groups", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Linux Lab", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"MSiD Lab", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"MSiD Wyklad", None))


        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"wt", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget_2.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"wt", None));
        ___qlistwidgetitem2 = self.listWidget_2.item(1)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nowy element", None));
        ___qlistwidgetitem3 = self.listWidget_2.item(2)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nowy element", None));
        ___qlistwidgetitem4 = self.listWidget_2.item(3)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nowy element", None));
        ___qlistwidgetitem5 = self.listWidget_2.item(4)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Nowy element", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled1)


        __sortingEnabled2 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem6 = self.listWidget_3.item(0)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"wt", None));
        ___qlistwidgetitem7 = self.listWidget_3.item(1)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nowy element", None));
        ___qlistwidgetitem8 = self.listWidget_3.item(2)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nowy element", None));
        ___qlistwidgetitem9 = self.listWidget_3.item(3)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nowy element", None));
        ___qlistwidgetitem10 = self.listWidget_3.item(4)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Nowy element", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled2)

        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Choose course ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"The one most prefered", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Okay ones", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Very not prefered", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Detailed Course Information", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

if __name__ == "__main__":

    app = QApplication()
    window = QMainWindow()
    Ui_MainWindow().setupUi(window)
    window.show()
    app.exec()