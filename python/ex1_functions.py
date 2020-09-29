import numpy as np
import cv2.cv2 as cv


def equalize_histogram(img):
    """Returns img with equalized histogram.
    Args:
        img:            input grayscale image
    Returns:
        equalized_img:  brightness normalized and contrast increased grayscale image
    """
    # Your code comes here
    return img  # This just makes the function work, change it as you see fit!


def rgb_grayscale(img, weights):
    """Returns grayscale img converted with weights.
    Args:
        img:            input RGB image
        weights:        values to describe the sensitivity of the human eye to colors
                        (e.g. red:0.299,green:0.587,blue:0.114)
    Returns:
        grayscale_img:  converted grayscale image
    """
    # Your code comes here
    return img[..., 0].squeeze()  # This just makes the function work, change it as you see fit!


def enhance_image(img):
    """Returns enhanced version of img.
    Args:
        img:            input grayscale image
    Returns:
        filtered_img:   median and Gaussian filtered grayscale image
    """
    # Your code comes here
    return img  # This just makes the function work, change it as you see fit!
