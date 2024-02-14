"""
Tester script for pymagick module.
"""

import os
import pymagick

# def test_handling(file_format, data):
#     # Create the output folder if it doesn't exist
#     output_folder = 'test-rubish'
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     # Define the output file path
#     output_file = os.path.join(output_folder, f"test{file_format}")
#     """
#     Test file handling for the given format.
#
#     Args:
#         file_format (str): The format of the file to test (e.g., '.csv', '.json', '.xml').
#         data: The sample data to use for testing.
#     """
#     # Print a message indicating the start of the test
#     print(f"Testing {file_format.upper()} file handling...")
#
#     # Convert data to the specified format
#     file_data = pymagick.convert(data, file_format)
#
#     # Display the converted data
#     print(f"{file_format.upper()} data:")
#     print(file_data)
#
#     # Write the converted data to a file
#     pymagick.write(file_data, output_file)
#
#     # Print a message indicating the creation of the output file
#     print(f"{file_format.upper()} file '{output_file}' created.")
#
#     # Format the file
#     print(f"Formatting {file_format.upper()} file...")
#     pymagick.opformat(output_file)
#
#     # Print a message indicating the completion of the test
#     print(f"{file_format.upper()} file formatted.\n")
#
#
# if __name__ == "__main__":
#     # Sample data
#     data = {
#         "employees": [
#             {"name": "John", "age": 30, "city": "New York"},
#             {"name": "Alice", "age": 25, "city": "Los Angeles"},
#             {"name": "Bob", "age": 35, "city": "Chicago"}
#         ]
#     }
#
#     # Test CSV handling
#     test_handling('.csv', [
#         ['Name', 'Age', 'City'],
#         ['John', 30, 'New York'],
#         ['Alice', 25, 'Los Angeles'],
#         ['Bob', 35, 'Chicago']
#     ])
#
#     # Test JSON handling
#     test_handling('.json', data)
#
#     # Test XML handling
#     test_handling('.xml', data)
csv_data = pymagick.read("test-rubish/test.json")
xml_data = pymagick.convert(csv_data, ".csv")
pymagick.write(xml_data, "test-rubish/test.csv")
