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
        """Predict different outputs given inputs x and latent representation z.

        Args:
            x (dict[str, Tensor]): Input data, each with shape (samples, tasks, *).
            z (dict[str, Tensor]): Computed latent representation, each with shape (samples, tasks, *).

        Returns:
            dict[str, Tensor]: Predicted values for output, each with shape (samples, tasks, *).
        """
        pass


class my_model(abstract_model):
    @beartype
    def __init__(
        self,
    ) -> None:
        super().__init__()

    @beartype
    def forward(self, x: Any) -> Any:
        """Predict given inputs x and model parameters z.

        Args:
            x (dict[str, Tensor]): Input data, each with shape (samples, tasks, *).
            z (dict[str, Tensor]): Aggregated context information, each with shape (samples, tasks, *).

        Returns:
            dict[str, Tensor]: Predicted values for y outputs, each with shape (samples, tasks, *).
        """
        pass

    @beartype
    def to(self, device):
        super().to(device)
        # custom .to operations here
        return self
