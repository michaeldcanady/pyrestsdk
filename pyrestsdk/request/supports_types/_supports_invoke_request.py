from __future__ import annotations
from typing import Protocol, Optional, Union, List
from abc import abstractmethod

class SupportsInvokeRequest(Protocol):

    @abstractmethod
    def invoke_request(self) -> Optional[Union[List[T], T]]:
        """Invokes the prepared request
        """