import sys

from pathlib import Path
from typing import List

from PySide6 import QtWidgets
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, QLineEdit, QTableWidgetItem)
from PySide6.QtGui import QCloseEvent, QPixmap
from PySide6.QtCore import Slot, QSettings, Qt

from resources.ui.ImageFileConverter_ui import Ui_MainWindow
from widgets.CustomQTableWidget import DroppableTableWidget
from modules.converter import Converter

# Constants
APP_NAME: str = "Image Converter"
APP_VERSION: str = "0.1.0"
APP_AUTHOR: str = "Jovan"

# from resources.qrc import ImageFileConverter_rc

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create and set up the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.replace_tablewidget_with_custom()
        self.setup_connections()
        
        # Init the converter object
        self.converter = Converter()
        self.on_conversion_start_signals(self.converter)


        # Settings file for storing application settings
        self.settings = QSettings("Jovan", "ImageConverter")

        # Window geometry restoration
        geometry = self.settings.value("geometry", bytes())
        if geometry:
            self.restoreGeometry(geometry)
    
    
    def setup_connections(self):
        # Setup the Qtablewidget and it's headers
        self.ui.tablewidget_bulk_conversion.setColumnCount(3)
        self.ui.tablewidget_bulk_conversion.setHorizontalHeaderLabels(["Filename", "Width x Height", "Extension"])
        header = self.ui.tablewidget_bulk_conversion.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        
        
        # Main button event of the whole app!
        self.ui.button_convert.clicked.connect(self.on_conversion_start)
        
        # Browse Buttons Connections
        self.ui.button_browse_save_image_to.clicked.connect(lambda: self.browse_folder_helper("Save files in folder", self.ui.line_edit_save_image_to))
        self.ui.button_bulk_conversion_browse_files.clicked.connect(self.bulk_conversion_browse_files)
        
        # Remove selected and all for list widget
        self.ui.button_remove_selected.clicked.connect(self.on_remove_item)
        self.ui.button_remove_all.clicked.connect(self.on_remove_all)
        
        # ListWidget click event
        self.ui.tablewidget_bulk_conversion.itemClicked.connect(self.set_image_width_and_height_in_spinbox)
        
        
    def replace_tablewidget_with_custom(self):
        parent = self.ui.tablewidget_bulk_conversion.parent()
        layout = self.ui.tablewidget_bulk_conversion.parent().layout()
        old_widget = self.ui.tablewidget_bulk_conversion

        index = layout.indexOf(old_widget)
        layout.removeWidget(old_widget)
        old_widget.deleteLater()

        custom_widget = DroppableTableWidget(parent, self.ui)
        custom_widget.setObjectName("tablewidget_bulk_conversion")
        layout.insertWidget(index, custom_widget)

        self.ui.tablewidget_bulk_conversion = custom_widget

    
    def set_image_width_and_height_in_spinbox(self):
        try:
            current_row = self.ui.tablewidget_bulk_conversion.currentRow()
            if current_row == -1:
                return  # No selection made

            item = self.ui.tablewidget_bulk_conversion.item(current_row, 0)
            if item is not None: # Check after remove
                image_path = Path(item.data(Qt.UserRole))  # Use stored full path

                size = Converter.get_selected_image_size(image_path)
                if size is not None:
                    width, height = size
                    self.ui.spinbox_resize_image_width.setValue(width)
                    self.ui.spinbox_resize_image_height.setValue(height)

                # Set image preview at the same time
                preview_ready_image = Converter.resize_image_for_preview(image_path, 400, 500)
                self.set_preview_image(preview_ready_image)
                
        except Exception as ex:
            QMessageBox.critical(self, f"{type(ex).__name__} Exception", str(ex))
    
    # Label Image Preview method
    def set_preview_image(self, input_file: Path) -> None:
        try:
            pix = QPixmap(input_file)
            self.ui.label_image_preview.setPixmap(pix)
        except Exception as ex:
            QMessageBox.critical(self, f"{type(ex).__name__} Exception", str(ex))


    # Main method which converts all images that have been added to list
    def on_conversion_start(self):
        ui_output_file = Path(self.ui.line_edit_save_image_to.text()) # For single file = full path, for bulk = output directory
        ui_output_extension_type  = self.ui.combobox_extension_type.currentText() # Target extension, e.g., "png", "ico"
        ui_input_files_bulk = self.gather_items_for_bulk_conversion() # List of files for bulk conversion
        ui_resize_width  = int(self.ui.spinbox_resize_image_width.text()) # Target width for resizing, 0 means no resize
        ui_resize_height = int(self.ui.spinbox_resize_image_height.text()) # Target height for resizing, 0 means no resize
        
        self.converter.settings.output_directory = ui_output_file
        self.converter.settings.output_extension_type = ui_output_extension_type
        self.converter.settings.input_files_bulk = ui_input_files_bulk
        self.converter.settings.resize_width = ui_resize_width
        self.converter.settings.resize_height = ui_resize_height
    
        self.converter.start_conversion_process()
    
    
    def gather_items_for_bulk_conversion(self) -> List[Path]:
        try:
            files: List[Path] = [] 
            if self.ui.tablewidget_bulk_conversion.rowCount():
                for i in range(self.ui.tablewidget_bulk_conversion.rowCount()):
                    item = self.ui.tablewidget_bulk_conversion.item(i, 0) # Row is i, Column is 0 which is the filename 
                    full_path = item.data(Qt.UserRole) # Gets the hidden file path
                    print(f"Gather Itmes for Bulk Conv, variable 'full_path'={full_path}")
                    files.append(Path(full_path)) # Use only file path which is index 0
            return files
        except TypeError as te:
            message = f"An exception of TypeError occurred.\nError message: {str(te)}"
            QMessageBox.critical(self, "TypeError Exception", message)
            
            
    def on_remove_item(self) -> None:
        try:
            current_item_text = self.ui.tablewidget_bulk_conversion.currentItem().text()
            current_item_row = self.ui.tablewidget_bulk_conversion.currentRow()
            if current_item_row != -1:
                self.ui.tablewidget_bulk_conversion.removeRow(current_item_row)
                # Reset the spinboxes to 0
                self.ui.spinbox_resize_image_width.setValue(0)
                self.ui.spinbox_resize_image_height.setValue(0)
                self.ui.statusbar.showMessage(f"Removed {current_item_text} from list.", 6000)
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. Arguments: {ex.args!r}"
            QMessageBox.critical(self, f"Exception {type(ex).__name__}", message)
            
            
    def on_remove_all(self) -> None:
        try:
            reply = QMessageBox.question(self, "Delete all items", "Do you really want to clear the list?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            
            if reply == QMessageBox.Yes:
                if self.ui.tablewidget_bulk_conversion.rowCount() > 0:
                    all_rows = self.ui.tablewidget_bulk_conversion.rowCount()
                    for i in reversed(range(0, all_rows)):
                        self.ui.tablewidget_bulk_conversion.removeRow(i)
                    self.ui.statusbar.showMessage("Deleted all items from list.", 6000)
                else:
                    self.ui.statusbar.showMessage("No items to delete.", 6000)
            else:
                return 
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. Arguments: {ex.args!r}"
            QMessageBox.critical(self, f"Exception {type(ex).__name__}", message)
            
            
    def on_conversion_start_signals(self, worker):
        worker.signals.statusbar_progress_text.connect(self.on_progress_text)
        worker.signals.messagebox_error.connect(self.on_messagebox_error)
        worker.signals.messagebox_warning.connect(self.on_messagebox_warning)
        worker.signals.messagebox_info.connect(self.on_messagebox_info)
    
    @Slot(str)
    def on_progress_text(self, message: str):
        self.ui.statusbar.showMessage(message)
    
    @Slot(str, str)
    def on_messagebox_error(self, title: str, message: str):
        QMessageBox.critical(self, title, message)
        
    @Slot(str, str)
    def on_messagebox_warning(self, title: str, message: str):
        QMessageBox.warning(self, title, message)
        
    @Slot(str, str)
    def on_messagebox_info(self, title: str, message: str):
        QMessageBox.information(self, title, message)

    # === Helper Methods === #
    
            
    def bulk_conversion_browse_files(self):
        try:
            file_paths, filters = QFileDialog.getOpenFileNames(self, "Browse Files", "", "Image Files (*.png *.jpeg *.jpg *.ico)")
            if file_paths:
                for file_path in file_paths:
                    
                    file_data = self.converter.get_image_file_data(Path(file_path))
                    if file_data:
                        file_name, extension, width, height = file_data
                        
                    # QTableWidgetItems
                    item = QTableWidgetItem(file_name)
                    item.setData(Qt.UserRole, Path(file_path))
                    item.setToolTip(file_path)
                    
                    # Insert new row
                    row = self.ui.tablewidget_bulk_conversion.rowCount()
                    self.ui.tablewidget_bulk_conversion.insertRow(row)
                    self.ui.tablewidget_bulk_conversion.setItem(row, 0, item) # Add the filename but internally it's the full path
                    self.ui.tablewidget_bulk_conversion.setItem(row, 1, QTableWidgetItem(str(f"{width}x{height}")))
                    self.ui.tablewidget_bulk_conversion.setItem(row, 2, QTableWidgetItem(str(extension)))
                    
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. Arguments: {ex.args!r}"
            QMessageBox.critical(self, f"Exception {type(ex).__name__}", message)
            
            
    def browse_folder_helper(self, dialog_message: str, line_widget: QLineEdit) -> None:
        """File dialog for folder browsing, sets the path of the selected folder in a specified QLineEdit Widget

        Args:
            dialog_message (str): Title message for the QFileDialog to display
            line_widget (QLineEdit): The QLineEdit Widget to write to the path value as string
        """
        try:
            folder = QFileDialog.getExistingDirectory(self, dialog_message)
            if folder:
                # Set the file path in the QLineEdit Widget
                line_widget.setText(folder)
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. Arguments: {ex.args!r}"
            QMessageBox.critical(self, "An exception occurred in browse folder method", message)


    def browse_file_helper(self, dialog_message: str, line_widget: QLineEdit, file_extension_filter: str) -> None:
        """File dialog for file browsing, sets the path of the selected file in a specified QLineEdit Widget

        Args:
            dialog_message (str): Title message for the QFileDialog to display
            line_widget (QLineEdit): The QLineEdit Widget to write to the path value as string
            file_extension_filter (str): Filter files for selection based on set filter.

                - Example for only XML files:
                    - 'XML File (*.xml)'

                - Example for multiple filters:
                    - 'Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)'
        """
        try:
            file_name, _ = QFileDialog.getOpenFileName(self, caption=dialog_message, filter=file_extension_filter)
            if file_name:
                line_widget.setText(file_name)  # Set the file path in the QLineEditWidget
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. Arguments: {ex.args!r}"
            QMessageBox.critical(self, "An exception occurred in browse folder method", message)
            
    
    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(
            self, 'Exit Program', 'Are you sure you want to exit the program?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.No:
            event.ignore()
            return
        else:
            Converter.cleanup_temp_folder()
            self.settings.setValue("geometry", self.saveGeometry())
            super().closeEvent(event)


if __name__ == "__main__":
    # Initialize the application
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())