from abc import ABC, abstractmethod
from typing import Any

import torch
from beartype import beartype
from torch import Tensor, nn
from torch.nn import functional as F


class abstract_model(ABC, nn.Module):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def forward(self, x: Any) -> Any:
        """Perform forward pass of the model."""
        pass


class my_model(abstract_model):
    @beartype
    def __init__(
        self,
    ) -> None:
        super().__init__()

    @beartype
    def forward(self, x: Any) -> Any:
        """Perform forward pass of the model."""
        pass

    @beartype
    def to(self, device):
        super().to(device)
        # custom .to operations here
        return self
