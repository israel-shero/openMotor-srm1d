from PyQt6.QtWidgets import QFormLayout, QScrollArea, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

from motorlib.propellant import Propellant
from .collectionEditor import CollectionEditor
from .propellantPreviewWidget import PropellantPreviewWidget

class PropellantEditor(CollectionEditor):
    def __init__(self, parent):
        super().__init__(parent, False)

        layout = self.layout()
        layout.takeAt(0)
        layout.takeAt(0)
        layout.takeAt(0)

        self.contentWidget = QWidget()
        contentLayout = QVBoxLayout(self.contentWidget)
        contentLayout.setContentsMargins(0, 6, 0, 6)
        contentLayout.setSpacing(8)
        contentLayout.addLayout(self.form)
        contentLayout.addLayout(self.stats)
        contentLayout.addStretch(1)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameShape(QScrollArea.Shape.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidget(self.contentWidget)
        layout.addWidget(self.scrollArea, 1)

        self.form.setRowWrapPolicy(
            QFormLayout.RowWrapPolicy.WrapLongRows)

        self.propellantPreview = PropellantPreviewWidget()
        self.propellantPreview.hide()
        self.stats.addWidget(self.propellantPreview)

    def cleanup(self):
        self.propellantPreview.hide()
        super().cleanup()

    def setPreferences(self, pref):
        super().setPreferences(pref)
        self.propellantPreview.setPreferences(self.preferences)

    def propertyUpdate(self):
        previewProp = Propellant(self.getProperties())
        self.propellantPreview.loadPropellant(previewProp)

    def loadProperties(self, obj):
        super().loadProperties(obj)
        self.propellantPreview.show()
