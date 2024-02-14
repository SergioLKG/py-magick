"""
Module for handling JSON files.
"""

import json
import csv
import xml.etree.ElementTree as et
import io


def convert(data):
    """
    Convert data to JSON format.

    Args:
        data: The data to be converted. It can be a string (CSV or XML data), or a list of dictionaries (CSV-like data).

    Returns:
        str: The data in JSON format.
    """
    if isinstance(data, str):
        # Try parsing the data as CSV
        try:
            return convert_csv(data)
        except Exception:
            # If parsing as CSV fails, try parsing as XML
            try:
                return convert_xml_to_json(data)
            except Exception as e:
                raise ValueError(f"Failed to convert data to JSON: {e}")
    elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
        # If data is a list of dictionaries (CSV-like data), convert it to JSON
        return json.dumps(data)
    else:
        raise ValueError("Unsupported data format for JSON conversion")


def convert_csv(csv_data):
    """
    Convert CSV data to JSON format.

    Args:
        csv_data (str): The CSV data to be converted.

    Returns:
        str: The data in JSON format.
    """
    # Convert CSV data into a list of dictionaries
    csv_lines = csv_data.strip().split('\n')
    column_headers = csv_lines[0].split(',')
    json_data = []
    for line in csv_lines[1:]:
        fields = line.split(',')
        item = {header: value for header, value in zip(column_headers[0:], fields[0:])}
        json_data.append(item)

    # Construct the JSON object with "countries" as key
    json_object = {"items": json_data}

    return json.dumps(json_object, indent=4)


def convert_xml_to_json(xml_data):
    """
    Convert XML data to JSON format.

    Args:
        xml_data (str): The XML data to be converted.

    Returns:
        str: The data in JSON format.
    """
    root = et.fromstring(xml_data)
    data = []
    for child in root:
        item = {}
        for subchild in child:
            item[subchild.tag] = subchild.text
        data.append(item)
    return json.dumps({"employees": data}, indent=4)


def opformat(file_path):
    """
    Format a JSON file to make it more readable.

    Args:
        file_path (str): The path to the JSON file to be formatted.
    """
    try:
        with open(file_path, 'r') as file:
            parsed_json = json.load(file)
        with open(file_path, 'w') as file:
            json.dump(parsed_json, file, indent=4)  # Format JSON with indentation
    except (ValueError, FileNotFoundError):
        print(f"Failed to format JSON file: {file_path}")
