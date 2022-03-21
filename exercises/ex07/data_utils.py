"""Dictionary related utility functions."""

__author__ = "730526509"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
   
    # Open a handle to the data file 
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Reac each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()

    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all vaules in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a colum-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    """Returns selected row in csv."""
    result: dict[str, list[str]] = {}
    for column in x:
        result[column] = x[column][0:y]
    return result


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Returns selected columns in csv."""
    result: dict[str, list[str]] = {}
    for column in x: 
        if column in y:
            result[column] = x[column]
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns two csv put together."""
    result: dict[str, list[str]] = {}
    for column in x:
        result[column] = x[column]
    for column in y:
        if column in result:
            result[column] += y[column]
        else:
            result[column] = y[column]
    return result