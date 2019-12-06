import string
import numpy as np


def increment(x):
    return(x + 1)


def min_max_scaler(x):
    """Returns numpy array with original values scaled"""
    return (x - x.min()) / (x.max() - x.min())


def strip_punctuation(text):
    """Strips all punctations from text"""
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exclude)


def bag_of_words(text):
    """Returns set of words from the text"""
    text = strip_punctuation(text)
    words = set(text.split(' '))
    return words
