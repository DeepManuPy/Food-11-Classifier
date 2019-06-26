import os

ORIG_INPUT_DATASET = "Food-11"
"""
initialize the base path to the new directory that will
contain our images after splitting.
"""
BASE_PATH = "dataset"
#define names of the split directories

TRAIN = "training"
TEST = "evaluation"
VAL = "validation"

#initialize the list of class label names
CLASSES = ["Bread","Dairy product","Dessert","Egg","Fried food","Meat","Noodles/Pasta",
"Rice","Seafood","Soup","Vegetable/Fruit"]
#set the batch size when fine-tuning
BATCH_SIZE = 32
# set the path to save model after training
MODEL_PATH = os.path.sep.join(["output","food11.model"])

UNFROZEN_PLOT_PATH = os.path.sep.join(["output","unfrozen.png"])
WARMUP_PLOT_PATH = os.path.sep.join(["output","warmup.png"])
