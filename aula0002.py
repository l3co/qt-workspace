import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication()

botao = QPushButton('Texto do Botão')
botao.show()

app.exec()