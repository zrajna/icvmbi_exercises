#   ex2.py
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
import cv2.cv2 as cv
from matplotlib import pyplot as plt
from skimage.draw import circle_perimeter

from ex2_functions import segment_lung, segment_cells, segment_colon


def task1():
    """Task 1: Region growing segmentation"""
    plt.figure()
    abdomen = cv.imread(path.join("images", "abdomen.png"), cv.IMREAD_GRAYSCALE)

    plt.subplot(1, 2, 1)
    plt.imshow(abdomen, cmap="gray")
    plt.axis("off")
    plt.title("original CT section")

    seedpoint = (330, 170)

    plt.plot(seedpoint[0], seedpoint[1], color='red', marker="+", markersize=20, linewidth=2)
    plt.legend('seed point', loc='upper left')

    lung = segment_lung(abdomen, seedpoint)

    background = np.zeros(abdomen.shape + (3, ), dtype=np.uint8)
    background[..., 1] = 255
    abdomen_masked = np.ma.masked_where(lung, abdomen)
    plt.subplot(1, 2, 2)
    plt.imshow(background)
    plt.imshow(abdomen_masked, cmap="gray")
    plt.axis("off")
    plt.title("segmented lung")

    plt.show()


def task2():
    """Task 2: Active contours segmentation"""
    plt.figure()
    cells = cv.imread(path.join("images", "cells.png"), cv.IMREAD_GRAYSCALE)

    plt.subplot(1, 2, 1)
    plt.imshow(cells, cmap="gray")
    plt.axis("off")
    plt.title("original cells and initial mask")

    center = (460, 430)
    radius = 300
    circle = plt.Circle(center, radius, color='deepskyblue', alpha=0.2)
    ax = plt.gca()
    ax.add_artist(circle)
    mask = np.zeros(cells.shape, dtype=np.uint8)
    mask[circle_perimeter(center[0], center[1], radius)] = True

    cells_bin = segment_cells(cells, mask)

    background = np.zeros(cells.shape + (3, ), dtype=np.uint8)
    background[..., 1] = 255
    abdomen_masked = np.ma.masked_where(cells_bin, cells)
    plt.subplot(1, 2, 2)
    plt.imshow(background)
    plt.imshow(abdomen_masked, cmap="gray")
    plt.axis("off")
    plt.title("segmented cells")

    plt.show()


def task3():
    """Task 3: Watershed segmentation"""
    plt.figure()
    colon = cv.imread(path.join("images", "colon.tif"))
    colon = cv.cvtColor(colon, cv.COLOR_BGR2RGB)

    plt.subplot(1, 2, 1)
    plt.imshow(colon)
    plt.axis("off")
    plt.title("original colon image")

    skeleton = segment_colon(colon)

    background = np.zeros(colon.shape, dtype=np.uint8)
    background[..., 1] = 255
    colon_gray = cv.cvtColor(colon, cv.COLOR_RGB2GRAY)
    colon_masked = np.ma.masked_where(skeleton, colon_gray)
    plt.subplot(1, 2, 2)
    plt.imshow(background)
    plt.imshow(colon_masked, cmap="gray")
    plt.axis("off")
    plt.title("segmented cells")

    plt.show()


def main():
    """ICVMBI exercise 2"""
    task1()
    task2()
    task3()


if __name__ == "__main__":
    main()
