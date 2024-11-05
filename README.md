![Build Status](https://github.com/Schemon-Inc/schemon-python-logger/actions/workflows/publish_pypi.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/schemon-python-logger)
![Downloads](https://img.shields.io/pypi/dm/schemon-python-logger)
![License](https://img.shields.io/github/license/Schemon-Inc/schemon-python-logger)
![Python Version](https://img.shields.io/pypi/pyversions/schemon-python-logger)
![GitHub Stars](https://img.shields.io/github/stars/Schemon-Inc/schemon-python-logger?style=social)

# schemon-python-logger

## Overview

`schemon-python-logger` is a simple and flexible logging library for Python applications. It provides a straightforward API to log messages with different severity levels and supports various output formats and handlers.

## Installation

You can install the package using pip:

```sh
pip install schemon-python-logger
```

## Usage

Here is a basic example of how to use `schemon-python-logger`:

```python
from schemon_python_logger.logger import Logger

# Create a logger instance
logger = Logger(name="example_logger")

# Log messages with different severity levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```
### Decorator
#### log_method

```python
from schemon_python_logger.logger import Logger
from schemon_python_logger.decorator import log_method

class test_class:
    number: int = 0
    logger: Logger = Logger('test logger')
    
    @log_method
    def test_method(self):
        print('logger')

test_class = test_class()
test_class.test_method()
```

```python
from schemon_python_logger.logger import Logger
from schemon_python_logger.decorator import log_function

logger: Logger = Logger('test logger', level='INFO')

@log_function
def test_function(logger=logger):
    print('logger')
    pass

test_function(logger)
```

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Contact

For any questions or suggestions, please submit an issue or join our Slack   
[![Slack](https://img.shields.io/badge/Slack-4A154B?logo=slack&logoColor=fff)](https://join.slack.com/t/schemon/shared_invite/zt-2jlk2l0fb-9A~lbn3COQlYbt2R0WnxAw)