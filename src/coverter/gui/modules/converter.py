from PIL import Image
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Tuple, ClassVar, Optional
from PySide6.QtCore import Signal, QObject

# Constants for username and temp path

TEMP: Path = Path(r"C:\tmp")

class ConversionSettings(BaseModel):
    output_directory: Path = Path() # default to current dir
    output_extension_type: str = ""
    input_files_bulk: List[Path] = Field(default_factory=list)
    resize_width: int = 0
    resize_height: int = 0


class ConverterSignals(QObject):
    statusbar_progress_text = Signal(str)
    messagebox_error = Signal(str, str)
    messagebox_warning = Signal(str, str)
    messagebox_info = Signal(str, str)

class Converter(BaseModel):
    def __init__(self):
        Converter.signals = ConverterSignals()
        Converter.settings = ConversionSettings()
    
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
            if not self.settings.input_files_bulk:
                raise ValueError("No input files provided for conversion.")
            
            # Check if all input files exist
            for input_file in self.settings.input_files_bulk:
                if not input_file.exists():
                    raise ValueError(f"Input file {input_file} does not exist.")
                if not input_file.is_file():
                    raise ValueError(f"Input path {input_file} is not a file.")
            
            # Check if output directory exists (output_file is always a directory for bulk conversion)
            if not self.settings.output_directory.exists():
                raise ValueError(f"Output directory {self.settings.output_directory} does not exist.")
            if not self.settings.output_directory.is_dir():
                raise ValueError(f"Output path {self.settings.output_directory} is not a directory.")
            
            return True
        except ValueError as ve:
            message = f"An exception of type {type(ve).__name__} has occurred.\nError Message: {str(ve)}"
            Converter.signals.statusbar_progress_text.emit("Check Error:", message)
            return False
        
    @staticmethod
    def get_selected_image_size(file_path: Path) -> Optional[Tuple[int, int]]:
        """
        Gets the dimensions (width, height) of a given image file.
        
        Args:
            file_path: Path to the image file
            
        Returns:
            Tuple of (width, height) or None if error occurs
        """
        try:
            with Image.open(file_path) as im:
                width, height = im.size 
                return width, height
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} has occurred.\nError Message: {str(ex)}"
            Converter.signals.messagebox_error.emit("Get input image size error", message)
            return None
        
    @staticmethod
    def get_image_file_data(file_path: Path) -> tuple[str, str, int, int]:
        """_summary_

        Args:
            file_path (str): File path to the image.

        Returns:
            tuple[str, str, int, int]: Filename (str), Extension (str), Width (int), Height (int)
        """
        try:
            # Convert the string path to a Path object
            full_path = Path(file_path)
            file_name = full_path.name
            extension = full_path.suffix
                    
            with Image.open(file_path) as image:
                width, height = image.width, image.height
            
            return file_name, extension, width, height
                
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. Arguments: {ex.args!r}"
            Converter.signals.messagebox_error.emit(f"Exception {type(ex).__name__}", message)
    
    @staticmethod
    def resize_image_for_preview(input_file: Path, width: int, height: int) -> Path:
        """Returns the image in a resized form for the preview and saves it in the temp folder C:\temp

        Args:
            input_file (Path): Path object of image file

        Returns:
            Path: Path object of image file in temp
        """
        try:
            # Check if it temp folder exists
            if not TEMP.exists():
                TEMP.mkdir(parents=True, exist_ok=True)
                
            with Image.open(input_file) as im:
                im = im.resize((width, height))
                output_path = Path(TEMP) / input_file.name
            # Save to temp folder
                im.save(output_path)

            return output_path
            
        except Exception as ex:
            message = f"Error resizing image {input_file.name}: {type(ex).__name__} - {str(ex)}"
            Converter.signals.messagebox_error.emit("Error resizing image", message)
            
    @staticmethod
    def cleanup_temp_folder() -> None:
        """Clean up the temp folder
        """
        try:
            files = [f for f in TEMP.iterdir() if f.is_file()]
            for file in files:
                Path.unlink(file)
        except FileNotFoundError as ex:
            Converter.signals.messagebox_error.emit("FileNotFoundError", str(ex))

    def perform_conversion(self, input_file: Path, output_path: Path) -> bool:
        """
        Performs the actual image conversion for a single file, including resizing if specified.
        
        Returns:
            bool: True if conversion successful, False otherwise
        """
        try:
            with Image.open(input_file) as im:
                # Perform resizing if dimensions are provided
                if self.settings.resize_width > 0 and self.settings.resize_height > 0:
                    im = im.resize((self.settings.resize_width, self.settings.resize_height))
                
                # Ensure output directory exists
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                im.save(output_path)
                Converter.signals.statusbar_progress_text.emit(f"Converted: {input_file.name} -> {output_path.name}")
                return True
        except Exception as ex:
            message = f"Error converting {input_file.name}: {type(ex).__name__} - {str(ex)}"
            Converter.signals.messagebox_error.emit("Conversion Error", message)
            return False


    def perform_bulk_conversion(self) -> None:
        """
        Performs bulk image conversion, iterating through input_files_bulk
        and saving each to the specified output directory with a new extension.
        """
        if not self.settings.input_files_bulk:
            Converter.signals.messagebox_error.emit("Bulk Conversion", "No files selected for bulk conversion.")
            return

        successful_conversions = 0
        total_files = len(self.settings.input_files_bulk)

        for input_path in self.settings.input_files_bulk:
            try:
                # Create output path for each file in bulk, preserving original filename stem
                # and applying the new extension, saving to the specified output directory.
                
                # Clean the extension (remove dot if present)
                clean_extension = self.settings.output_extension_type.lstrip('.')
                output_filename = input_path.stem + f".{clean_extension}"
                if self.settings.resize_width > 0 and self.settings.resize_height > 0:
                    output_full_path = self.settings.output_directory / f"{self.settings.resize_width}x{self.settings.resize_height}_{output_filename}"
                else:
                    output_full_path = self.settings.output_directory / output_filename # self.settings.output_file is the directory for bulk
                
                if self.perform_conversion(input_path, output_full_path):
                    successful_conversions += 1
                    
            except Exception as ex:
                message = f"Skipping conversion for {input_path.name} due to error: {type(ex).__name__} - {str(ex)}"
                Converter.signals.messagebox_error.emit("Bulk Conversion Error", message)

        # Summary message
        if successful_conversions == total_files:
            Converter.signals.messagebox_info.emit("Bulk Conversion Complete", 
                                            f"Successfully converted {successful_conversions}/{total_files} files.")
        elif successful_conversions > 0:
            Converter.signals.messagebox_warning.emit("Bulk Conversion Partial", 
                                            f"Converted {successful_conversions}/{total_files} files. Some conversions failed.")
        else:
            Converter.signals.messagebox_error.emit("Bulk Conversion Failed", 
                                            "No files were successfully converted.")


    def start_conversion_process(self):
        """
        Starts the conversion process for bulk files.
        """
        try:
            if not self.perform_checks():
                return

            # Validate output extension
            if not self.settings.output_extension_type or self.settings.output_extension_type == "Choose file extension...":
                Converter.signals.messagebox_error.emit("Conversion Error", "Please select a valid output file extension.")
                return

            Converter.signals.statusbar_progress_text.emit("Starting bulk conversion...")
            self.perform_bulk_conversion()
            Converter.signals.statusbar_progress_text.emit("Bulk conversion process completed.")

        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} has occurred.\nError Message: {str(ex)}"
            Converter.signals.messagebox_error.emit("Convert File Error", message)
