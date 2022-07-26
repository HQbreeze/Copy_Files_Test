"""
=======================================================
@Project --- File : PythonProjects --- windows_frame_copyfiles
@Author : 黄强
@Date   : 2022/7/21 12:44
1-功能描述:

2-实现步骤:
=======================================================
"""
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class CopyFilesTool(QWidget):

    def __init__(self):  # 初始化，直接加载
        super().__init__()

        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = CopyFilesTool()
    sys.exit(app.exec_())