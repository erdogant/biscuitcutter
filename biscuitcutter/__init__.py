import logging

# We import 'main' instead of 'biscuitcutter' since that is the actual entry point in your script.
from biscuitcutter.biscuitcutter import main

__author__ = 'Erdogan Taskesen'
__email__ = 'erdogant@gmail.com'
__version__ = '1.1.0'

# Setup package-level logger
_logger = logging.getLogger('biscuitcutter')
_log_handler = logging.StreamHandler()
_formatter = logging.Formatter(fmt='[{asctime}] [{name:<12.12}] [{levelname:<8}] {message}', style='{', datefmt='%d-%m-%Y %H:%M:%S')
_log_handler.setFormatter(_formatter)
_log_handler.setLevel(logging.DEBUG)
if not _logger.hasHandlers():  # avoid duplicate handlers if re-imported
    _logger.addHandler(_log_handler)
_logger.setLevel(logging.DEBUG)
_logger.propagate = True  # allow submodules to inherit this handler


# module level doc-string
__doc__ = """
biscuitcutter
=====================================================================

biscuitcutter is a new repo scaffolder using command line interface.

Example
-------
>>> # Install
>>> pip install biscuitcutter
>>> # From the terminal run:
>>> biscuitcutter
>>>


References
----------
https://github.com/erdogant/biscuitcutter

"""