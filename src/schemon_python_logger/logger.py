import logging
import time
import inspect
from schemon_python_logger.print import print_full_stack


class ColoredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[94m",  # Blue
        "INFO": "",  # Default terminal color
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Magenta
    }

    RESET = "\033[0m"

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        # Adjust log level and thread name to be fixed length
        levelname_padded = f"{record.levelname:<8}"
        threadname_padded = f"{record.threadName:<25}"
        message = super().format(record)
        # Replace the default format with the padded versions
        return f"{color}{message.replace(record.levelname, levelname_padded).replace(record.threadName, threadname_padded)}{self.RESET}"


class SchemonPythonLogger:
    def __init__(self, name: str, log_file: str = "schemon.log", level: str = "DEBUG"):
        log_level = logging._nameToLevel.get(level.upper(), logging.DEBUG)
        print(f"CONFIG | Log level: {level}({log_level}) for {name}")
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        if not self.logger.hasHandlers():
            console_handler = logging.StreamHandler()
            if level == "DEBUG":
                formatter = ColoredFormatter(
                    "%(asctime)s.%(msecs)03d | %(levelname)s | %(threadName)s | %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                )
            else:
                formatter = ColoredFormatter(
                    "%(asctime)s.%(msecs)03d | %(levelname)s | %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                )
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def format_message(
        self, message: str, stage: str = None, entity_name: str = None
    ) -> str:
        if stage and entity_name:
            return f"[{stage}] {entity_name} | {message}"
        elif stage:
            return f"[{stage}] {message}"
        elif entity_name:
            return f"{entity_name} | {message}"
        return message

    def debug(self, message: str, stage: str = None, entity_name: str = None):
        formatted_message = self.format_message(message, stage, entity_name)
        self.logger.debug(formatted_message)

    def info(self, message: str, stage: str = None, entity_name: str = None):
        formatted_message = self.format_message(message, stage, entity_name)
        self.logger.info(formatted_message)

    def warning(self, message: str, stage: str = None, entity_name: str = None):
        formatted_message = self.format_message(message, stage, entity_name)
        self.logger.warning(formatted_message)

    def error(self, message: str, stage: str = None, entity_name: str = None):
        formatted_message = self.format_message(message, stage, entity_name)
        self.logger.error(formatted_message)
        print_full_stack()

    def critical(self, message: str, stage: str = None, entity_name: str = None):
        formatted_message = self.format_message(message, stage, entity_name)
        self.logger.critical(formatted_message)
        print_full_stack()

    def get_logger(self):
        return self.logger

    def log_function_start(
        self, stage: str = None, entity_name: str = None, func_name: str = None
    ):
        start_time = time.time()
        if func_name is None:
            func_name = inspect.stack()[1].function
        self.info(
            f"{func_name}() - Operation started",
            stage,
            entity_name,
        )
        return start_time

    def log_function_end(
        self,
        start_time,
        stage: str = None,
        entity_name: str = None,
        row_count=None,
        func_name: str = None,
    ):
        end_time = time.time()
        duration = end_time - start_time
        if func_name is None:
            func_name = inspect.stack()[1].function
        if row_count is None:
            self.info(
                f"{func_name}() - Operation completed. Duration: {duration:.2f} seconds",
                stage,
                entity_name,
            )
        else:
            self.info(
                f"{func_name}() - Operation completed. Duration: {duration:.2f} seconds, Row count: {row_count}",
                stage,
                entity_name,
            )

    def log_merge_metrics(
        self,
        num_affected_rows,
        num_updated_rows,
        num_deleted_rows,
        num_inserted_rows,
        stage: str = None,
        entity_name: str = None,
    ):
        self.info(
            (
                "write() - Merge operation completed.\n"
                f"Inserted: {num_inserted_rows}\n"
                f"Updated: {num_updated_rows}\n"
                f"Deleted: {num_deleted_rows}\n"
                f"Total affected: {num_affected_rows}"
            ),
            stage,
            entity_name,
        )
