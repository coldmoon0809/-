# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:25:28 2020

@author: ACER
"""

# coding:utf-8 
from PyQt5 import QtCore,QtGui,QtWidgets 
import sys 
import qtawesome 

class MainUi(QtWidgets.QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.init_ui() 
    def init_ui(self): 
        self.setFixedSize(960,700) 
        self.main_widget = QtWidgets.QWidget() # 創建窗口主部件 
        self.main_layout = QtWidgets.QGridLayout() # 創建主部件的網格布局 
        self.main_widget.setLayout(self.main_layout) # 設置窗口主部件布局為網格布局 
        self.left_widget = QtWidgets.QWidget() # 創建左側部件
        self.left_widget.setObjectName('left_widget') 
    
        self.left_layout = QtWidgets.QGridLayout() # 創建左側部件的網格布局層 
        self.left_widget.setLayout(self.left_layout) # 設置左側部件布局為網格
        self.right_widget = QtWidgets.QWidget() # 創建右側部件 
        self.right_widget.setObjectName('right_widget') 
        self.right_layout = QtWidgets.QGridLayout() 
        self.right_widget.setLayout(self.right_layout) # 設置右側部件布局為網格 
        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左側部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右側部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget) # 設置窗口主部件
def main(): 
        app = QtWidgets.QApplication(sys.argv)
        gui = MainUi() 
        gui.show() 
        sys.exit(app.exec_()) 
if __name__ == '__main__': 
        main()
