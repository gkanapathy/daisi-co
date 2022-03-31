import pandas as pd
import numpy as np

def tag(itemlist: list):
    cats = ["one", "two", "three"]
    return [(i, cats[0] for i in itemlist]
