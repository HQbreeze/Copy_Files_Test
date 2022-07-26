"""
=======================================================
@Project --- File : PythonProjects --- test_win
@Author : 黄强
@Date   : 2022/7/21 14:55
1-功能描述:

2-实现步骤:
=======================================================
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QInputDialog, QTextBrowser, QPushButton


# class CopyFilesTool(QWidget):
#
#     def __init__(self):  # 初始化，直接加载
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         window_main = QMainWindow()
#         window_main.resize(600, 500)
#         window_main.move(300, 350)
#         window_main.setWindowTitle("Linsy拷贝文件")
#
#
#         lbl1 = QLabel('Zetcode', self)
#         lbl1.move(15, 10)
#
#         lbl2 = QLabel('tutorials', self)
#         lbl2.move(35, 40)
#
#         lbl3 = QLabel('for programmers', self)
#         lbl3.move(55, 70)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Absolute')
#         self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)  # app = QApplication([])
#     # window_main = QMainWindow()
#
#     ex = CopyFilesTool()
#     sys.exit(app.exec_())


# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(500, 500, 500, 550)
#         self.setWindowTitle('CopyFileAPP')
#
#         # self.lb1 = QLabel('姓名：', self)
#         # self.lb1.move(20, 20)
#         #
#         # self.lb2 = QLabel('年龄：', self)
#         # self.lb2.move(20, 80)
#         #
#         # self.lb3 = QLabel('性别：', self)
#         # self.lb3.move(20, 140)
#         #
#         # self.lb4 = QLabel('身高（cm）：', self)
#         # self.lb4.move(20, 200)
#         #
#         # self.lb5 = QLabel('基本信息：', self)
#         # self.lb5.move(20, 260)
#         #
#         # self.lb6 = QLabel('学点编程', self)
#         # self.lb6.move(80, 20)
#         #
#         # self.lb7 = QLabel('18', self)
#         # self.lb7.move(80, 80)
#         #
#         # self.lb8 = QLabel('男', self)
#         # self.lb8.move(80, 140)
#         #
#         # self.lb9 = QLabel('175', self)
#         # self.lb9.move(120, 200)
#         #
#         # self.tb = QTextBrowser(self)
#         # self.tb.move(20, 320)
#
#         self.bt1 = QPushButton('修改姓名', self)
#         self.bt1.move(200, 20)
#
#         self.bt2 = QPushButton('修改年龄', self)
#         self.bt2.move(200, 80)
#
#         self.bt3 = QPushButton('修改性别', self)
#         self.bt3.move(200, 140)
#
#         self.bt4 = QPushButton('修改身高', self)
#         self.bt4.move(200, 200)
#
#         self.bt5 = QPushButton('修改信息', self)
#         self.bt5.move(200, 260)
#
#         self.show()  # 让页面都显示
#
#         self.bt1.clicked.connect(self.showDialog)  # 页面动作处理slot（把 button 被 点击（clicked） 的信号（signal）， 连接（connect）到了 showDialog 这样的一个 slot上，即让 showDialog 来处理 button 被 点击的操作）
#         self.bt2.clicked.connect(self.showDialog)
#         self.bt3.clicked.connect(self.showDialog)
#         self.bt4.clicked.connect(self.showDialog)
#         self.bt5.clicked.connect(self.showDialog)
#
#     def showDialog(self):
#         sender = self.sender()
#         sex = ['男', '女']
#         if sender == self.bt1:
#             text, ok = QInputDialog.getText(self, '修改姓名', '请输入姓名：')
#             if ok:
#                 self.lb6.setText(text)
#         elif sender == self.bt2:
#             text, ok = QInputDialog.getInt(self, '修改年龄', '请输入年龄：', min=1)
#             if ok:
#                 self.lb7.setText(str(text))
#         elif sender == self.bt3:
#             text, ok = QInputDialog.getItem(self, '修改性别', '请选择性别：', sex)
#             if ok:
#                 self.lb8.setText(text)
#         elif sender == self.bt4:
#             text, ok = QInputDialog.getDouble(self, '修改身高', '请输入身高：', min=1.0)
#             if ok:
#                 self.lb9.setText(str(text))
#         elif sender == self.bt5:
#             text, ok = QInputDialog.getMultiLineText(self, '修改信息', '请输入个人信息：')
#             if ok:
#                 self.tb.setText(text)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


import sys
import PyQt5
import frame01  # 刚刚转为py文件的UI文件名，我的是untitled
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = frame01.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())