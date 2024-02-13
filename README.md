# PY-MAGICK 🪄✨

**py-magik** is a Python module designed to facilitate file manipulation and usage in various formats. The module
provides functionalities for reading, writing, and manipulating files of different types, including CSV, JSON, XML, and
more. This project aims to offer an intuitive and efficient interface for working with data stored in files, providing
powerful tools for common data manipulation operations.

## Key Features ⚔️

- **File Reading and Writing:** The module provides functions to read and write data in files of various formats,
  including CSV, JSON, XML, etc.
- **Data Manipulation:** It allows performing data manipulation operations on files programmatically, such as adding,
  removing, or modifying data.
- **Intuitive Interface:** Offers an intuitive and easy-to-use interface for Python developers, enabling efficient file
  operations.
- **Support for Various File Formats:** In addition to CSV, the module supports file manipulation in a variety of
  formats, making it highly versatile and useful for a range of applications.

## Installation 🛠️

You can install the module using pip:

```cmd
> pip install py-magik
````

## Example Usage 💻

```python
    import py_magik

# Read data from a CSV file / export the data while read 
data = py_magik.csv.read('data.csv') / ('data.csv', 'output.txt')

# Convert the date (if possible)
py_magik.convert(data, '.sql')

# Write data to a CSV file / 
py_magik.csv.write('output.csv', data)

# Append in file
py_magik.csv.append('output.csv', data, modifiers...)

object = {
    "data": [
        {
            "something": "Wizard",
            "anotherthing": "Elder",
            "idontknow": "The Best",
            "enjoy": {
                "whynot": "elemental",
                "ofcourse": "Panther"
            },
            "anything": "hello"
        }
    ]
}

# Oh! I forget to add something, NO PROBLEM!!
object.appendto("enjoy", '"iforget": "Magick!"')

...
```

## Quick Solve Methods 🏃‍♂️💨

- **CSV Quick Solve:**
    ```python
    import py_magik
    """
    Quickest way to perform files without any format, just quick solves!
    """
    data = py_magik.csv.read('data.csv')
    py_magik.csv.write('output.csv', data)
    ```

- **JSON Quick Solve:**
    ```python
    import py_magik
    """
    Quickest way to perform files without any format, just quick solves!
    """
    data = rjson('data.json')
    wjson('output.csv', data)
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
