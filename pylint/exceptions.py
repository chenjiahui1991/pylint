# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

"""Exception classes raised by various operations within pylint."""


class InvalidMessageError(Exception):
    """raised when a message creation, registration or addition is rejected"""

class UnknownMessage(Exception):
    """raised when a unregistered message id is encountered"""

class EmptyReport(Exception):
    """raised when a report is empty and so should not be displayed"""
