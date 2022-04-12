"""Dictionary related utility functions."""

__author__ = "730526509"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
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


def count(x: list[str]) -> dict[str, int]:
    """Counts the list on how many times a value reoccurs."""
    result: dict[str, int] = {}
    for thing in x:
        if thing in result: 
            result[thing] += 1 
        else:
            result[thing] = 1 
    return result 


def common_value(x: list[str]):
    """Chooses the most repeated value."""
    result: dict[str, int] = {}
    for thing in x:
        if thing in result: 
            result[thing] += 1 
        else:
            result[thing] = 1 
    
    h_count = list(result.values())
    top = max(h_count)
    for v in x:
        if result[v] == top:
            return v