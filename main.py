
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

    USER_ERROR = -1
    UNKNOWN_ERROR = 0
    SERVER_ERROR = 1
    RATE_LIMIT_ERROR = 2
    INVALID_REQUEST_ERROR = 3
    EXPIRED_ACCESS_TOKEN_ERROR = 4
    INVALID_ACCESS_TOKEN_ERROR = 5
    PROHIBITED_CONCURRENT_QUERY_ERROR = 6
    AUTHENTICATION_ERROR = 7
    CLOUDFLARE_ERROR = 8


class Error(ChatbotError):
    """
    Base class for exceptions in V1 module.
    """

    def __init__(
        self,
        source: str,
        message: str,
        *args: object,
        code: Union[ErrorType, int] = ErrorType.UNKNOWN_ERROR,
    ) -> None:
        self.source: str = source
        self.message: str = message
        self.code: ErrorType | int = code
        super().__init__(*args)

    def __str__(self) -> str:
        return f"{self.source}: {self.message} (code: {self.code})"

    def __repr__(self) -> str:
        return f"{self.source}: {self.message} (code: {self.code})"


class AuthenticationError(ChatbotError):
    """
    Subclass of ChatbotError

    The object of the error thrown by a validation failure or exception
    """

    def __init__(self, *args: object) -> None:
        if SUPPORT_ADD_NOTES:
            super().add_note(
                "Please check if your key is correct, maybe it may not be valid",
            )
        super().__init__(*args)


class APIConnectionError(ChatbotError):
    """
    Subclass of ChatbotError

    An exception object thrown when an API connection fails or fails to connect due to network or
    other miscellaneous reasons
    """

    def __init__(self, *args: object) -> None:
        if SUPPORT_ADD_NOTES:
            super().add_note(
                "Please check if there is a problem with your network connection",
            )
        super().__init__(*args)


class NotAllowRunning(ActionNotAllowedError):
    """
    Subclass of ActionNotAllowedError

    Direct startup is not allowed for some reason
    """


class ResponseError(APIConnectionError):
    """
    Subclass of APIConnectionError

    Error objects caused by API request errors due to network or other miscellaneous reasons
    """


class OpenAIError(APIConnectionError):
    """
    Subclass of APIConnectionError

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

    USER_ERROR = -1
    UNKNOWN_ERROR = 0
    SERVER_ERROR = 1
    RATE_LIMIT_ERROR = 2
    INVALID_REQUEST_ERROR = 3
    EXPIRED_ACCESS_TOKEN_ERROR = 4
    INVALID_ACCESS_TOKEN_ERROR = 5
    PROHIBITED_CONCURRENT_QUERY_ERROR = 6
    AUTHENTICATION_ERROR = 7
    CLOUDFLARE_ERROR = 8


class Error(ChatbotError):
    """
    Base class for exceptions in V1 module.
    """

    def __init__(
        self,
        source: str,
        message: str,
        *args: object,
        code: Union[ErrorType, int] = ErrorType.UNKNOWN_ERROR,
    ) -> None:
        self.source: str = source
        self.message: str = message
        self.code: ErrorType | int = code
        super().__init__(*args)

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

    USER_ERROR = -1
    UNKNOWN_ERROR = 0
    SERVER_ERROR = 1
    RATE_LIMIT_ERROR = 2
    INVALID_REQUEST_ERROR = 3
    EXPIRED_ACCESS_TOKEN_ERROR = 4
    INVALID_ACCESS_TOKEN_ERROR = 5
    PROHIBITED_CONCURRENT_QUERY_ERROR = 6
    AUTHENTICATION_ERROR = 7
    CLOUDFLARE_ERROR = 8


class Error(ChatbotError):
    """
    Base class for exceptions in V1 module.
    """

    def __init__(
        self,
        source: str,
        message: str,
        *args: object,
        code: Union[ErrorType, int] = ErrorType.UNKNOWN_ERROR,
    ) -> None:
        self.source: str = source
        self.message: str = message
        self.code: ErrorType | int = code
        super().__init__(*args)

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

    USER_ERROR = -1
    UNKNOWN_ERROR = 0
    SERVER_ERROR = 1
    RATE_LIMIT_ERROR = 2
    INVALID_REQUEST_ERROR = 3
    EXPIRED_ACCESS_TOKEN_ERROR = 4
    INVALID_ACCESS_TOKEN_ERROR = 5
    PROHIBITED_CONCURRENT_QUERY_ERROR = 6
    AUTHENTICATION_ERROR = 7
    CLOUDFLARE_ERROR = 8


class Error(ChatbotError):
    """
    Base class for exceptions in V1 module.
    """

    def __init__(
        self,
        source: str,
        message: str,
        *args: object,
        code: Union[ErrorType, int] = ErrorType.UNKNOWN_ERROR,
    ) -> None:
        self.source: str = source
        self.message: str = message
        self.code: ErrorType | int = code
        super().__init__(*args)

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
