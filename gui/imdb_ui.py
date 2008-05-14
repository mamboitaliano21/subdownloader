# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imdb.ui'
#
# Created: Wed May 14 15:23:45 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_IMDBSearchDialog(object):
    def setupUi(self, IMDBSearchDialog):
        IMDBSearchDialog.setObjectName("IMDBSearchDialog")
        IMDBSearchDialog.setWindowModality(QtCore.Qt.WindowModal)
        IMDBSearchDialog.resize(QtCore.QSize(QtCore.QRect(0,0,522,406).size()).expandedTo(IMDBSearchDialog.minimumSizeHint()))
        IMDBSearchDialog.setModal(True)

        self.vboxlayout = QtGui.QVBoxLayout(IMDBSearchDialog)


        self.label = QtGui.QLabel(IMDBSearchDialog)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.hboxlayout = QtGui.QHBoxLayout()


        self.movieSearch = QtGui.QLineEdit(IMDBSearchDialog)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movieSearch.sizePolicy().hasHeightForWidth())
        self.movieSearch.setSizePolicy(sizePolicy)
        self.movieSearch.setObjectName("movieSearch")
        self.hboxlayout.addWidget(self.movieSearch)

        self.searchMovieButton = QtGui.QPushButton(IMDBSearchDialog)
        self.searchMovieButton.setObjectName("searchMovieButton")
        self.hboxlayout.addWidget(self.searchMovieButton)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.searchResultsView = ImdbListView(IMDBSearchDialog)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchResultsView.sizePolicy().hasHeightForWidth())
        self.searchResultsView.setSizePolicy(sizePolicy)
        self.searchResultsView.setAcceptDrops(True)
        self.searchResultsView.setDragEnabled(True)
        self.searchResultsView.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.searchResultsView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.searchResultsView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.searchResultsView.setGridStyle(QtCore.Qt.DotLine)
        self.searchResultsView.setObjectName("searchResultsView")
        self.vboxlayout.addWidget(self.searchResultsView)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.movieInfoButton = QtGui.QPushButton(IMDBSearchDialog)
        self.movieInfoButton.setIcon(QtGui.QIcon(":/images/imdb.jpg"))
        self.movieInfoButton.setIconSize(QtCore.QSize(32,16))
        self.movieInfoButton.setObjectName("movieInfoButton")
        self.hboxlayout1.addWidget(self.movieInfoButton)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.okButton = QtGui.QPushButton(IMDBSearchDialog)
        self.okButton.setObjectName("okButton")
        self.hboxlayout1.addWidget(self.okButton)

        self.cancelButton = QtGui.QPushButton(IMDBSearchDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout1.addWidget(self.cancelButton)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.retranslateUi(IMDBSearchDialog)
        QtCore.QMetaObject.connectSlotsByName(IMDBSearchDialog)

    def retranslateUi(self, IMDBSearchDialog):
        IMDBSearchDialog.setWindowTitle(QtGui.QApplication.translate("IMDBSearchDialog", "Search the IMDB movie", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("IMDBSearchDialog", "Enter the Movie Title or IMDB id:", None, QtGui.QApplication.UnicodeUTF8))
        self.searchMovieButton.setText(QtGui.QApplication.translate("IMDBSearchDialog", "Search Movie", None, QtGui.QApplication.UnicodeUTF8))
        self.movieInfoButton.setText(QtGui.QApplication.translate("IMDBSearchDialog", "Movie Info", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("IMDBSearchDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("IMDBSearchDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

from imdblistview import ImdbListView
import images_rc
