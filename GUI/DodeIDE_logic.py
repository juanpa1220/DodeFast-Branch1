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



    def startCompile(self):

        print("Compile")
        self.OutputArea.clear()

        code = self.CodeTextArea.toPlainText()

        lexicalAnalizer(code, self)

        sintacticAnalizer(code, self)

    def SaveFile(self):

        print("Save file")

    def OpenFile(self):

        print("OpenFile")

    def changeOutputText(self):
        print("hola")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()




