#   ex3.py
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

from ex3_functions import basic_registration, jisp2d


def task1():
    """Task 1: Registering translated images"""
    plt.figure()
    head = cv.imread(path.join("images", "head.png"), cv.IMREAD_GRAYSCALE)
    head_moved = cv.imread(path.join("images", "head_moved.png"), cv.IMREAD_GRAYSCALE)

    plt.subplot(2, 2, 1)
    plt.imshow(head, cmap="gray")
    plt.axis("off")
    plt.title("original head (1)")
    plt.subplot(2, 2, 2)
    plt.imshow(head_moved, cmap="gray")
    plt.axis("off")
    plt.title("moved and noisy head (2)")

    head_corrected = basic_registration(head_moved, head)

    plt.subplot(2, 2, 3)
    plt.imshow(head_corrected, cmap="gray")
    plt.axis("off")
    plt.title("corrected and noisy head (3)")

    sq_difference = np.square(head - head_corrected)

    plt.subplot(2, 2, 4)
    plt.imshow(sq_difference)
    plt.title("squared difference (1,3)")
    plt.axis("off")
    plt.colorbar()

    plt.show()


def task2():
    """Task 2: Extraction of matching SIFT descriptors"""
    plt.figure()
    mri1 = cv.imread(path.join("images", "mri1.png"), cv.IMREAD_GRAYSCALE)
    mri2 = cv.imread(path.join("images", "mri2.png"), cv.IMREAD_GRAYSCALE)

    plt.subplot(2, 2, 1)
    plt.imshow(mri1, cmap="gray")
    plt.axis("off")
    plt.title("MRI 1")

    plt.subplot(2, 2, 2)
    plt.imshow(mri2, cmap="gray")
    plt.axis("off")
    plt.title("MRI 2")

    # Initiate SIFT detector
    sift = cv.SIFT_create()

    # Find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(mri1, None)
    kp2, des2 = sift.detectAndCompute(mri2, None)

    # Brute Force Matcher with default params
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    matches = [[m] for m, n in matches if m.distance < 0.75 * n.distance]
    mri_matches = cv.drawMatchesKnn(
        mri1,
        kp1,
        mri2,
        kp2,
        matches,
        None,
        flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
    )

    plt.subplot(2, 1, 2)
    plt.imshow(mri_matches)
    plt.axis("off")
    plt.title("matching SIFT descriptors")

    plt.show()


def task3():
    """Task 3: Multimodal registration"""
    plt.figure()
    body_ct = cv.imread(path.join("images", "body_ct.png"), cv.IMREAD_GRAYSCALE)
    body_mri = cv.imread(path.join("images", "body_mri.png"), cv.IMREAD_GRAYSCALE)
    body_mri_rot = cv.imread(
        path.join("images", "body_mri_rotated.png"), cv.IMREAD_GRAYSCALE
    )

    plt.subplot(2, 3, 1)
    plt.imshow(body_ct, cmap="gray")
    plt.axis("off")
    plt.title("CT body (1)")
    plt.subplot(2, 3, 2)
    plt.imshow(body_mri, cmap="gray")
    plt.axis("off")
    plt.title("MRI body (2)")
    plt.subplot(2, 3, 3)
    plt.imshow(body_mri_rot, cmap="gray")
    plt.axis("off")
    plt.title("MRI rotated body (3)")

    jisp1 = jisp2d(body_ct, body_mri)
    plt.subplot(2, 2, 3)
    plt.imshow(jisp1, vmin=0, vmax=50)
    plt.xlabel("CT")
    plt.ylabel("MRI")
    plt.title("JISP of aligned imges (1,2)")
    plt.colorbar()

    jisp2 = jisp2d(body_ct, body_mri_rot)
    plt.subplot(2, 2, 4)
    plt.imshow(jisp2, vmin=0, vmax=50)
    plt.xlabel("CT")
    plt.ylabel("MRI")
    plt.title("JISP of unaligned imges (1,3)")
    plt.colorbar()

    plt.show()


def main():
    """ICVMBI exercise 3"""
    task1()
    task2()
    task3()


if __name__ == "__main__":
    main()
