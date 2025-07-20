from pathlib import Path

input_file = r"D:\Downloads\Images\Test\Test.jpg"
output_file = r"Test.jpg"

path_input_file = Path(input_file)
path_output_file = Path(output_file)

# Check if output_file is just a filename (no path)
is_filename_only = path_output_file.name == output_file

def check_if_output_file_is_file(output_file: Path) -> bool:
    """Checks if the output_file is a file name and not a path
    Returns:
        bool: Returns True if output file is a file without a path, else False
    """
    # Check if output_file is just a filename (no path)
    is_file = output_file.name == output_file
    return is_file

def convert_file(output_extension_type: str, input_file: Path, output_file: Path = None):
    """
    Converts the input_file to a specified output format.
    
    If only a filename is given (e.g., 'final.ico'), the input file's folder is used.
    
    Args:
        output_extension_type (str, optional): Target file extension (e.g., "png"). Defaults to None.
        output_file (Path, optional): Path or filename to save the converted file.
    """
    other_file = r"D:\Downloads\Images\Test\Test.jpg"
    # Determine target path
    if output_file is None:
        final_output = other_file
    else:
        final_output = output_file
        # If only a name like "final.ico" is provided, no folder:
        is_filename = check_if_output_file_is_file(final_output)
        if not is_filename: # If only filename like string has been inputted
            final_output = input_file.parent / output_file.name # Save file in same dir as input file
        elif is_filename:
            final_output = output_file # Else save in the full specified directory
    # Apply extension override
    if output_extension_type != "Choose file extension..." and None:
        final_output = final_output.with_suffix(f".{output_extension_type}")
    print(f"Saving converted file to: {final_output}")
    

convert_file(None, path_input_file, path_output_file)