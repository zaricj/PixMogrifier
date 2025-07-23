# droppable_listwidget.py
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QDropEvent
from pathlib import Path
from PIL import Image


class DroppableTableWidget(QTableWidget):
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
                
                full_path = Path(url.toLocalFile()) # Full file path
                file_name = full_path.name # Only the file name
                extension = full_path.suffix # THe files extension

                # Check file type first
                if not (full_path.is_file() and full_path.suffix.lower() in self.allowed_extensions):
                    if self.ui:
                        self.ui.statusbar.showMessage("Unsupported file, only images allowed.")
                    continue

                try:
                    with Image.open(full_path) as image:
                        width, height = image.width, image.height

                    # Items
                    item = QTableWidgetItem(file_name)
                    item.setData(Qt.UserRole, full_path)  # Store full path invisibly
                    item.setToolTip(url.toLocalFile()) # Helps users, shows the actually full path to the file

                    # Insert new row
                    row = self.rowCount()
                    self.insertRow(row)
                    self.setItem(row, 0, item) # Add the filename but internally it's the full path
                    self.setItem(row, 1, QTableWidgetItem(str(f"{width}x{height}")))
                    self.setItem(row, 2, QTableWidgetItem(str(extension)))

                except Exception as e:
                    if self.ui:
                        self.ui.statusbar.showMessage(f"Error reading image: {e}")
                    print(f"Error reading {full_path}: {e}")
            event.acceptProposedAction()

