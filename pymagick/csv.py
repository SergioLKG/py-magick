"""
Module for handling CSV files.
"""
import csv
import io
import json
import xml.etree.ElementTree as et


def convert(data):
    """
    Convert data to CSV format.

    Args:
        data: The data to be converted. It can be a string (JSON or XML data),
              a list of dictionaries (JSON-like data), or an ElementTree Element (XML data).

    Returns:
        str: The data in CSV format.
    """
    if isinstance(data, str):
        # Try parsing the data as JSON
        try:
            json_data = json.loads(data)
            if isinstance(json_data, list):
                # Convert the list to a dictionary with a default key
                json_data = {"data": json_data}
            return convert_json(json_data)
        except json.JSONDecodeError:
            # If parsing as JSON fails, try parsing as XML
            try:
                root = et.fromstring(data)
                return convert_xml(root)
            except et.ParseError:
                # If parsing as XML fails as well, assume it's already CSV data
                return data
    elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
        # If data is a list of dictionaries (JSON-like data), convert it to CSV
        return convert_json({"data": data})
    elif isinstance(data, et.Element):
        # If data is an ElementTree Element (XML data), convert it to CSV
        return convert_xml(data)
    else:
        raise ValueError("Unsupported data format for CSV conversion")


def convert_json(data):
    """
    Convert JSON data to CSV format.

    Args:
        data (dict or str): The JSON data to be converted.

    Returns:
        str: The data in CSV format.
    """
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data")
    elif not isinstance(data, (list, dict)):
        raise ValueError("JSON data must be a list or dictionary")

    if isinstance(data, dict):
        # If the data is a dictionary with a single key, assume that key contains the list
        # and use its value as the data
        if len(data) == 1:
            key = next(iter(data))
            if isinstance(data[key], list):
                data = data[key]

    if not isinstance(data, list):
        raise ValueError("JSON data must be a list of dictionaries")

    # Extract column headers from the first dictionary
    column_headers = list(data[0].keys())

    output = io.StringIO()
    writer = csv.writer(output, lineterminator='\n')

    # Write header row with "countries" as an additional column
    writer.writerow(column_headers)

    # Write data rows
    for item in data:
        writer.writerow([item.get(header, "") for header in column_headers])

    return output.getvalue()


def convert_xml(data):
    """
    Convert XML data to CSV format.

    Args:
        data (xml.etree.ElementTree.Element): The XML data to be converted.

    Returns:
        str: The data in CSV format.
    """
    if not isinstance(data, et.Element):
        raise ValueError("XML data must be an ElementTree Element")

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([child.tag for child in data[0]])
    for elem in data:
        writer.writerow([elem.find(child.tag).text if elem.find(child.tag) is not None else "" for child in data[0]])
    return output.getvalue()


def opformat(file_path):
    """
    No formatting needed for CSV files.

    Args:
        file_path (str): The path to the CSV file to be formatted.
    """
    pass  # No formatting needed for CSV files
