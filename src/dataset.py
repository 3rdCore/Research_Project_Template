import copy
import warnings
from abc import ABC, abstractmethod
from typing import Any, Dict, Iterable, List, Literal, Optional

import numpy as np
import torch
import torch.nn as nn
from beartype import beartype
from lightning import LightningDataModule
from pytorch_lightning.utilities.seed import isolate_rng
from torch import FloatTensor, Tensor
from torch.utils.data import DataLoader, Dataset
from torchdata.datapipes.map import MapDataPipe

warnings.filterwarnings("ignore", message=".*does not have many workers.*")


class Custom_Dataset(Dataset):
    @beartype
    def __init__(
        self,
    ):
        super().__init__()
        # add your setup

        self.data, self.task_params = self.gen_data()

    @beartype
    def __len__(self) -> int:
        pass

    @beartype
    def __getitem__(
        self, index
    ) -> Any:  # be careful of the return type, please read lightning doc for best-practices
        pass

    @beartype
    @torch.inference_mode()
    def gen_data(
        self,
        n_samples: int,
    ) -> Any:  # be careful of the return type
        x = None
        y = None
        data_dict = {"x": x, "y": y}
        params_dict = None

        return data_dict, params_dict

    @abstractmethod
    def function(self, x: Tensor, params: dict[str, Tensor]) -> FloatTensor:
        """Applies the function defined using the params (function parameters)
        on the x(input data) to get y (output)

        Args:
            x (Tensor): input data with shape (n_tasks, n_samples, x_dim)
            params (int): function parameters with shape (n_tasks, ...)

        Returns:
            FloatTensor: y (output) with shape (n_tasks, n_samples, y_dim)
        """
        pass


class CustomDataModule(LightningDataModule):
    @beartype
    def __init__(
        self,
        train_dataset: Dataset,
        val_dataset: Dataset,
        batch_size: int,
        num_workers: int = 0,
    ):
        super().__init__()
        self.save_hyperparameters()
        self.train_dataset = train_dataset
        self.val_dataset = val_dataset

        # setup

    @beartype
    def train_dataloader(self) -> DataLoader:
        return DataLoader(
            self.train_dataset,
            batch_size=self.hparams.batch_size,
            num_workers=self.hparams.num_workers,
            shuffle=True,
            collate_fn=None,
        )

    @beartype
    def val_dataloader(self) -> DataLoader:
        return DataLoader(
            self.val_dataset,
            batch_size=self.hparams.batch_size,
            num_workers=self.hparams.num_workers,
            shuffle=False,
            collate_fn=None,
        )
