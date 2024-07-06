from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(0,0)

Text_lbl = QLabel("У якому році перший канал отримав кнопку від YouTube?")
v_2005 = QRadioButton("2005")
v_2010 = QRadioButton("2010")
v_2000 = QRadioButton("2000")
v_2015 = QRadioButton("2015")

main_line = QVBoxLayout()
main_line.addWidget(Text_lbl)

horizotal_line = QHBoxLayout()
horizotal_line.addWidget(v_2005)
horizotal_line.addWidget(v_2010)

horizotal2_line = QHBoxLayout()
horizotal2_line.addWidget(v_2000)
horizotal2_line.addWidget(v_2015)

main_line.addLayout(horizotal_line)
main_line.addLayout(horizotal2_line)
def show_win():
    win_msg  = QMessageBox()
    win_msg.setText("Ти Переміг")
    win_msg.exec()

def show_lose():
    lose_msg = QMessageBox()
    lose_msg.setText("Ти Програв")
    lose_msg.exec()

v_2005.    clicked.connect(show_win)
v_2000.    clicked.connect(show_lose)
v_2010.    clicked.connect(show_lose)
v_2015.    clicked.connect(show_lose)






window.setLayout(main_line)
window.show()
app.exec()
