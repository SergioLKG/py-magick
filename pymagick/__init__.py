"""
Welcome to PYMAGICK

A Python module for file manipulation and usage.
The python module where dreams come true!
"""
import os
import subprocess

from . import csv
from . import json


def convert(data, to_format):
    """
    Convert data to the specified file format.

    Args:
        data (dict or list): The data to be converted.
        to_format (str): The target file format (e.g., '.csv', '.json').

    Returns:
        str: The converted data.
    """
    if to_format == '.csv':
        return csv.convert(data)
    elif to_format == '.json':
        return json.convert(data)
    else:
        raise ValueError(f"Unsupported format: {to_format}")


def opformat(file_path):
    """
    Format a file if possible.

    Args:
        file_path (str): The path to the file to be formatted.
    """
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == '.json':
        json.opformat(file_path)
    else:
        print(f"Format not supported for file: {file_path}")
