import numpy as np
import cv2.cv2 as cv


def segment_lung(img, p):
    """Returns binary mask of lung.
    Hint: you should/can use cv.floodFill function
    Args:
        img:  input grayscale image
        p:    seed point as tuple
    Returns:
        ret:  binary mask of lung, same size as img
    """
    # Your code comes here
    ret = np.zeros(img.shape, dtype=np.uint8)  # This just makes the function work, change it as you see fit!
    return ret


def segment_cells(img, mask):
    """Returns binary mask of cells.
    Args:
        img:   input grayscale image
        mask:  initial region to shrink
    Returns:
        ret:   binary mask of cells, same size as img
    """
    # Your code comes here
    ret = np.zeros(img.shape, dtype=np.uint8)  # This just makes the function work, change it as you see fit!
    return ret


def segment_colon(img):
    """Returns binary skeleton between colon segments.
    Args:
        img:  input RGB color image
    Returns:
        ret:  binary skeleton between colon segments, same width and height as img
    """
    # Your code comes here
    ret = np.zeros(img.shape[:2], dtype=np.uint8)  # This just makes the function work, change it as you see fit!
    return ret
