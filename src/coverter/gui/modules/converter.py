from PIL import Image
from pathlib import Path
from pydantic import BaseModel
from typing import List, Tuple, ClassVar, Optional


from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QFileDialog, QMessageBox, QInputDialog, QLineEdit)
from PySide6.QtGui import QIcon, QAction, QCloseEvent, QShortcut, QKeySequence
from PySide6.QtCore import Qt, Signal, Slot, QFile, QTextStream, QIODevice, QSettings, QThreadPool, QObject

class ConverterSignals(QObject):
    progress_text = Signal(str)
    messagebox_error = Signal(str, str)
    messagebox_warning = Signal(str, str)
    messagebox_info = Signal(str, str)

class Converter(BaseModel):
    
    output_directory: Path # Output directory for bulk conversion
    output_extension_type: str = "" # Target extension, e.g., "png", "ico"
    input_files_bulk: List[Path] = [] # List of files for bulk conversion
    resize_width: int = 0 # Target width for resizing, 0 means no resize
    resize_height: int = 0 # Target height for resizing, 0 means no resize
    
    # Declare signals as a ClassVar so Pydantic ignores it as a model field
    signals: ClassVar[ConverterSignals] = ConverterSignals()

    class Config:
        arbitrary_types_allowed = True  # Allow Path objects in Pydantic

    def perform_checks(self) -> bool:
        """Checks if input files exist and if output directory exists

        Returns:
            bool: True if all checks pass, False otherwise
        """
        try:
            # Check if we have input files for bulk conversion
            if not self.input_files_bulk:
                raise ValueError("No input files provided for conversion.")
            
            # Check if all input files exist
            for input_file in self.input_files_bulk:
                if not input_file.exists():
                    raise ValueError(f"Input file {input_file} does not exist.")
                if not input_file.is_file():
                    raise ValueError(f"Input path {input_file} is not a file.")
            
            # Check if output directory exists (output_file is always a directory for bulk conversion)
            if not self.output_directory.exists():
                raise ValueError(f"Output directory {self.output_directory} does not exist.")
            if not self.output_directory.is_dir():
                raise ValueError(f"Output path {self.output_directory} is not a directory.")
            
            return True
        except ValueError as ve:
            message = f"An exception of type {type(ve).__name__} has occurred.\nError Message: {str(ve)}"
            self.signals.messagebox_error.emit("Check Error", message)
            return False
        
        
    def get_selected_image_size(self, input_file: Path) -> Optional[Tuple[int, int]]:
        """
        Gets the dimensions (width, height) of a given image file.
        
        Args:
            input_file: Path to the image file
            
        Returns:
            Tuple of (width, height) or None if error occurs
        """
        try:
            with Image.open(input_file) as im:
                width, height = im.size 
                return width, height
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} has occurred.\nError Message: {str(ex)}"
            self.signals.messagebox_error.emit("Get input image size error", message)
            return None


    def perform_conversion(self, input_path: Path, output_path: Path) -> bool:
        """
        Performs the actual image conversion for a single file, including resizing if specified.
        
        Returns:
            bool: True if conversion successful, False otherwise
        """
        try:
            with Image.open(input_path) as im:
                # Perform resizing if dimensions are provided
                if self.resize_width > 0 and self.resize_height > 0:
                    im = im.resize((self.resize_width, self.resize_height))
                
                # Ensure output directory exists
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                im.save(output_path)
                self.signals.progress_text.emit(f"Converted: {input_path.name} -> {output_path.name}")
                return True
        except Exception as ex:
            message = f"Error converting {input_path.name}: {type(ex).__name__} - {str(ex)}"
            print(message)
            self.signals.messagebox_error.emit("Conversion Error", message)
            return False


    def perform_bulk_conversion(self) -> None:
        """
        Performs bulk image conversion, iterating through input_files_bulk
        and saving each to the specified output directory with a new extension.
        """
        if not self.input_files_bulk:
            self.signals.messagebox_error.emit("Bulk Conversion", "No files selected for bulk conversion.")
            return

        successful_conversions = 0
        total_files = len(self.input_files_bulk)

        for input_path in self.input_files_bulk:
            try:
                # Create output path for each file in bulk, preserving original filename stem
                # and applying the new extension, saving to the specified output directory.
                
                # Clean the extension (remove dot if present)
                clean_extension = self.output_extension_type.lstrip('.')
                output_filename = input_path.stem + f".{clean_extension}"
                if self.resize_width > 0 and self.resize_height > 0:
                    output_full_path = self.output_directory / f"{self.resize_width}x{self.resize_height}_{output_filename}"
                else:
                    output_full_path = self.output_directory / output_filename # self.output_file is the directory for bulk
                
                if self.perform_conversion(input_path, output_full_path):
                    successful_conversions += 1
                    
            except Exception as ex:
                message = f"Skipping conversion for {input_path.name} due to error: {type(ex).__name__} - {str(ex)}"
                print(message)
                self.signals.messagebox_error.emit("Bulk Conversion Error", message)

        # Summary message
        if successful_conversions == total_files:
            self.signals.messagebox_info.emit("Bulk Conversion Complete", 
                                            f"Successfully converted {successful_conversions}/{total_files} files.")
        elif successful_conversions > 0:
            self.signals.messagebox_warning.emit("Bulk Conversion Partial", 
                                            f"Converted {successful_conversions}/{total_files} files. Some conversions failed.")
        else:
            self.signals.messagebox_error.emit("Bulk Conversion Failed", 
                                            "No files were successfully converted.")


    def start_conversion_process(self):
        """
        Starts the conversion process for bulk files.
        """
        try:
            if not self.perform_checks():
                return

            # Validate output extension
            if not self.output_extension_type or self.output_extension_type == "Choose file extension...":
                self.signals.messagebox_error.emit("Conversion Error", "Please select a valid output file extension.")
                return

            self.signals.progress_text.emit("Starting bulk conversion...")
            self.perform_bulk_conversion()
            self.signals.progress_text.emit("Bulk conversion process completed.")

        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} has occurred.\nError Message: {str(ex)}"
            self.signals.messagebox_error.emit("Convert File Error", message)
