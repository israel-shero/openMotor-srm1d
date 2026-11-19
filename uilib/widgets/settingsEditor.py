from PyQt6.QtWidgets import (
    QFormLayout, QLayout, QScrollArea, QVBoxLayout, QWidget,
)
from PyQt6.QtCore import Qt

from .collectionEditor import CollectionEditor

class SettingsEditor(CollectionEditor):
    def __init__(self, parent):
        super().__init__(parent, False)

        layout = self.layout()
        layout.takeAt(0)
        layout.takeAt(0)
        layout.takeAt(0)

        content = QWidget()
        contentLayout = QVBoxLayout(content)
        contentLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        contentLayout.setContentsMargins(0, 0, 0, 0)
        contentLayout.addLayout(self.form)
        contentLayout.addLayout(self.stats)
        contentLayout.addStretch(1)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameShape(QScrollArea.Shape.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidget(content)
        layout.addWidget(self.scrollArea, 1)

        self.form.setRowWrapPolicy(
            QFormLayout.RowWrapPolicy.WrapLongRows)
