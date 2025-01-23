import random
from abc import ABC, abstractmethod
from typing import Any, Iterable, Literal

import torch
from beartype import beartype
from lightning import Callback, LightningModule
from torch import Tensor


class my_custom_task(ABC, LightningModule):
    @beartype
    def __init__(
        self,
        lr: float = 1e-4,
    ):
        super().__init__()
        self.save_hyperparameters()  # ignore the instance of nn.Module that are already stored ignore=['my_module'])

    @beartype
    def forward(self, x: Any) -> Any:
        """Forward pass of the model."""
        pass

    @beartype
    def training_step(self, data, batch_idx) -> Tensor:
        pass
        # return loss #can also return a dict with key 'loss'

    @beartype
    def validation_step(self, data, batch_idx) -> Tensor:
        pass
        # return loss #can also return a dict with key 'loss'

    @abstractmethod
    def loss_function(self, target: Any, preds: Any) -> Tensor:
        """Loss function to be used in the training loop."""
        pass

    """ example of lightning hooks that can be overwrited
    @torch.inference_mode()
    def on_train_end(self):
        pass
    """

    def configure_optimizers(self) -> None:
        return torch.optim.Adam(self.parameters(), lr=self.hparams.lr)

    """example of property that can be added
    @property
    def is_a_lightning_module(self) -> bool:
        return True
    """


class MyCustomCallback(Callback):
    def __init__(self) -> None:
        super().__init__()

    def on_train_epoch_start(self, trainer, pl_module) -> None:  # pl_module is the LightningModule
        # setattr(pl_module, "my_param", new_param)
        pass
