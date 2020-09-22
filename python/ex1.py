#   ex1.py
#   Copyright (C) 2020  Zalan Rajna
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import path

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

from ex1_functions import equalize_histogram, rgb_grayscale, enhance_image


def make_cv_title(image, title, border_size=10):
    img_w_border = cv.copyMakeBorder(
        image,
        border_size,
        border_size,
        border_size,
        border_size,
        cv.BORDER_CONSTANT,
        value=[180, 180, 180],
    )
    rect = np.ones((4 * border_size, img_w_border.shape[1]), dtype=np.uint8) * 180
    rect_w_text = cv.putText(
        rect,
        title,
        (border_size, 3 * border_size),
        cv.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 0),
        2,
    )
    return cv.vconcat((rect_w_text, img_w_border))


def task1():
    """Task 1: Histogram equalization"""
    plt.figure()
    xray = cv.imread(path.join("images", "xray.png"), cv.IMREAD_GRAYSCALE)

    plt.subplot(2, 2, 1)
    plt.imshow(xray, cmap="gray")
    plt.axis("off")
    plt.title("original xray image")
    plt.subplot(2, 2, 2)
    plt.hist(xray.ravel(), 256)
    plt.ylim((0, 2e5))
    plt.axis("off")
    plt.title("histogram of original xray image")

    xray_eq = equalize_histogram(xray)

    plt.subplot(2, 2, 3)
    plt.imshow(xray_eq, cmap="gray")
    plt.axis("off")
    plt.title("modified xray image")
    plt.subplot(2, 2, 4)
    plt.hist(xray_eq.ravel(), 256)
    plt.ylim((0, 2e5))
    plt.axis("off")
    plt.title("histogram of modified xray image")

    plt.show()


def task2():
    """Task 2: RGB to grayscale conversion"""
    plt.figure()
    hestain = cv.imread(path.join("images", "hestain.png"), cv.IMREAD_COLOR)
    plt.subplot(2, 2, 1)
    plt.imshow(hestain)
    plt.axis("off")
    plt.title("original microscope image")

    hestain_gray1 = rgb_grayscale(hestain, np.ones((3,)) / 3)
    plt.subplot(2, 2, 3)
    plt.imshow(hestain_gray1, cmap="gray")
    plt.axis("off")
    plt.title("equally weighted grayscale conversion")

    hestain_gray2 = rgb_grayscale(hestain, np.array([0.299, 0.587, 0.114]))
    plt.subplot(2, 2, 4)
    plt.imshow(hestain_gray2, cmap="gray")
    plt.axis("off")
    plt.title("0.299R + 0.587G + 0.114B")

    hestain_diff = hestain_gray2 - hestain_gray1
    plt.subplot(2, 2, 2)
    plt.imshow(hestain_diff, cmap="gray")
    plt.axis("off")
    plt.title("difference between grayscale conversions")

    plt.show()


def task3():
    """Task 3: Noise removal"""
    mri_pd = cv.imread(path.join("images", "mri-pd.png"), cv.IMREAD_GRAYSCALE)
    mri_pd_w_title = make_cv_title(mri_pd, "noisy proton density slice")

    mri_pd_enhanced = enhance_image(mri_pd)
    mri_pd_enhanced_w_title = make_cv_title(mri_pd_enhanced, "enhanced proton density slice")

    # Show the image in an OpenCV window this time
    cv.imshow(
        "mri-pd (press any key to close)",
        np.hstack((mri_pd_w_title, mri_pd_enhanced_w_title)),
    )
    cv.waitKey(0)
    cv.destroyAllWindows()


def main():
    """ICVMBI exercise 1"""
    task1()
    task2()
    task3()


if __name__ == "__main__":
    main()
