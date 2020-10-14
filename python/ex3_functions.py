import numpy as np
import cv2.cv2 as cv


def basic_registration(moved, ref):
    """Returns registered (translated) version of moved.
    Hint: you should/can use cv.findTransformECC and cv.warpAffine functions
    Args:
        moved: grayscale image to register to ref
        ref:   reference image
    Returns:
        ret:   translated version of moved, registered to ref
    """
    # Your code comes here
    ret = moved  # This just makes the function work, change it as you see fit!

    return ret


def jisp2d(im1, im2):
    """Returns joint intensity scatter plot.
    Args:
        im1: image for scatter plot first axis
        im2: image for scatter plot second axis
    Returns:
        ret: joint intensity scatter plot (256x256 array of integers)
    """
    assert im1.size == im2.size
    jisp = np.zeros((256, 256), dtype=int)
    # Your code comes here

    return jisp
