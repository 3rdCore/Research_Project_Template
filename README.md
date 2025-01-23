# 🚀 Your Research Project Template  

This template provides tools and best practices to quick-start your research project with a fully functional environment and backbones for your codebase. It is based on my own experience and the experience of others and aims to help you get started effectively. Feel free to use this template and modify it to suit your needs. The template includes the following:  

- ⚡ [Pytorch Lightning](https://lightning.ai/docs/pytorch/stable/): A framework to organize your deep learning research.
- 🔧 [Hydra](https://hydra.cc/): A powerful configuration management system.
- ✅ [Pre-commit](https://pre-commit.com/): A tool to ensure clean and formatted code.
- 🧪 [Unit Testing](https://docs.pytest.org/en/6.2.x/): For verifying that each function works as expected.
- 📊 [WandB integration](https://wandb.ai/site): For experiment tracking and visualization.
- 🤖 [CI with Github Actions](https://docs.github.com/en/actions): Continuous Integration setup to maintain project quality.

Additional utilities:
- Ready-to-use Jupyter notebook in `report/plots/notebook.ipynb` for making reproducible Seaborn plots, pulling data directly from your WandB project.
- Pre-implemented VScode debugger config file in `.vscode/launch.json` for debugging your code.

---

## 🛠️ Tools Overview  

### ⚡ PyTorch Lightning  
This template is built around the PyTorch Lightning framework. You are expected to organize your modules in the `src` folder:  
- `src/model.py`: Define your model architecture and the `forward` function. Each model should be a class inheriting from `pl.LightningModule`.  
- `src/dataset.py`: Define your datasets (`torch.utils.data.Dataset`) and datamodules (`pl.LightningDataModule`).  
- `src/task.py`: Implement your global forward function, loss function, train and evaluation steps, and metrics. Add custom callbacks if needed.  
- `src/train.py`: The main script. It loads the configuration file, instantiates components, trains the model, and saves logs and outputs.  

Learn more about PyTorch Lightning [here](https://lightning.ai/docs/pytorch/stable/).  

---

### 🔧 Hydra Configuration  
The template uses Hydra for flexible configuration management. Configuration files are stored in the `configs` folder:  
- `configs/train.yaml`: The main config file where you define hyperparameters.  

You can also define different configurations for different experiments, overwrite configs, create nested configs etc... The configuration system is very flexible and allows you to define your own configuration structure. Use Hydra to structure your configuration system effectively. More details [here](https://hydra.cc/).  

---

### ✅ Pre-commit  
Pre-commit hooks ensure that your code is clean and formatted before committing any change when working with multiple collaborators. The hooks are defined in the `.pre-commit-config.yaml` file. 
When the hooks are triggered, you need to re-commit any change it made. They are also automatically run by the CI pipeline on your remote repository to maintain code quality.
Install them with:  
```bash
pre-commit install
```  

---

### 🧪 Unit Testing  
A unit test file, `test_all.py`, is included to verify that each of your functions works as expected. While not mandatory for simple projects, it is a good practice for larger or collaborative projects. The tests are automatically run by the CI pipeline on your remote repository, and notifications are sent if any test fails.  

---

### 📊 WandB Integration  
Log experiments and metrics seamlessly with WandB. The integration is already included in the template, and logging is as simple as using the `self.log()` function in PyTorch Lightning. To configure WandB, just edit `configs/train.yaml`:  
```yaml
logger:
  _target_: lightning.pytorch.loggers.WandbLogger
  entity: # Add your WandB entity here
  project: # Add your WandB project here
```  
Learn more about WandB [here](https://wandb.ai/site).  

---

## ⚙️ Installation  
Python 3.6 or later is required. It is recommended to use a virtual environment to avoid package conflicts.  

1️⃣ Install dependencies:  
```bash
pip install -r requirements.txt
```  

2️⃣ Set up pre-commit hooks:  
```bash
pre-commit install
```  

3️⃣ Configure WandB (if applicable):  
Edit `configs/train.yaml` with your WandB entity and project information.  

4️⃣ You're good to go! 

---

## ▶️ Usage  

To run your code, simply execute the `train.py` script. Pass hyperparameters as arguments:  
```bash
python train.py seed=0 my_custom_argument=config_1
```  
This will launch a training run with the specified hyperparameters.

For parallel jobs on a cluster, use Hydra’s `--multirun` feature:  
```bash
python train.py --multirun seed=0,1,2,3,4 my_custom_argument=config_1,config_2
```  

If using Slurm, the default launcher config `hydra/launcher/slurm.yaml` based on the `submitit` plugin for Hydra will be used.

Learn more about Hydra [here](https://hydra.cc/docs/intro).  

---

## 🤝 Contribution 

This template is directly inspired by our project [PrequentialCode](https://github.com/3rdCore/PrequentialCode), made possible by Eric Elmoznino, and Tejas Kasetty.

All kinds of contributions are welcome! You can add tools, improve practices, or suggest trade-offs.  
👉 If you add external dependencies, make sure to update the `requirements.txt` file.  

---

Feel free to dive in and start your project! 🌟