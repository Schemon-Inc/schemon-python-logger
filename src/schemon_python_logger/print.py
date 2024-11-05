import datetime
import inspect
import threading
from pyspark.sql import DataFrame as SparkDataFrame


def print_dict(d: dict, indent_level: int = 0):
    indent = "  " * indent_level  # Adjust indentation based on depth
    for key, value in d.items():
        if isinstance(value, dict):
            print(f"{indent}{key}:")  # Print the key with indentation
            print_dict(
                value, indent_level + 1
            )  # Recursive call for nested dict with increased indent
        else:
            print(f"{indent}{key}: {value}")  # Print key-value pair with indentation


def print_df(
    df: SparkDataFrame, n: int = 20, vertical: bool = False, truncate: bool = True
):
    green = "\033[92m"
    reset = "\033[0m"
    start_time = datetime.datetime.now()
    formatted_start_time = (
        start_time.strftime("%Y-%m-%d %H:%M:%S")
        + f".{start_time.microsecond // 1000:03d}"
    )
    func_name = inspect.stack()[1].function
    thread_name = threading.current_thread().name
    padded_thread_name = f"{thread_name:<25}"

    print(
        f"{green}{formatted_start_time} | SHOWDATA | {padded_thread_name} | {func_name}() | print data.{reset}"
    )

    df.show(n=n, vertical=vertical, truncate=truncate)


def print_sql(sql: str):
    green = "\033[92m"
    reset = "\033[0m"
    start_time = datetime.datetime.now()
    formatted_start_time = (
        start_time.strftime("%Y-%m-%d %H:%M:%S")
        + f".{start_time.microsecond // 1000:03d}"
    )
    func_name = inspect.stack()[1].function
    thread_name = threading.current_thread().name
    padded_thread_name = f"{thread_name:<25}"

    print(
        f"{green}{formatted_start_time} | SHOWSQL  | {padded_thread_name} | {func_name}() | print sql.{reset}"
    )

    print(f"{green}{sql}{reset}")


def print_full_stack():
    # Get the current call stack
    stack = inspect.stack()

    print("Full stack trace:")
    for frame_info in stack:
        # frame_info[0]: the frame object
        # frame_info[1]: the filename
        # frame_info[2]: the line number
        # frame_info[3]: the function name
        print(
            f"File: {frame_info.filename}, Line: {frame_info.lineno}, Function: {frame_info.function}"
        )
