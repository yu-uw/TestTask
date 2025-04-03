from contextlib import AbstractContextManager
from typing import Any, Callable, TypeVar, overload, Union, BinaryIO
from typing_extensions import Protocol

T = TypeVar("T", bound=Callable[..., Any])


def epic(name: str) -> Callable[[T], T]: ...


def feature(name: str) -> Callable[[T], T]: ...


def title(name: str) -> Callable[[T], T]: ...


@overload
def step(name: str) ->  AbstractContextManager[None]: ...
@overload
def step(func: T) -> T: ...

# Типы для allure.attach()
class AttachmentType(Protocol):
    PNG: str
    JPG: str
    TEXT: str
    JSON: str
    XML: str
    CSV: str
    HTML: str

attachment_type: AttachmentType

def attach(
    body: Union[bytes, str, BinaryIO],
    name: str,
    attachment_type: str = ...,
    extension: str = ...,
) -> None: ...