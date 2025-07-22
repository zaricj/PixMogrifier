# droppable_listwidget.py
from PySide6.QtWidgets import QListWidget
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDropEvent
from pathlib import Path
from PIL import Image


class DroppableListWidget(QListWidget):
    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.allowed_extensions = {'.png', '.jpeg', '.jpg', '.ico'}
        self.ui = ui

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = Path(url.toLocalFile())
                with Image.open(file_path) as image:
                    width, height = image.width, image.height
                display_text = f"{file_path} ----- {width}x{height}"
                if file_path.is_file() and file_path.suffix.lower() in self.allowed_extensions:
                    self.addItem(str(display_text))
                else:
                    self.ui.statusbar.showMessage("Unsupported file, only images allowed.")
            event.acceptProposedAction()
