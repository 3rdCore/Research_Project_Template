# Your Research Project 

This repo is a template for your future research project. It includes a set of tools and best practices that I have found useful in my own research projects. The tools and best practices are based on my experience and the experience of others. The goal of this template is to help you quick-start a research project with a fully functional environment and backbones for the project structure. Feel free to use this template and modify it to fit your needs. The template includes the following tools and best practices:

- [Pytorch Lightning](https://lightning.ai/docs/pytorch/stable/)
- [Hydra](https://hydra.cc/)
- [Pre-commit](https://pre-commit.com/)
- [Unit Testing](https://docs.pytest.org/en/6.2.x/)
- [WandB integration](https://wandb.ai/site)
- [CI with Github Actions](https://docs.github.com/en/actions)

...and additional utilities including a ready-to-use Jupiter notebook for making reproducible Seaborn plots,s pulling data directly from your WandB account. 

## Description of the tools

### Pytorch Lightning
The template is build around the Pytorch lightning framework, so it's expected that you implement your different modules following the lightning formalism. More info about Pytorch Lightning can be found [here](https://lightning.ai/docs/pytorch/stable/). The different modules are organized in the `src` folder :
- `src/model.py` :  This is where you define the architecture and forward function of the models that you will use in your project. Each model should be a class that inherits from `pl.LightningModule`.
- `src/dataset.py` : This is where you define the datasets and datamodules that you will use in your project. Each dataset should be a class that inherits from `torch.utils.data.Dataset` and each dataModule should be a class that inherits from `pl.LightningDataModule`.
- `src/task.py` :  This is where you define your task that defines your global forward function, your loss function, the train step, and the evaluation step. Additionally, you can define the metrics that you will use to evaluate your model and custom callbacks depending on usage.
- `src/train.py` : This is the main script that you will execute. It loads the configuration file, instantiate every sub-modules, and trains the model. It also saves the model and the logs in the `outputs` folder. 

### Hydra Configuration

The template uses the Hydra configuration system to manage the different hyperparameters of the project. The configuration files are located in the 'configs' folder. The main configuration file is `train.yaml` and it includes the different hyperparameters that you will use in your project. You can also define different configurations for different experiments, overwrite configs, create nested configs etc... The configuration system is very flexible and allows you to define your own configuration structure. More info about Hydra can be found [here](https://hydra.cc/).

### Pre-commit

The template uses the pre-commit system to ensure that the code is clean and formatted when working with multiple collaborators. The pre-commit hooks are defined in the `.pre-commit-config.yaml` file.

### Unit Testing

The template includes a unit test file `test.py` that you can use to test that each of your function works as expected. For simple projects, we do not recommend using unit tests.

### WandB integration

The template includes a WandB integration that allows you to log your experiments and results in a WandB project. The WandB integration is seemlessly integrated in the Pytorch Lightning framework. At each step of the training, you can log the different metrics that you want to monitor using the `self.log()` function.


## Installation
Python 3.6 or later is required. We recommend using a virtual environment to avoid packages conflicts with other projects. After activating your environment, to install the template, follow these steps:

1. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Set up the pre-commit hooks:

    ```bash
    pre-commit install
    ```

    Make sure you have the `.pre-commit-config.yaml` file set up in your project root.

3. If you're using WandB, you will need to specify your target for the WandB logger in the config file `configs/train.yaml`:

    ```yaml
    logger:
    _target_: lightning.pytorch.loggers.WandbLogger
    entity: # Add your wandb entity here
    project: # Add your wandb project here
    ```
Optionally, you can also remove the wandb logger and use the default logger.

## Usage

#to complete

```bash
For launching parallel jobs, you can use the following command with --multirun: This will start a naive grid search over the carthesian product of the arguments you provide

```bash
python train.py --multirun hydra/launcher=mila_tom save_dir=logs seed=0,1,2,3,4 my_custom_argument=config_1,config_2
```
For launching a single job, you can use the same command without --multirun. Make sure to provide a single value for each argument :
```bash
python train.py hydra/launcher=mila_tom save_dir=logs seed=0 my_custom_argument=config_1
```
# For more information on how to use Hydra, please refer to the documentation: https://hydra.cc/docs/intro

## Contribution

All kinds of contributions are welcome, e.g. adding more tools, better practices, discussions on trade-offs. Make sure to add any external dependencies to the `requirements.txt` file. If you add a new dependency, please make sure to add it to the `requirements.txt` file.
