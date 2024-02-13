"""
Tester script for pymagick module.
"""

import os
import pymagick


def test_csv_handling():
    print("Testing CSV file handling...")
    # Sample data
    data = [
        ['Name', 'Age', 'City'],
        ['John', 30, 'New York'],
        ['Alice', 25, 'Los Angeles'],
        ['Bob', 35, 'Chicago']
    ]

    # Convert data to CSV format
    csv_data = pymagick.convert(data, '.csv')
    print("CSV data:")
    print(csv_data)

    # Write CSV data to file
    output_folder = 'test-rubish'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, 'test.csv')
    with open(output_file, 'w') as file:
        file.write(csv_data)
    print(f"CSV file '{output_file}' created.")

    # Format CSV file
    pymagick.opformat(output_file)


def test_json_handling():
    print("\nTesting JSON file handling...")
    # Sample data
    data = {
        "employees": [
            {"name": "John", "age": 30, "city": "New York"},
            {"name": "Alice", "age": 25, "city": "Los Angeles"},
            {"name": "Bob", "age": 35, "city": "Chicago"}
        ]
    }

    # Convert data to JSON format
    json_data = pymagick.convert(data, '.json')
    print("JSON data:")
    print(json_data)

    # Write JSON data to file
    output_folder = 'test-rubish'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, 'test.json')
    with open(output_file, 'w') as file:
        file.write(json_data)
    print(f"JSON file '{output_file}' created.")

    # Format JSON file
    pymagick.opformat(output_file)


if __name__ == "__main__":
    test_csv_handling()
    test_json_handling()
