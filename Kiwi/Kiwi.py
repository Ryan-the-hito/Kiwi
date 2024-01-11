#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8

import codecs
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
							 QLabel, QHBoxLayout, QVBoxLayout, QLineEdit,
							 QSystemTrayIcon, QMenu, QDialog, QMenuBar, QFileDialog)
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QAction, QIcon, QColor, QMovie, QPixmap
import PyQt6.QtGui
import webbrowser
import sys
import subprocess
import signal
from bs4 import BeautifulSoup
import html2text
import urllib3
import logging
import requests
import re
import os
import shutil
from pathlib import Path
import time
from PIL import Image, ImageQt
import matplotlib
matplotlib.use('QtAgg') # 切换到TkAgg后端，您也可以尝试其他后端，比如'Qt5Agg', 'MacOSX', 'GTK3Agg'等
import matplotlib.pyplot as plt
import numpy as np
try:
	from AppKit import NSWorkspace
except ImportError:
	print("can't import AppKit -- maybe you're running python from homebrew?")
	print("try running with /usr/bin/python instead")
	exit(1)


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

BasePath = '/Applications/Kiwi.app/Contents/Resources/'
# BasePath = ''  # test

# Create the icon
icon = QIcon(BasePath + "kiwi-logo.icns")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

action3 = QAction("🥝 Switch on Kiwi!")
action3.setCheckable(True)
menu.addAction(action3)

menu.addSeparator()

action7 = QAction("⚙️ Settings")
menu.addAction(action7)

menu.addSeparator()

action2 = QAction("🆕 Check for Updates")
menu.addAction(action2)

action1 = QAction("ℹ️ About")
menu.addAction(action1)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

# create a system menu
btna4 = QAction("&Switch on Coconut!")
sysmenu = QMenuBar()
file_menu = sysmenu.addMenu("&Actions")
file_menu.addAction(btna4)


