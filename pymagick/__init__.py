"""
Welcome to PYMAGICK

A Python module for file manipulation and usage.
The python module where dreams come true!
"""
import os

from . import csv
from . import json
from . import xml


def read(file_path):
    """
    Reads data from a file.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content read from the file.

    Raises:
        FileNotFoundError: If the file specified by file_path does not exist.
        IOError: If an error occurs while reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except IOError as e:
        raise IOError(f"Error reading file '{file_path}': {e}")


def write(data, file_path):
    """
    Writes data to a file.

    Args:
        data (str): The data to be written to the file.
        file_path (str): The path to the file to be written.

    Raises:
        IOError: If an error occurs while writing the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except IOError as e:
        raise IOError(f"Error writing to file '{file_path}': {e}")


def convert(data, output_format):
    """
    Convert data to the specified output format.

    Args:
        data (str): The data to be converted.
        output_format (str): The desired output format (".json", ".csv", or ".xml").

    Returns:
        str: The data in the specified output format.

    Raise: ValueError: If data format is not supported for conversion.
    """
    if output_format == ".xml":
        return xml.convert(data)
    elif output_format == ".json":
        return json.convert(data)
    elif output_format == ".csv":
        return csv.convert(data)
    else:
        raise ValueError("Unsupported output format for conversion")


def opformat(file_path):
    """
    Format a file if possible.

    Args:
        file_path (str): The path to the file to be formatted.
    """
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == '.json':
        json.opformat(file_path)
    elif file_extension == '.csv':
        csv.opformat(file_path)
    elif file_extension == '.xml':
        xml.opformat(file_path)
    else:
        print(f"Format not supported for file: {file_path}")
