# PY-MAGICK 🪄✨

**pymagick** is a Python module designed to facilitate file manipulation and usage in various formats. The module provides functionalities for reading, writing, and manipulating files of different types, including CSV, JSON, XML, and more. This project aims to offer an intuitive and efficient interface for working with data stored in files, providing powerful tools for common data manipulation operations.

## Key Features ⚔️

- **File Reading and Writing:** The module provides functions to read and write data in files of various formats, including CSV, JSON, XML, etc.
- **Data Manipulation:** It allows performing data manipulation operations on files programmatically, such as adding, removing, or modifying data.
- **File Formating**: Brings an easy way to format a file at the moment you write it, even after.
- **Intuitive Interface:** Offers an intuitive and easy-to-use interface for Python developers, enabling efficient file operations.
- **Support for Various File Formats:** In addition to CSV, the module supports file manipulation in a variety of formats, making it highly versatile and useful for a range of applications.

## Installation 🛠️

You can install the module using pip:

```cmd
> pip install pymagick
````

## Example Usage 💻
*Full info example tester file here*
[TESTER.py](https://gist.github.com/SergioLKG/e1bd7c26a29653cb5bec0824151be8f2)

```python
import os
import pymagick

def test_handling(file_format, data):
    output_folder = 'test-rubish'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, f"test{file_format}")

    print(f"Testing {file_format.upper()} file handling...")

    file_data = pymagick.convert(data, file_format)
    print(f"{file_format.upper()} data:")
    print(file_data)

    pymagick.write(file_data, output_file)
    print(f"{file_format.upper()} file '{output_file}' created.")

    print(f"Formatting {file_format.upper()} file...")
    pymagick.opformat(output_file)
    print(f"{file_format.upper()} file formatted.\n")

if __name__ == "__main__":
    data = {
        "employees": [
            {"name": "John", "age": 30, "city": "New York"},
            {"name": "Alice", "age": 25, "city": "Los Angeles"},
            {"name": "Bob", "age": 35, "city": "Chicago"}
        ]
    }

    test_handling('.csv', [['Name', 'Age', 'City'], ['John', 30, 'New York'], ['Alice', 25, 'Los Angeles'], ['Bob', 35, 'Chicago']])
    test_handling('.json', data)
    test_handling('.xml', data)
...
```

## Quick Solve Methods 🏃‍♂️💨

- **Quick Solve:**
    ```python
    import pymagick
    """
    Quickest way to perform file operations using pymagick module!
    """

    # Example: Read CSV file
    data = pymagick.read('data.csv')

    # Example: Write data to a CSV file
    pymagick.write('output.csv', data)

    # Example: Append data to a CSV file
    pymagick.append('output.csv', new_data)

    # Example: Convert data to JSON format
    json_data = pymagick.convert(data, '.json')

    # Example: Format JSON file
    pymagick.format('output.json')
    ```

## Contribution 🤝

*Contributions are welcome! If you'd like to contribute to this project, please follow these steps:*

1. Fork the repository
2. Create a branch for your new feature (`git checkout -b feature/new-feature`)
3. Make your changes and commit (`git commit -am 'Add new feature'`)
4. Push the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is licensed under the [MIT License](LICENSE).
