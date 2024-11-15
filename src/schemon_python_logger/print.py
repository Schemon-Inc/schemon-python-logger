import datetime
import inspect
import threading
from pyspark.sql import DataFrame as SparkDataFrame
from tabulate import tabulate


def print_dict(d: dict, parent_key: str = ""):
    """
    Prints a dictionary in a nice table format, showing keys, values, and nesting.
    """
    if not d:
        print("Empty dict")
        return

    rows = []

    def flatten_dict(d, parent_key):
        for key, value in d.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict):
                flatten_dict(value, full_key)
            else:
                rows.append({"Key": full_key, "Value": value})

    flatten_dict(d, parent_key)
    print(tabulate(rows, headers="keys", tablefmt="grid"))


def print_df(
    df: SparkDataFrame,
    n: int = 20,
    vertical: bool = False,
    truncate: bool = True,
    stage: str = None,
    entity_name: str = None,
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

    if stage and entity_name:
        print(
            f"{green}{formatted_start_time} | SHOWDATA | {padded_thread_name} | [{stage}] {entity_name} | {func_name}() | print data.{reset}"
        )
    else:
        print(
            f"{green}{formatted_start_time} | SHOWDATA | {padded_thread_name} | {func_name}() | print data.{reset}"
        )

    df.show(n=n, vertical=vertical, truncate=truncate)


def print_sql(
    sql: str,
    stage: str = None,
    entity_name: str = None,
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

    if stage and entity_name:
        print(
            f"{green}{formatted_start_time} | SHOWSQL | {padded_thread_name} | [{stage}] {entity_name} | {func_name}() | print sql.{reset}"
        )
    else:
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
