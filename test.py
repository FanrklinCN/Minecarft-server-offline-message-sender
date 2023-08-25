import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, QDesktopWidget, QPlainTextEdit, QMessageBox
from PyQt5.QtGui import QIcon, QTextCursor
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from mcpi.minecraft import Minecraft

def open_github():
    url = QUrl("https://github.com/FanrklinCN/Minecarft-server-offline-message-sender/")
    QDesktopServices.openUrl(url)

def send_message():
    ip = ip_input.text()
    name = name_input.text()
    text = text_input.toPlainText()

    mc = Minecraft.create(ip)
    mc.postToChat("<[离线] {}> {}".format(name, text))

    QMessageBox.information(window, "提示", "消息已发送！", QMessageBox.Ok)
    
def copy_text():
    clipboard = QApplication.clipboard()
    clipboard.setText('RaspberryJuice')
    QMessageBox.information(window, "提示", "复制成功！", QMessageBox.Ok)

app = QApplication(sys.argv)

# 设置窗口图标
app_icon = QIcon("logo.png")
app.setWindowIcon(app_icon)

# 创建一个 QMainWindow 对象
main_window = QMainWindow()
main_window.setWindowTitle("Minecraft消息发送器")
main_window.setFixedSize(400, 300)

# 设置全局样式
app.setStyleSheet('''
    * {
        border-radius: 5px;
    }

    QMainWindow {
        background-color: #f0f0f0;
    }

    QLabel {
        color: #333333;
    }

    QLineEdit, QPlainTextEdit {
        background-color: #ffffff;
        border: 1px solid #aaaaaa;
        padding: 5px;
    }

    QPushButton {
        background-color: #007BFF;
        color: #ffffff;
        padding: 5px 10px;
        border: none;
    }

    QPushButton:hover {
        background-color: #0056b3;
    }

    QMessageBox {
        background-color: #ffffff;
        color: #333333;
    }
''')

window = QMainWindow()
window.setWindowTitle("Minecraft消息发送器")
window.resize(400, 300)

# 创建选项卡组件
tab_widget = QTabWidget(window)

# 创建主页选项卡
home_tab = QWidget()
home_layout = QVBoxLayout(home_tab)

# 创建文本框用于显示完整提示文本
install_text_edit = QPlainTextEdit()
install_text_edit.setReadOnly(True)
install_text_edit.setPlainText('请确保服务器已安装 RaspberryJuice 插件，如没有，请在互联网查找此插件并安装至服务器！')
home_layout.addWidget(install_text_edit)

# 创建复制按钮
copy_button = QPushButton("复制插件名")
copy_button.clicked.connect(copy_text)
home_layout.addWidget(copy_button)

ip_label = QLabel("服务器IP地址:")
ip_input = QLineEdit()
name_label = QLabel("玩家名:")
name_input = QLineEdit()
text_label = QLabel("消息内容:")
text_input = QPlainTextEdit()
send_button = QPushButton("发送消息")
send_button.clicked.connect(send_message)
home_layout.addWidget(ip_label)
home_layout.addWidget(ip_input)
home_layout.addWidget(name_label)
home_layout.addWidget(name_input)
home_layout.addWidget(text_label)
home_layout.addWidget(text_input)
home_layout.addWidget(send_button)
home_layout.addStretch(1)
tab_widget.addTab(home_tab, "主页")

# 创建关于选项卡
about_tab = QWidget()
about_layout = QVBoxLayout(about_tab)
about_layout.addWidget(QLabel("这是关于页面"))
about_layout.addWidget(QLabel("作者：THZ同学 QQ：2840519267"))
about_layout.addWidget(QLabel("反馈邮箱：thz15916108729@163.com"))
about_layout.addWidget(QLabel("Copyright © Aurora-Studio. All Rights Reserved."))
about_layout.addWidget(QLabel("Aurora-Studio 版权所有"))
github_button = QPushButton("GitHub开源库")
github_button.clicked.connect(open_github)
about_layout.addWidget(github_button)
about_layout.addStretch(1)
tab_widget.addTab(about_tab, "关于")

# 将选项卡组件添加到主窗口
window.setCentralWidget(tab_widget)

window.show()

sys.exit(app.exec_())