class window_about(QWidget):  # 增加说明页面(About)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 说明页面内信息
		self.setUpMainWindow()
		self.resize(400, 410)
		self.center()
		self.setWindowTitle('About')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widg1 = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'kiwi-logo.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumWidth(100)
		l1.setMaximumHeight(100)
		l1.setScaledContents(True)
		blay1 = QHBoxLayout()
		blay1.setContentsMargins(0, 0, 0, 0)
		blay1.addStretch()
		blay1.addWidget(l1)
		blay1.addStretch()
		widg1.setLayout(blay1)

		widg2 = QWidget()
		lbl0 = QLabel('Kiwi', self)
		font = PyQt6.QtGui.QFont()
		font.setFamily("Arial")
		font.setBold(True)
		font.setPointSize(20)
		lbl0.setFont(font)
		blay2 = QHBoxLayout()
		blay2.setContentsMargins(0, 0, 0, 0)
		blay2.addStretch()
		blay2.addWidget(lbl0)
		blay2.addStretch()
		widg2.setLayout(blay2)

		widg3 = QWidget()
		lbl1 = QLabel('Version 0.0.1', self)
		blay3 = QHBoxLayout()
		blay3.setContentsMargins(0, 0, 0, 0)
		blay3.addStretch()
		blay3.addWidget(lbl1)
		blay3.addStretch()
		widg3.setLayout(blay3)

		widg4 = QWidget()
		lbl2 = QLabel('Thanks for your love🤟.', self)
		blay4 = QHBoxLayout()
		blay4.setContentsMargins(0, 0, 0, 0)
		blay4.addStretch()
		blay4.addWidget(lbl2)
		blay4.addStretch()
		widg4.setLayout(blay4)

		widg5 = QWidget()
		lbl3 = QLabel('感谢您的喜爱！', self)
		blay5 = QHBoxLayout()
		blay5.setContentsMargins(0, 0, 0, 0)
		blay5.addStretch()
		blay5.addWidget(lbl3)
		blay5.addStretch()
		widg5.setLayout(blay5)

		widg6 = QWidget()
		lbl4 = QLabel('♥‿♥', self)
		blay6 = QHBoxLayout()
		blay6.setContentsMargins(0, 0, 0, 0)
		blay6.addStretch()
		blay6.addWidget(lbl4)
		blay6.addStretch()
		widg6.setLayout(blay6)

		widg7 = QWidget()
		lbl5 = QLabel('※\(^o^)/※', self)
		blay7 = QHBoxLayout()
		blay7.setContentsMargins(0, 0, 0, 0)
		blay7.addStretch()
		blay7.addWidget(lbl5)
		blay7.addStretch()
		widg7.setLayout(blay7)

		widg8 = QWidget()
		bt1 = QPushButton('The Author', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.intro)
		bt2 = QPushButton('Github Page', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(100)
		bt2.clicked.connect(self.homepage)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg8.setLayout(blay8)

		bt7 = QPushButton('Buy me a cup of coffee☕', self)
		bt7.setMaximumHeight(20)
		bt7.setMinimumWidth(215)
		bt7.clicked.connect(self.coffee)

		widg8_5 = QWidget()
		blay8_5 = QHBoxLayout()
		blay8_5.setContentsMargins(0, 0, 0, 0)
		blay8_5.addStretch()
		blay8_5.addWidget(bt7)
		blay8_5.addStretch()
		widg8_5.setLayout(blay8_5)

		widg9 = QWidget()
		bt3 = QPushButton('🍪\n¥5', self)
		bt3.setMaximumHeight(50)
		bt3.setMinimumHeight(50)
		bt3.setMinimumWidth(50)
		bt3.clicked.connect(self.donate)
		bt4 = QPushButton('🥪\n¥10', self)
		bt4.setMaximumHeight(50)
		bt4.setMinimumHeight(50)
		bt4.setMinimumWidth(50)
		bt4.clicked.connect(self.donate2)
		bt5 = QPushButton('🍜\n¥20', self)
		bt5.setMaximumHeight(50)
		bt5.setMinimumHeight(50)
		bt5.setMinimumWidth(50)
		bt5.clicked.connect(self.donate3)
		bt6 = QPushButton('🍕\n¥50', self)
		bt6.setMaximumHeight(50)
		bt6.setMinimumHeight(50)
		bt6.setMinimumWidth(50)
		bt6.clicked.connect(self.donate4)
		blay9 = QHBoxLayout()
		blay9.setContentsMargins(0, 0, 0, 0)
		blay9.addStretch()
		blay9.addWidget(bt3)
		blay9.addWidget(bt4)
		blay9.addWidget(bt5)
		blay9.addWidget(bt6)
		blay9.addStretch()
		widg9.setLayout(blay9)

		widg10 = QWidget()
		lbl6 = QLabel('© 2024 Ryan-the-hito. All rights reserved.', self)
		blay10 = QHBoxLayout()
		blay10.setContentsMargins(0, 0, 0, 0)
		blay10.addStretch()
		blay10.addWidget(lbl6)
		blay10.addStretch()
		widg10.setLayout(blay10)

		main_h_box = QVBoxLayout()
		main_h_box.addWidget(widg1)
		main_h_box.addWidget(widg2)
		main_h_box.addWidget(widg3)
		main_h_box.addWidget(widg4)
		main_h_box.addWidget(widg5)
		main_h_box.addWidget(widg6)
		main_h_box.addWidget(widg7)
		main_h_box.addWidget(widg8)
		main_h_box.addWidget(widg8_5)
		main_h_box.addWidget(widg9)
		main_h_box.addWidget(widg10)
		main_h_box.addStretch()
		self.setLayout(main_h_box)

	def intro(self):
		webbrowser.open('https://github.com/Ryan-the-hito/Ryan-the-hito')

	def homepage(self):
		webbrowser.open('https://github.com/Ryan-the-hito/Coconut')

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def donate(self):
		dlg = CustomDialog()
		dlg.exec()

	def donate2(self):
		dlg = CustomDialog2()
		dlg.exec()

	def donate3(self):
		dlg = CustomDialog3()
		dlg.exec()

	def donate4(self):
		dlg = CustomDialog4()
		dlg.exec()

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def activate(self):  # 设置窗口显示
		self.show()


class CustomDialog(QDialog):  # (About1)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat5.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay5.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog2(QDialog):  # (About2)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat10.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay10.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog3(QDialog):  # (About3)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat20.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay20.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog4(QDialog):  # (About4)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat50.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay50.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class window_update(QWidget):  # 增加更新页面（Check for Updates）
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 说明页面内信息

		self.lbl = QLabel('Current Version: v0.0.1', self)
		self.lbl.move(30, 45)

		lbl0 = QLabel('Download Update:', self)
		lbl0.move(30, 75)

		lbl1 = QLabel('Latest Version:', self)
		lbl1.move(30, 15)

		self.lbl2 = QLabel('', self)
		self.lbl2.move(122, 15)

		bt1 = QPushButton('Google Drive', self)
		bt1.setFixedWidth(120)
		bt1.clicked.connect(self.upd)
		bt1.move(150, 75)

		bt2 = QPushButton('Baidu Netdisk', self)
		bt2.setFixedWidth(120)
		bt2.clicked.connect(self.upd2)
		bt2.move(150, 105)

		self.resize(300, 150)
		self.center()
		self.setWindowTitle('Kiwi Updates')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def upd(self):
		pass

	def upd2(self):
		pass

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def activate(self):  # 设置窗口显示
		self.show()
		self.checkupdate()

	def checkupdate(self):
		targetURL = 'https://github.com/Ryan-the-hito/Kiwi/releases'
		try:
			# Fetch the HTML content from the URL
			urllib3.disable_warnings()
			logging.captureWarnings(True)
			s = requests.session()
			s.keep_alive = False  # 关闭多余连接
			response = s.get(targetURL, verify=False)
			response.encoding = 'utf-8'
			html_content = response.text
			# Parse the HTML using BeautifulSoup
			soup = BeautifulSoup(html_content, "html.parser")
			# Remove all images from the parsed HTML
			for img in soup.find_all("img"):
				img.decompose()
			# Convert the parsed HTML to plain text using html2text
			text_maker = html2text.HTML2Text()
			text_maker.ignore_links = True
			text_maker.ignore_images = True
			plain_text = text_maker.handle(str(soup))
			# Convert the plain text to UTF-8
			plain_text_utf8 = plain_text.encode(response.encoding).decode("utf-8")

			for i in range(10):
				plain_text_utf8 = plain_text_utf8.replace('\n\n\n\n', '\n\n')
				plain_text_utf8 = plain_text_utf8.replace('\n\n\n', '\n\n')
				plain_text_utf8 = plain_text_utf8.replace('   ', ' ')
				plain_text_utf8 = plain_text_utf8.replace('  ', ' ')

			pattern2 = re.compile(r'(v\d+\.\d+\.\d+)\sLatest')
			result = pattern2.findall(plain_text_utf8)
			result = ''.join(result)
			nowversion = self.lbl.text().replace('Current Version: ', '')
			if result == nowversion:
				alertupdate = result + '. You are up to date!'
				self.lbl2.setText(alertupdate)
				self.lbl2.adjustSize()
			else:
				alertupdate = result + ' is ready!'
				self.lbl2.setText(alertupdate)
				self.lbl2.adjustSize()
		except:
			alertupdate = 'No Intrenet'
			self.lbl2.setText(alertupdate)
			self.lbl2.adjustSize()


class TimeoutException(Exception):
	pass


class window3(QWidget):  # 主窗口
	def __init__(self):
		super().__init__()
		self.initUI()
		self.ReLa()

	def initUI(self):
		self.mytimer = QTimer(self)
		self.mytimer.timeout.connect(self.front_timer)
		self.backtimer = QTimer(self)
		self.backtimer.timeout.connect(self.back_timer)
		self.resttimer = QTimer(self)
		self.resttimer.timeout.connect(self.rest_timer)
		self.nowtime = 0
		self.backtime = int(codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read())

		self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
		self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

		DockRe = codecs.open(BasePath + "DockRe.txt", 'r', encoding='utf-8').read()
		if DockRe == '0':
			# AppleScript命令
			check_dock_hide_script = '''
					tell application "System Events"
					    get the autohide of dock preferences
					end tell
					'''
			# 运行AppleScript
			result = subprocess.run(["osascript", "-e", check_dock_hide_script], capture_output=True, text=True)
			# 解析输出结果
			is_dock_autohide = result.stdout.strip() == 'true'
			if is_dock_autohide:
				with open(BasePath + "DockVi.txt", 'w', encoding='utf-8') as f0:
					f0.write('1')
			if not is_dock_autohide:
				with open(BasePath + "DockVi.txt", 'w', encoding='utf-8') as f0:
					f0.write('0')

			# AppleScript命令
			toggle_dock_script = '''
					tell application "System Events" to set the autohide of dock preferences to true
					'''
			# 运行AppleScript
			subprocess.run(["osascript", "-e", toggle_dock_script])

			with open(BasePath + "DockRe.txt", 'w', encoding='utf-8') as f0:
				f0.write('1')

			os.execv(sys.executable, [sys.executable, __file__])
		if DockRe == '1':
			# get the menubar height
			screen_height = app.primaryScreen().geometry().height()
			small_height = self.screen().availableGeometry().height()
			menubar_height = screen_height - small_height

			DockVi = codecs.open(BasePath + "DockVi.txt", 'r', encoding='utf-8').read()
			# restore the dock state
			if DockVi == '0':
				# AppleScript命令
				toggle_dock_script = '''
					    tell application "System Events" to set the autohide of dock preferences to false
					    '''
				# 运行AppleScript
				subprocess.run(["osascript", "-e", toggle_dock_script])

			with open(BasePath + "menu_height.txt", 'w', encoding='utf-8') as f0:
				f0.write(str(menubar_height))
			with open(BasePath + "DockRe.txt", 'w', encoding='utf-8') as f0:
				f0.write('2')

			os.execv(sys.executable, [sys.executable, __file__])
		if DockRe == '2':
			small_height = self.screen().availableGeometry().height()
			screen_width = app.primaryScreen().geometry().width()
			screen_height = app.primaryScreen().geometry().height()

			menubar_height = int(codecs.open(BasePath + "menu_height.txt", 'r', encoding='utf-8').read())

			# AppleScript命令
			check_dock_hide_script = '''
			tell application "System Events"
				get the autohide of dock preferences
			end tell
			'''
			# 运行AppleScript
			result = subprocess.run(["osascript", "-e", check_dock_hide_script], capture_output=True, text=True)
			# 解析输出结果
			is_dock_autohide = result.stdout.strip() == 'true'

			self.window_size = 50
			if not is_dock_autohide:
				self.window_size = screen_height - small_height - menubar_height  # Menubar height = 25
			if is_dock_autohide:
				self.window_size = 50
			self.resize(screen_width, self.window_size)

			time_length = int(codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read())
			self.per_length = int(int(screen_width - (2 * self.window_size)) / time_length)

			self.l1 = QLabel(self)
			img = Image.open(BasePath + 'kiwi-logo.png')
			img_smooth_scaled0 = img.resize((self.window_size, self.window_size), Image.LANCZOS)
			qpixmap0 = QPixmap.fromImage(ImageQt.ImageQt(img_smooth_scaled0))
			self.l1.setPixmap(qpixmap0)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
			self.l1.setFixedSize(self.window_size, self.window_size)

			self.l2 = QLabel(self)
			img = Image.open(BasePath + 'cosine_plot0.png')
			img_smooth_scaled = img.resize((self.per_length, self.window_size), Image.LANCZOS)
			qpixmap = QPixmap.fromImage(ImageQt.ImageQt(img_smooth_scaled))
			self.l2.setPixmap(qpixmap)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
			self.l2.setFixedSize(self.per_length, self.window_size)
			self.l2.move(self.window_size, 0)

			self.l3 = QLabel(self)
			movie = QMovie(BasePath + 'green.gif')
			movie.setScaledSize(QSize(4*self.window_size, self.window_size))
			self.l3.setMovie(movie)
			movie.start()
			self.l3.show()
			self.l3.setFixedSize(4*self.window_size, self.window_size)
			self.l3.move(self.window_size, 0)

			home_dir = str(Path.home())
			tarname1 = "KiwiAppPath"
			fulldir1 = os.path.join(home_dir, tarname1)
			if not os.path.exists(fulldir1):
				os.mkdir(fulldir1)

			w3 = QWidget()
			blay3 = QHBoxLayout()
			blay3.setContentsMargins(0, 0, 0, 0)
			blay3.addWidget(self.l1)
			blay3.addStretch()
			w3.setLayout(blay3)

			blayend = QHBoxLayout()
			blayend.setContentsMargins(0, 0, 0, 0)
			blayend.addWidget(w3)
			self.setLayout(blayend)

			if is_dock_autohide:
				self.move(0, small_height - menubar_height)
			if not is_dock_autohide:
				self.move(0, small_height + menubar_height)
			self.show()

	def timeout_handler(self, signum, frame):
		raise TimeoutException("Timeout")

	def notify(self, CMD, title, text):
		subprocess.call(['osascript', '-e', CMD, title, text])

	def front_timer(self):
		active_app = NSWorkspace.sharedWorkspace().activeApplication()
		if active_app['NSApplicationName'] != 'loginwindow':
			# main code
			home_dir = str(Path.home())
			tarname1 = "KiwiAppPath"
			fulldir1 = os.path.join(home_dir, tarname1)
			signal.signal(signal.SIGALRM, self.timeout_handler)
			signal.alarm(60)
			try:
				# 首先是检查路径下有没有对应编号的图片，如果没有就重新计算一次
				# 如果有对应的图片就直接展示就行了
				# 达到了计数的值之后自动开始下一轮（加一个休息判断，先是5分钟的休息，然后是再来规定的25分钟）
				self.nowtime += 1
				self.backtime = self.nowtime
				SetTime = int(codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read())
				if self.nowtime <= SetTime:
					n = self.nowtime
					m = 'cosine_plot' + str(n) + '.png'
					temp_picpath = BasePath + m
					picpath = os.path.join(fulldir1, m)
					if not os.path.exists(picpath):
						x = self.window_size / 4
						# 设置图形尺寸
						fig, ax = plt.subplots(figsize=(n * self.per_length / x, 4))
						x = np.linspace(-n, n, 2000)
						y1 = np.sin(x)
						y2 = -np.sin(x)
						ax.plot(x, y1, color='#A0C844', linewidth=10)
						ax.plot(x, y2, color='#A0C844', linewidth=10)
						# 将左侧的spine移动到数据空间的0位置
						ax.spines['left'].set_position(('data', 0))
						# 将底部的spine移动到数据空间的0位置
						ax.spines['bottom'].set_position(('data', 0))
						# 去掉右侧和顶部的边界线
						ax.spines['right'].set_color('none')
						ax.spines['top'].set_color('none')
						# 设置x轴的刻度位置在底部的spine
						ax.xaxis.set_ticks_position('bottom')
						# 设置y轴的刻度位置在左侧的spine
						ax.yaxis.set_ticks_position('left')
						plt.axis('off')
						# 在保存图像前，确保不会被任何图像部件（如坐标轴标签等）影响边界
						plt.savefig(temp_picpath, dpi=300, bbox_inches='tight', pad_inches=0, transparent=True)
						plt.close(fig)
						# 打开一张图片
						img = Image.open(temp_picpath)
						# 获取图片的宽度和高度
						width, height = img.size
						# 设置剪切区域为图片的右半边
						# (left, upper, right, lower)
						crop_area = (width // 2, 0, width, height)
						# 剪切图片并保存
						right_half = img.crop(crop_area)
						right_half.save(picpath)
					# 移动主体
					img = Image.open(picpath)
					img_smooth_scaled = img.resize((n * self.per_length, self.window_size), Image.LANCZOS)
					qpixmap = QPixmap.fromImage(ImageQt.ImageQt(img_smooth_scaled))
					self.l2.setPixmap(qpixmap)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
					self.l2.setFixedSize(n * self.per_length, self.window_size)
					self.l2.move(self.window_size, 0)
					# 移动动画
					if n * self.per_length >= 3 * self.window_size:
						self.l3.move(n * self.per_length - 2 * self.window_size, 0)
				if self.nowtime == SetTime:
					CMD = '''
						on run argv
							display notification (item 2 of argv) with title (item 1 of argv)
						end run'''
					self.notify(CMD, "Kiwi: Tomato Clock at Your Dock",
								f"Time up! Take a rest now!")
					rest_length = int(codecs.open(BasePath + "RestTime.txt", 'r', encoding='utf-8').read())
					self.resttimer.start(60 * 1000 * rest_length)
				if self.nowtime > SetTime:
					self.mytimer.stop()
					self.backtimer.start(1000)
			except TimeoutException:
				CMD = '''
				on run argv
					display notification (item 2 of argv) with title (item 1 of argv)
				end run'''
				self.notify(CMD, "Kiwi: Tomato Clock at Your Dock",
							f"There seems to be an error. Please try again.")
			except Exception as e:
				with open(BasePath + 'errorfile.txt', 'w', encoding='utf-8') as f0:
					f0.write(str(e))
				CMD = '''
				on run argv
					display notification (item 2 of argv) with title (item 1 of argv)
				end run'''
				self.notify(CMD, "Kiwi: Tomato Clock at Your Dock",
							f"Error. Please try again.")
			signal.alarm(0)

	def back_timer(self):
		active_app = NSWorkspace.sharedWorkspace().activeApplication()
		if active_app['NSApplicationName'] != 'loginwindow':
			# main code
			home_dir = str(Path.home())
			tarname1 = "KiwiAppPath"
			fulldir1 = os.path.join(home_dir, tarname1)
			signal.signal(signal.SIGALRM, self.timeout_handler)
			signal.alarm(10)
			try:
				# 首先是检查路径下有没有对应编号的图片，如果没有就重新计算一次
				# 如果有对应的图片就直接展示就行了
				# 达到了计数的值之后自动开始下一轮（加一个休息判断，先是5分钟的休息，然后是再来规定的25分钟）
				self.backtime -= 1
				if self.backtime > 0:
					n = self.backtime
					m = 'cosine_plot' + str(n) + '.png'
					temp_picpath = BasePath + m
					picpath = os.path.join(fulldir1, m)
					if not os.path.exists(picpath):
						x = self.window_size / 4
						# 设置图形尺寸
						fig, ax = plt.subplots(figsize=(n * self.per_length / x, 4))
						x = np.linspace(-n, n, 2000)
						y1 = np.sin(x)
						y2 = -np.sin(x)
						ax.plot(x, y1, color='#A0C844', linewidth=10)
						ax.plot(x, y2, color='#A0C844', linewidth=10)
						# 将左侧的spine移动到数据空间的0位置
						ax.spines['left'].set_position(('data', 0))
						# 将底部的spine移动到数据空间的0位置
						ax.spines['bottom'].set_position(('data', 0))
						# 去掉右侧和顶部的边界线
						ax.spines['right'].set_color('none')
						ax.spines['top'].set_color('none')
						# 设置x轴的刻度位置在底部的spine
						ax.xaxis.set_ticks_position('bottom')
						# 设置y轴的刻度位置在左侧的spine
						ax.yaxis.set_ticks_position('left')
						plt.axis('off')
						# 在保存图像前，确保不会被任何图像部件（如坐标轴标签等）影响边界
						plt.savefig(temp_picpath, dpi=300, bbox_inches='tight', pad_inches=0, transparent=True)
						plt.close(fig)
						# 打开一张图片
						img = Image.open(temp_picpath)
						# 获取图片的宽度和高度
						width, height = img.size
						# 设置剪切区域为图片的右半边
						# (left, upper, right, lower)
						crop_area = (width // 2, 0, width, height)
						# 剪切图片并保存
						right_half = img.crop(crop_area)
						right_half.save(picpath)
					# 移动主体
					img = Image.open(picpath)
					img_smooth_scaled = img.resize((n * self.per_length, self.window_size), Image.LANCZOS)
					qpixmap = QPixmap.fromImage(ImageQt.ImageQt(img_smooth_scaled))
					self.l2.setPixmap(qpixmap)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
					self.l2.setFixedSize(n * self.per_length, self.window_size)
					self.l2.move(self.window_size, 0)
					# 移动动画
					if n * self.per_length >= 3 * self.window_size:
						self.l3.move(n * self.per_length - 2 * self.window_size, 0)
					if n * self.per_length < 3 * self.window_size:
						self.l3.move(self.window_size, 0)
				elif self.backtime == 0:
					self.backtimer.stop()
					img = Image.open(BasePath + 'cosine_plot0.png')
					img_smooth_scaled = img.resize((self.per_length, self.window_size), Image.LANCZOS)
					qpixmap = QPixmap.fromImage(ImageQt.ImageQt(img_smooth_scaled))
					self.l2.setPixmap(qpixmap)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
					self.l2.setFixedSize(self.per_length, self.window_size)
					self.l3.move(self.window_size, 0)
					self.backtime = int(codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read())
			except TimeoutException:
				CMD = '''
						on run argv
							display notification (item 2 of argv) with title (item 1 of argv)
						end run'''
				self.notify(CMD, "Kiwi: Tomato Clock at Your Dock",
							f"There seems to be an error. Please try again.")
			except Exception as e:
				with open(BasePath + 'errorfile.txt', 'w', encoding='utf-8') as f0:
					f0.write(str(e))
				CMD = '''
						on run argv
							display notification (item 2 of argv) with title (item 1 of argv)
						end run'''
				self.notify(CMD, "Kiwi: Tomato Clock at Your Dock",
							f"Error. Please try again.")
			signal.alarm(0)

	def rest_timer(self):
		self.resttimer.stop()
		self.mytimer.start(60000)
		CMD = '''
			on run argv
				display notification (item 2 of argv) with title (item 1 of argv)
			end run'''
		self.notify(CMD, "Kiwi: Tomato Clock at Your Dock",
					f"Rest ends! Concentrate now!")

	def activate(self):  # 设置窗口显示
		if action3.isChecked():
			self.mytimer.start(60000)
			CMD = '''
				on run argv
					display notification (item 2 of argv) with title (item 1 of argv)
				end run'''
			self.notify(CMD, "Kiwi: Tomato Clock at Your Dock",
						f"Concentrate now!")
			# SetTime 只是一个倍数，用来计数的。实际上每一分钟计算一次，然后到了规定的时间，就重新开始下一轮。
		if not action3.isChecked():
			if self.mytimer.isActive():
				self.mytimer.stop()
				self.backtimer.start(1000)
			if self.resttimer.isActive():
				self.resttimer.stop()

	def ReLa(self):
		ReLa = codecs.open(BasePath + "ReLa.txt", 'r', encoding='utf-8').read()
		if ReLa == '1':
			action3.setChecked(True)
			self.mytimer.start(60000)

	def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
		if e.key() == Qt.Key.Key_Escape.value:
			self.close()

	def cancel(self):  # 设置取消键的功能
		self.close()


class window4(QWidget):  # Customization settings
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 设置窗口内布局
		self.setUpMainWindow()
		self.setFixedSize(500, 180)
		self.center()
		self.setWindowTitle('Customization settings')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		self.lbl1 = QLabel('A tomato clock round (minutes): ', self)

		self.le1 = QLineEdit(self)
		self.le1.setPlaceholderText('Minutes. Numbers only, no decimal. Default=25')
		text = codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read()
		self.le1.setText(text)

		self.lbl2 = QLabel('Rest for (minutes): ', self)

		self.le2 = QLineEdit(self)
		self.le2.setPlaceholderText('Minutes. Numbers only, no decimal. Default=5')
		text2 = codecs.open(BasePath + 'RestTime.txt', 'r', encoding='utf-8').read()
		self.le2.setText(text2)

		self.btn_1 = QPushButton('Save', self)
		self.btn_1.clicked.connect(self.SetTime)
		self.btn_1.setFixedSize(150, 20)

		qw1 = QWidget()
		vbox1 = QHBoxLayout()
		vbox1.setContentsMargins(0, 0, 0, 0)
		vbox1.addStretch()
		vbox1.addWidget(self.btn_1)
		vbox1.addStretch()
		qw1.setLayout(vbox1)

		qw5 = QWidget()
		vbox5 = QHBoxLayout()
		vbox5.setContentsMargins(0, 0, 0, 0)
		vbox5.addWidget(self.lbl1)
		vbox5.addStretch()
		qw5.setLayout(vbox5)

		qw6 = QWidget()
		vbox6 = QHBoxLayout()
		vbox6.setContentsMargins(0, 0, 0, 0)
		vbox6.addWidget(self.lbl2)
		vbox6.addStretch()
		qw6.setLayout(vbox6)

		vbox2 = QVBoxLayout()
		vbox2.setContentsMargins(20, 20, 20, 20)
		vbox2.addWidget(qw5)
		vbox2.addWidget(self.le1)
		vbox2.addWidget(qw6)
		vbox2.addWidget(self.le2)
		vbox2.addWidget(qw1)
		self.setLayout(vbox2)
	
	def SetTime(self):
		if self.le1.text() != '' and self.le1.text() != '0':
			SetTime = str(int(self.le1.text()))
			with open(BasePath + "SetTime.txt", 'w', encoding='utf-8') as f0:
				f0.write(SetTime)
		if self.le2.text() != '' and self.le2.text() != '0':
			RestTime = str(int(self.le2.text()))
			with open(BasePath + "RestTime.txt", 'w', encoding='utf-8') as f0:
				f0.write(RestTime)
		home_dir = str(Path.home())
		tarname1 = "KiwiAppPath"
		fulldir1 = os.path.join(home_dir, tarname1)
		if not os.path.exists(fulldir1):
			os.mkdir(fulldir1)
		shutil.rmtree(fulldir1)
		os.mkdir(fulldir1)
		self.close()
		if action3.isChecked():
			with open(BasePath + "ReLa.txt", 'w', encoding='utf-8') as f0:
				f0.write('1')
		os.execv(sys.executable, [sys.executable, __file__])

	def totalquit(self):
		with open(BasePath + "ReLa.txt", 'w', encoding='utf-8') as f0:
			f0.write('0')
		with open(BasePath + "DockRe.txt", 'w', encoding='utf-8') as f0:
			f0.write('0')
		sys.exit(0)
	
	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
		if e.key() == Qt.Key.Key_Escape.value:
			self.close()
	
	def activate(self):  # 设置窗口显示
		text = codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read()
		self.le1.setText(text)
		text2 = codecs.open(BasePath + 'RestTime.txt', 'r', encoding='utf-8').read()
		self.le2.setText(text2)
		home_dir = str(Path.home())
		tarname1 = "KiwiAppPath"
		fulldir1 = os.path.join(home_dir, tarname1)
		if not os.path.exists(fulldir1):
			os.mkdir(fulldir1)

		w2.checkupdate()
		if w2.lbl2.text() != 'No Intrenet' and 'ready' in w2.lbl2.text():
			w2.show()

		self.show()
		self.setFocus()
		self.raise_()
		self.activateWindow()
	
	def cancel(self):  # 设置取消键的功能
		self.close()

style_sheet_ori = '''
	QTabWidget::pane {
		border: 1px solid #ECECEC;
		background: #ECECEC;
		border-radius: 9px;
}
	QTableWidget{
		border: 1px solid grey;  
		border-radius:4px;
		background-clip: border;
		background-color: #FFFFFF;
		color: #000000;
		font: 14pt Helvetica;
}
	QWidget#Main {
		border: 1px solid #ECECEC;
		background: #ECECEC;
		border-radius: 9px;
}
	QPushButton{
		border: 1px outset grey;
		background-color: #FFFFFF;
		border-radius: 4px;
		padding: 1px;
		color: #000000
}
	QPushButton:pressed{
		border: 1px outset grey;
		background-color: #0085FF;
		border-radius: 4px;
		padding: 1px;
		color: #FFFFFF
}
	QPlainTextEdit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QPlainTextEdit#edit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #FFFFFF;
		color: rgb(113, 113, 113);
		font: 14pt Helvetica;
}
	QTableWidget#small{
		border: 1px solid grey;  
		border-radius:4px;
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QLineEdit{
		border-radius:4px;
		border: 1px solid gray;
		background-color: #FFFFFF;
}
	QTextEdit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QListWidget{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
'''

if __name__ == '__main__':
	while True:
		try:
			w1 = window_about()  # about
			w2 = window_update()  # update
			w3 = window3()  # main1
			w3.setAutoFillBackground(True)
			p = w3.palette()
			p.setColor(w3.backgroundRole(), QColor('#ECECEC'))
			w3.setPalette(p)
			w4 = window4()  # CUSTOMIZING
			action1.triggered.connect(w1.activate)
			action2.triggered.connect(w2.activate)
			action3.triggered.connect(w3.activate)
			action7.triggered.connect(w4.activate)
			btna4.triggered.connect(w3.activate)
			quit.triggered.connect(w4.totalquit)
			app.setStyleSheet(style_sheet_ori)
			app.exec()
		except Exception as e:
			# 发生异常时打印错误信息
			p = "程序发生异常:" + str(e)
			with open(BasePath + "Error.txt", 'w', encoding='utf-8') as f0:
				f0.write(p)
			# 延时一段时间后重新启动程序（例如延时 5 秒）
			time.sleep(5)
			# 重启后的操作
			with open(BasePath + "ReLa.txt", 'w', encoding='utf-8') as f0:
				f0.write('1')
			# 使用 os.execv() 在当前进程中启动自身，实现自动重启
			os.execv(sys.executable, [sys.executable, __file__])
