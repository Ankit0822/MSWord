from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import sys


class MSWord(QMainWindow):
    def __init__(self):
        super(MSWord, self).__init__()
        self.editor = QTextEdit()
        self.font_size = QSpinBox()
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.setWindowTitle("MS Word Clone")
        self.create_toolbar()
        
        self.editor.setFontPointSize(15)
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = QMenuBar()

        file_menu = QMenu('File', self)
        menu_bar.addMenu(file_menu)

        save_pdf = QAction('save as pdf', self)
        save_pdf.triggered.connect(self.save_as_pdf)
        file_menu.addAction(save_pdf)

        edit_menu = QMenu('Edit', self)
        menu_bar.addMenu(edit_menu)

        view_menu = QMenu('View', self)
        menu_bar.addMenu(view_menu)

        self.setMenuBar(menu_bar)


    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        undo = QAction(QIcon('undo.png'),'undo', self)
        undo.triggered.connect(self.editor.undo)
        toolbar.addAction(undo)

        redo = QAction(QIcon('redo.png'),'redo', self)
        redo.triggered.connect(self.editor.redo)
        toolbar.addAction(redo)

        toolbar.addSeparator()
        toolbar.addSeparator()

        cut = QAction(QIcon('cut.png'),'cut', self)
        cut.triggered.connect(self.editor.cut)
        toolbar.addAction(cut)

        copy = QAction(QIcon('copy.png'),'copy', self)
        copy.triggered.connect(self.editor.copy)
        toolbar.addAction(copy)

        paste = QAction(QIcon('paste.png'),'paste', self)
        paste.triggered.connect(self.editor.paste)
        toolbar.addAction(paste)

        toolbar.addSeparator()
        toolbar.addSeparator()

        self.font_size.setValue(15)
        self.font_size.valueChanged.connect(self.set_font)
        toolbar.addWidget(self.font_size)

    def set_font(self):
        font_value = self.font_size.value()
        self.editor.setFontPointSize(font_value)

    def save_as_pdf(self):
        path, _ = QFileDialog.getSaveFileName(self, 'Export PDF',None,'PDF Files (*.pdf)')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(path)
        self.editor.document().print_(printer)



app = QApplication(sys.argv)
w = MSWord()
w.show()
sys.exit(app.exec_())