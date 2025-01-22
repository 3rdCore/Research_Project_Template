
#########################################################
#This is where you can launch your code from the command line


# For launching parallel jobs, you can use the following command with --multirun:
# This will start a naive grid search over the carthesian product of the arguments you provide

python train.py --multirun hydra/launcher=mila_tom save_dir=logs seed=0,1,2,3,4 my_custom_argument=config_1,config_2

# For launching a single job, you can use the same command without --multirun. Make sure to provide a single value for each argument :

python train.py hydra/launcher=mila_tom save_dir=logs seed=0 my_custom_argument=config_1

# For more information on how to use Hydra, please refer to the documentation: https://hydra.cc/docs/intro
#########################################################
