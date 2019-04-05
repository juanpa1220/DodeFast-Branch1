from GUI.DodeIDE import *
from GUI.syntax import *
from LexicalAnalysis.LexicalAnalizer import *
from SintacticAnalysis.SintacticAnalizer import *


class MainWindow(QtWidgets.QMainWindow, Ui_DodeIDE):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.CompileButton.clicked.connect(self.startCompile)
        self.SaveButton.clicked.connect(self.SaveFile)
        self.OpenFileButton.clicked.connect(self.OpenFile)
        self.highlight = PythonHighlighter(self.CodeTextArea.document())
        self.setStyleSheet("background-color: gray;")

        self.OutputArea.setStyleSheet(
            """QPlainTextEdit {background-color: #333;
                               color: #00FF00;
                               text-decoration: underline;
                               font-family: Courier;}""")

        self.CodeTextArea.setStyleSheet(
            """QPlainTextEdit {background-color: #333;
                                color: #ffffff;
                               }""")

    def startCompile(self):
        print("Compile")
        self.OutputArea.clear()

        code = self.CodeTextArea.toPlainText()

        if code != "":
            lexicalAnalizer(code, self)
            sintacticAnalizer(code, self)
        else:
            self.OutputArea.setPlainText(">> ERROR: Debe ingresar un código válido antes de compilar.\n")

    def SaveFile(self):
        text = self.CodeTextArea.toPlainText()
        if text != "":
            name = QtWidgets.QFileDialog.getSaveFileName(self, "Save file")
            name = name[0]
            if name[-4:] != ".txt":
                name += ".txt"
            file = open(name, 'w')
            file.write(text)

    def OpenFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, "Open file")
        file = open(name[0], 'r')
        self.CodeTextArea.clear()
        self.CodeTextArea.insertPlainText(file.read())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
