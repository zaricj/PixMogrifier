import sys

from pathlib import Path
from typing import List

from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, QLineEdit)
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import Slot, QSettings

from resources.ui.ImageFileConverter_ui import Ui_MainWindow
from widgets.droppable_qlistwidget import DroppableListWidget
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
        
        self.replace_listwidget_with_custom()
        self.setup_connections()
        self.setup_converter_object()

        # Settings file for storing application settings
        self.settings = QSettings("Jovan", "ImageConverter")

        # Window geometry restoration
        geometry = self.settings.value("geometry", bytes())
        if geometry:
            self.restoreGeometry(geometry)  
    
    
    def setup_connections(self):

        self.ui.button_convert.clicked.connect(self.on_conversion_start)
        
        # Browse Buttons Connections
        self.ui.button_browse_save_image_to.clicked.connect(lambda: self.browse_folder_helper("Save files in folder", self.ui.line_edit_save_image_to))
        self.ui.button_bulk_conversion_browse_files.clicked.connect(self.bulk_conversion_browse_files)
        
        # Remove selected and all for list widget
        self.ui.button_remove_selected.clicked.connect(self.on_remove_item)
        self.ui.button_remove_all.clicked.connect(self.on_remove_all)
        
        # ListWidget click event
        self.ui.listwidget_bulk_conversion.itemClicked.connect(self.set_image_width_and_height_in_spinbox)
        

    def setup_converter_object(self):
        ui_output_file: Path = "" # For single file = full path, for bulk = output directory
        ui_output_extension_type  = "" # Target extension, e.g., "png", "ico"
        ui_input_files_bulk = [] # List of files for bulk conversion
        ui_resize_width  = 0 # Target width for resizing, 0 means no resize
        ui_resize_height = 0 # Target height for resizing, 0 means no resize
        
        self.converter = Converter(
            output_directory = ui_output_file,
            output_extension_type = ui_output_extension_type,
            input_files_bulk = ui_input_files_bulk,
            resize_width = ui_resize_width,
            resize_height = ui_resize_height
        )
    
    
    def replace_listwidget_with_custom(self):
        parent = self.ui.listwidget_bulk_conversion.parent()
        layout = self.ui.listwidget_bulk_conversion.parent().layout()
        old_widget = self.ui.listwidget_bulk_conversion

        index = layout.indexOf(old_widget)
        layout.removeWidget(old_widget)
        old_widget.deleteLater()

        custom_widget = DroppableListWidget(parent, self.ui)
        custom_widget.setObjectName("listwidget_bulk_conversion")
        layout.insertWidget(index, custom_widget)

        self.ui.listwidget_bulk_conversion = custom_widget
        
    
    def set_image_width_and_height_in_spinbox(self):
        current_row = self.ui.listwidget_bulk_conversion.currentRow()
        if current_row == -1:
            return  # No selection made

        item = self.ui.listwidget_bulk_conversion.item(current_row)
        path_text = self.item_path_splitter(item.text())
        image_path = Path(path_text[0])

        size = self.converter.get_selected_image_size(image_path)
        if size is not None:
            width, height = size
            self.ui.spinbox_resize_image_width.setValue(width)
            self.ui.spinbox_resize_image_height.setValue(height)

        
    def on_conversion_start(self):
        ui_output_file = Path(self.ui.line_edit_save_image_to.text()) # For single file = full path, for bulk = output directory
        ui_output_extension_type  = self.ui.combobox_extension_type.currentText() # Target extension, e.g., "png", "ico"
        ui_input_files_bulk = self.gather_items_for_bulk_conversion() # List of files for bulk conversion
        ui_resize_width  = int(self.ui.spinbox_resize_image_width.text()) # Target width for resizing, 0 means no resize
        ui_resize_height = int(self.ui.spinbox_resize_image_height.text()) # Target height for resizing, 0 means no resize
        
        self.converter = Converter(
            output_directory = ui_output_file,
            output_extension_type = ui_output_extension_type,
            input_files_bulk = ui_input_files_bulk,
            resize_width = ui_resize_width,
            resize_height = ui_resize_height
        )
        
        self.on_conversion_start_signals(self.converter)
        self.converter.start_conversion_process()
        
    
    def item_path_splitter(self, text: str) -> str:
        return text.split(" ----- ") #  -----  Separator set manually. Check class DroppableListWidget.
    
    def gather_items_for_bulk_conversion(self) -> List[Path]:
        try:
            files: List[Path] = [] 
            if not self.ui.listwidget_bulk_conversion.count() == 0:
                for i in range(self.ui.listwidget_bulk_conversion.count()):
                    item = self.ui.listwidget_bulk_conversion.item(i)
                    item_text = self.item_path_splitter(item.text())
                    files.append(Path(item_text[0])) # Use only file path which is index 0
            return files
        except TypeError as te:
            message = f"An exception of TypeError occurred.\nError message: {str(te)}"
            QMessageBox.critical(self, "TypeError Exception", message)
            
            
    def on_remove_item(self) -> None:
        try:
            current_item_text = self.ui.listwidget_bulk_conversion.currentItem().text()
            current_item_row = self.ui.listwidget_bulk_conversion.currentRow()
            if current_item_row != -1:
                self.ui.listwidget_bulk_conversion.takeItem(current_item_row)
                self.ui.statusbar.showMessage(f"Removed {current_item_text} from list.", 6000)
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. Arguments: {ex.args!r}"
            QMessageBox.critical(self, f"Exception {type(ex).__name__}", message)
            
            
    def on_remove_all(self) -> None:
        try:
            reply = QMessageBox.question("Delete all items", "Do you really want to clear the list?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            
            if reply == QMessageBox.Yes:
                if self.ui.listwidget_bulk_conversion.count() > 0:
                    self.ui.listwidget_bulk_conversion.clear()
                    self.ui.statusbar.showMessage("Deleted all items from list.", 6000)
                else:
                    self.ui.statusbar.showMessage("No items to delete.", 6000)
            else:
                return 
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. Arguments: {ex.args!r}"
            QMessageBox.critical(self, f"Exception {type(ex).__name__}", message)
            
            
    def on_conversion_start_signals(self, worker):
        worker.signals.progress_text.connect(self.on_progress_text)
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
                    self.ui.listwidget_bulk_conversion.addItem(file_path)
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
            self.settings.setValue("geometry", self.saveGeometry())
            super().closeEvent(event)


if __name__ == "__main__":
    # Initialize the application
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())