
"""

import os
import platform
from enum import Enum
from typing import Union


python_version = list(platform.python_version_tuple())
SUPPORT_ADD_NOTES = int(python_version[0]) >= 3 and int(python_version[1]) >= 11


class ChatbotError(Exception):
    """
    Base class for all Chatbot errors in this Project
    """

    def __init__(self, *args: object) -> None:
        if SUPPORT_ADD_NOTES:
            super().add_note(
                "Please check that the input is correct, or you can resolve this issue by filing an issue",
            )
            super().add_note("Project URL: https://github.com/acheong08/ChatGPT")
        super().__init__(*args)


class ActionError(ChatbotError):
    """
    Subclass of ChatbotError

    An object that throws an error because the execution of an operation is blocked
    """

    def __init__(self, *args: object) -> None:
        if SUPPORT_ADD_NOTES:
            super().add_note(
                "The current operation is not allowed, which may be intentional",
            )
        super().__init__(*args)


class ActionNotAllowedError(ActionError):
    """
    Subclass of ActionError

    An object that throws an error because the execution of an unalloyed operation is blocked
    """


class ActionRefuseError(ActionError):
    """
    Subclass of ActionError

    An object that throws an error because the execution of a refused operation is blocked.
    """


class CLIError(ChatbotError):
    """
    Subclass of ChatbotError

    The error caused by a CLI program error
    """


class ErrorType(Enum):
    """
    Enumeration class for different types of errors.
    """
