from functools import wraps

try:
    from schemon.domain.contract.contract import Contract  # type: ignore
except ImportError:
    Contract = None

try:
    from schemon.service.notebook.base.store_service import get_store  # type: ignore
except ImportError:
    get_store = None

from schemon_python_logger.logger import Logger


def log_method(func):
    """
    Decorator to log class method start and end times.

    The logger instance is assumed to be part of the class instance (self).
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Extract function name and initialize logger
        func_name = func.__name__
        if not hasattr(self, "logger") or not isinstance(self.logger, Logger):
            raise ValueError(
                "The class instance does not have a valid 'logger' of type Logger"
            )
        logger: Logger = self.logger
        contract = None
        stage = None
        entity_name = None
        row_count = None

        # Check if Contract is imported and extract contract if present
        if Contract:
            for arg in args:
                if isinstance(arg, Contract):
                    contract = arg

        # Check if get_store and Contract are available before proceeding
        if (
            get_store
            and contract
            and (func_name == "transform" or func_name == "write")
        ):
            store = get_store(self.stores, contract)
            stage = contract.stage
            entity_name = contract.entity.name

            if store is None:
                logger.error(
                    f"{func_name}() - Store not found for contract {entity_name}.",
                    stage,
                    entity_name,
                )
                raise ValueError(f"Store not found for contract {entity_name}")
            elif store.df is None:
                logger.error(
                    f"{func_name}() - DataFrame not found for contract {entity_name}.",
                    stage,
                    entity_name,
                )
                raise ValueError(f"DataFrame not found for contract {entity_name}")
            elif store.df.count() == 0:
                logger.warning(
                    f"{func_name}() - No data to {func_name}.",
                    stage,
                    entity_name,
                )
            else:
                row_count = store.df.count()

        # Log the function start
        start_time = logger.log_function_start(stage, entity_name, func_name)

        try:
            # Execute the wrapped function
            return_value = func(self, *args, **kwargs)
            return return_value
        finally:
            # Log the function end
            logger.log_function_end(
                start_time, stage, entity_name, row_count, func_name
            )

    return wrapper


def log_function(func):
    """
    Decorator to log standalone function start and end times.

    The logger instance is assumed to be provided as a keyword argument.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Extract function name and initialize logger
        func_name = func.__name__
        logger: Logger = None
        contract = None
        stage = None
        entity_name = None
        row_count = None
        for arg in args:
            if isinstance(arg, Logger):
                logger = arg
                break

        if not logger:
            raise ValueError("A valid 'Logger' instance must be passed as an argument")

        # Check if Contract is imported and extract contract if present
        if Contract:
            for arg in args:
                if isinstance(arg, Contract):
                    contract = arg

        # Check if get_store and Contract are available before proceeding
        if get_store and contract:
            store = get_store(kwargs.get("stores"), contract)
            stage = contract.stage
            entity_name = contract.entity.name

            if store is None:
                logger.error(
                    f"{func_name}() - Store not found for contract {entity_name}.",
                    stage,
                    entity_name,
                )
                raise ValueError(f"Store not found for contract {entity_name}")
            elif store.df is None:
                logger.error(
                    f"{func_name}() - DataFrame not found for contract {entity_name}.",
                    stage,
                    entity_name,
                )
                raise ValueError(f"DataFrame not found for contract {entity_name}")
            elif store.df.count() == 0:
                logger.warning(
                    f"{func_name}() - No data to {func_name}.",
                    stage,
                    entity_name,
                )
            else:
                row_count = store.df.count()

        # Log the function start
        start_time = logger.log_function_start(stage, entity_name, func_name)

        try:
            # Execute the wrapped function
            return_value = func(*args, **kwargs)
            return return_value
        finally:
            # Log the function end
            logger.log_function_end(
                start_time, stage, entity_name, row_count, func_name
            )

    return wrapper
