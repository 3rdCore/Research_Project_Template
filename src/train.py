import hydra
import torch
from lightning import Trainer, seed_everything
from omegaconf import OmegaConf

from utils import ast_eval

# torch.set_float32_matmul_precision("medium")  # or 'high' based on your needs


@hydra.main(config_path="../configs/", config_name="train", version_base=None)
def train(cfg):
    seed_everything(cfg.seed)
    dataset = hydra.utils.instantiate(
        cfg.datamodule
    )  # can also pass previously instantiated object : (attribute=my_attribute)!
    task = hydra.utils.instantiate(cfg.task)
    logger = hydra.utils.instantiate(cfg.logger) if cfg.logger else False
    callbacks = (
        [hydra.utils.instantiate(cfg.callbacks[cb]) for cb in cfg.callbacks] if cfg.callbacks else None
    )

    if logger:
        logger.experiment.config.update(OmegaConf.to_container(cfg, resolve=True))
        logger.experiment.config.update({"seed": cfg.seed})

    trainer = Trainer(
        logger=logger,
        callbacks=callbacks,
        enable_checkpointing=False,
        **cfg.trainer,
    )
    trainer.fit(model=task, datamodule=dataset)


if __name__ == "__main__":
    train()
