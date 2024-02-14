"""
Module for handling XML files.
"""

import xml.dom.minidom as minidom
import xml.etree.ElementTree as et
import json
import csv


def convert(data):
    """
    Convert data to XML format.

    Args:
        data (dict or str): The data to be converted. It can be a dictionary representing JSON data, a JSON string,
                            or a file path to a CSV file.

    Returns:
        str: The data in XML format.
    """
    if isinstance(data, str):
        # If the input data is a string, it may be JSON data or a file path to a CSV file
        # Check if it is a JSON string or a file path to a CSV file
        if data.endswith('.json'):
            return convert_json(data)
        elif data.endswith('.csv'):
            return convert_csv(data)
        else:
            try:
                # Try to load the string as JSON data
                json_data = json.loads(data)
                return convert_json(json_data)
            except json.JSONDecodeError:
                # If it's not valid JSON data, assume it's XML data and return it as is
                return data
    elif isinstance(data, dict):
        # If the input data is a dictionary, convert it to XML
        return convert_json(data)
    else:
        raise ValueError("Unsupported data format for conversion")


def convert_json(data):
    """
    Convert JSON data to XML format.

    Args:
        data (dict or str): The JSON data to be converted.

    Returns:
        str: The data in XML format.
    """
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data")
    elif not isinstance(data, dict):
        raise ValueError("JSON data must be a dictionary")

    return _json_to_xml(data)


def _json_to_xml(data):
    """
    Convert JSON data to XML format.

    Args:
        data (dict): The JSON data to be converted.

    Returns:
        str: The data in XML format.
    """
    root = et.Element("root")  # Create root element

    # Iterate over each key-value pair in the input data and create XML elements for them
    for key, value in data.items():
        if isinstance(value, list):
            # If the value is a list, create an element for each item in the list
            for item in value:
                element = et.SubElement(root, key)  # Create an element with the key name
                if isinstance(item, dict):
                    # If the item is a dictionary, create subelements for its key-value pairs
                    for subkey, subvalue in item.items():
                        subelement = et.SubElement(element, subkey)  # Create a subelement with the subkey name
                        subelement.text = str(subvalue)  # Set the text content of the subelement
        else:
            # If the value is not a list, create a single element for it
            element = et.SubElement(root, key)  # Create an element with the key name
            element.text = str(value)  # Set the text content of the element

    xml_str = et.tostring(root, encoding="unicode")  # Convert ElementTree to XML string
    xml_str = minidom.parseString(xml_str).toprettyxml(indent="  \t")  # Parse content xml
    return xml_str


def convert_csv(csv_data):
    """
    Convert CSV data to XML format.

    Args:
        csv_data (str): The CSV data to be converted.

    Returns:
        str: The data in XML format.
    """
    lines = csv_data.strip().split('\n')  # Split CSV data into lines
    headers = lines[0].split(',')  # Extract headers from the first line
    xml = ['<?xml version="1.0" ?>', '<root>']  # Initialize XML list

    for line in lines[1:]:  # Iterate over each line (excluding headers)
        values = line.split(',')  # Split line into values
        xml.append('\t<countries>')  # Open countries tag for each record
        for header, value in zip(headers[1:], values[1:]):  # Skip the first header
            xml.append(f'\t\t<{header}>{value}</{header}>')  # Add XML tag for each field
        xml.append('\t</countries>')  # Close countries tag for each record

    xml.append('</root>')  # Close root tag
    return '\n'.join(xml)  # Join XML list into a single string



def opformat(file_path):
    """
    Format an XML file to make it more readable.

    Args:
        file_path (str): The path to the XML file to be formatted.
    """
    try:
        with open(file_path, 'r') as file:
            xml_str = file.read()  # Read file
            xml = minidom.parseString(xml_str)  # Parse content xml
            with open(file_path, 'w') as file:  # Open file as writing
                file.write(xml.toprettyxml(indent="  \t"))  # format file
    except FileNotFoundError:
        print(f"Failed to format XML file: {file_path}")
