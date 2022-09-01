import logging
import logging.config
import os
import sys

from utils.singleton import TestContext


def log_cleanup(logger_obj):
    # type: (logging.Logger) -> None
    for handler in logger_obj.handlers:
        handler.close()
        logger_obj.removeHandler(handler)


def create_logger(file_base_name, console_debug=logging.DEBUG):
    """Create logger object for the test to use."""
    log_file_name = os.path.join(os.path.dirname(__file__), "wmanager.log")
    if not os.path.exists(log_file_name):
        os.makedirs(log_file_name)

    test_log = logging.getLogger(file_base_name)
    test_log.setLevel(logging.DEBUG)

    # Define message format
    piv_log_fmt = logging.Formatter(
        fmt=u'%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
        datefmt=u'%m/%d/%Y %I:%M:%S %p')

    # Create streams
    stdout_stream = logging.StreamHandler(sys.stdout)
    stdout_stream.setLevel(logging.DEBUG if console_debug else logging.INFO)
    stdout_stream.setFormatter(piv_log_fmt)
    file_stream = logging.FileHandler(log_file_name, mode='w', encoding='utf-8')
    file_stream.setLevel(logging.DEBUG)
    file_stream.setFormatter(piv_log_fmt)

    # Add handlers to logger
    test_log.addHandler(stdout_stream)
    test_log.addHandler(file_stream)

    # Push cleanup method onto the test context
    TestContext().callback(log_cleanup, test_log)
    test_log.info("Results are saved in %s", log_file_name)
    # Return log object
    return test_log
