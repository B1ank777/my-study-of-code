import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtGui import QPainter  # 必须导入，否则 QPainter 崩溃
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QSize




class CodeEditor(QPlainTextEdit):
    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), Qt.lightGray)

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + int(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.lineNumberArea.width() - 2,
                                 self.fontMetrics().height(),
                                 Qt.AlignRight, number)
            block = block.next()
            top = bottom
            bottom = top + int(self.blockBoundingRect(block).height())
            blockNumber += 1

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont("Courier New", 10))
        self.lineNumberArea = LineNumberArea(self)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.updateLineNumberAreaWidth(0)

    def lineNumberAreaWidth(self):
        digits = len(str(max(1, self.blockCount())))
        space = 3 + self.fontMetrics().width('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(cr.left(), cr.top(),
                                        self.lineNumberAreaWidth(), cr.height())


class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.editor.lineNumberAreaPaintEvent(event)


class SimulatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('RV32 Simulator')
        self.setGeometry(100, 100, 1000, 600)

        # 顶部按钮
        control_bar = QHBoxLayout()
        buttons = ['编译', '启动', '单步', '执行', '结束']
        self.btn_group = []
        for btn in buttons:
            button = QPushButton(btn)
            button.setFixedSize(80, 30)
            control_bar.addWidget(button)
            self.btn_group.append(button)
        control_bar.addStretch()

        # 中央区域
        main_splitter = QSplitter(Qt.Horizontal)

        # 左侧代码区域
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        self.code_editor = CodeEditor()
        self.code_editor.setPlainText(self.get_sample_code())
        left_layout.addWidget(self.code_editor)
        left_widget.setLayout(left_layout)

        # 右侧寄存器区域
        right_widget = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()

        # 寄存器表格
        self.register_table = QTableWidget()
        self.register_table.setColumnCount(2)
        self.register_table.setHorizontalHeaderLabels(['寄存器号', '值'])
        self.register_table.horizontalHeader().setStretchLastSection(True)
        self.init_register_table()

        tab_layout = QVBoxLayout()
        tab_layout.addWidget(self.register_table)
        tab1.setLayout(tab_layout)

        right_widget.addTab(tab1, "Tab 1")
        right_widget.addTab(tab2, "Tab 2")

        main_splitter.addWidget(left_widget)
        main_splitter.addWidget(right_widget)
        main_splitter.setSizes([600, 400])

        # 主布局
        main_widget = QWidget()
        layout = QVBoxLayout()
        layout.addLayout(control_bar)
        layout.addWidget(main_splitter)
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def init_register_table(self):
        self.register_table.setRowCount(15)
        for i in range(15):
            self.register_table.setItem(i, 0, QTableWidgetItem(f"x{i + 1}"))
            self.register_table.setItem(i, 1, QTableWidgetItem("0x0"))

    def get_sample_code(self):
        return """"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimulatorGUI()
    ex.show()
    sys.exit(app.exec_())