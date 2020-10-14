# ICVMBI exercises
MATLAB and Python exercises for course:  
*521149S An introduction to computer vision methods for biomedical images*

* [Exercise 1](#exercise-1) - image enhancement
* [Exercise 2](#exercise-2) - image segmentation
* [Exercise 3](#exercise-3) - image registration

Materials are based on previous courses and Jeff Orchard's [Medical Image Processing](https://cs.uwaterloo.ca/~jorchard/cs473/CS473/Lectures.html) course.

## General instructions

You are free to choose to complete the three exercises in ImageJ, MATLAB, or Python. You may also switch between them during the course.

Submit your solutions in [moodle](https://moodle.oulu.fi/course/view.php?id=4366&section=3).

Always follow inline documentation and comments, and only submit syntactically and semantically correct code.

If you find a typo, place for corrections or room for improvement in the task descriptions, create an issue on [github](https://github.com/zrajna/icvmbi_exercises/issues) and/or submit a [pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

You should make sure that you are using the latest template from this site before seeking assistance. :)

## Language specific instructions

* [MATLAB](matlab/README.md)
* [Python](python/README.md)

## Exercise 1

### Task 1: Histogram equalization

*“Histogram equalization is a method in image processing for contrast adjustment using the image's histogram.”* Read and understand the detailed description of the method at [https://en.wikipedia.org/wiki/Histogram_equalization](https://en.wikipedia.org/wiki/Histogram_equalization).

In this example you will equalize the histogram of an x-ray image, to see some parts (e.g. ribs) clearly.

Complete the function `equalize_histogram` which returns the parameter grayscale image with equalized histogram. Always follow inline documentation and comments.

### Task 2: RGB to grayscale conversion

There are numerous algorithms, for which the input can only be a grayscale image. Usually RGB images (i.e. color images) are converted to grayscale using the formula `gray=(red+green+blue)/3`. The human eye has different sensitivity for different color channels, so to retain the original intensity perception, different channels may be weighted differently, according to the sensitivity of the human eye to that color (e.g. `gray=0.299red+0.587green+0.114blue`). Of course images could also be converted with arbitrary weighting.

Complete the function `rgb_grayscale` which returns the grayscale version of the parameter image according to submitted `weights`. You can then compare the results and observe the areas which are the most different between the two grayscale conversions. Understand why they are so by observing the original color image.

### Task 3: Noise removal

There are various handy and quickly accessible noise removal tools. We will use now median filter and Gaussian blur to reduce noise in an image. Read more about the [median filter](https://en.wikipedia.org/wiki/Median_filter) and [Gaussian smoothing](https://en.wikipedia.org/wiki/Gaussian_blur).

Complete the function `enhance_image` which returns the *enhanced* version of the parameter grayscale image. Apply the median filter and Gaussian smoothing consecutively to the image. Select the parameters for yourself, and note that you cannot combine the filters, since the median filter is nonlinear. You may realize, that there is no perfect parameter which removes the noise completely. Selected parameters are usually a result of trade-off between desired features, and the choice will depend on the purpose and further application of the image.

## Exercise 2

You are not expected to get perfect results in the segmentation tasks, but the functions should roughly do what they are defined to do. If you wish to do plotting or preparing images yourself, also submit your modified `ex2` script with your solution. Otherwise your function should work as a drop-in replacement with the template.

Note the hints for functions to use. With some pre- and postprocessing, and setting the parameters carefully, it is possible to solve the segmentation problem with the suggested functions. However, you may freely choose alternatives as well.

*Python users!* The package list was updated in the Python virtual environment, refresh yours with `pip install -r requirements.txt` in your venv after pulling the latest changes in the repo. If you wish to use other packages, you should also submit your `requirements.txt` file with your solution.

### Task 1: Region growing segmentation

“Region growing is a simple region-based image segmentation method. It is also classified as a pixel-based image segmentation method since it involves the selection of initial seed points. This approach to segmentation examines neighboring pixels of initial seed points and determines whether the pixel neighbors should be added to the region. The process is iterated on, in the same manner as general data clustering algorithms.” Read the detailed description at [https://en.wikipedia.org/wiki/Region_growing](https://en.wikipedia.org/wiki/Region_growing).

In this task you will segment the lung from the image with a given seed point. Complete the function `segment_lung`, which returns the binary mask of the lung on the right side of the image.

### Task 2: Active contours

“Active contours evolve an initial contour in time according to multiple intrinsic geometric measures of the image. In the plugin implementation the measures are an edge based constraint, a grey value penalty and a curvature constraint which prevents them from leaking the object boundary at areas of poor edges. During curve evolution the active contours in this implementation can split and merge and thus be used to detect even multiple objects.” Read the detailed description at [https://se.mathworks.com/help/images/ref/activecontour.html](https://se.mathworks.com/help/images/ref/activecontour.html) or [https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_chan_vese.html](https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_chan_vese.html).

In this task you will segment the cells from the image background with a given initial binary mask. Complete the function `segment_cells`, which returns either the segmented cells within the mask or all of them in the image. Note, that the Chan-Vese algorithm might return the inverse, i.e. segment the background instead of the foreground, in which case you just need to return the negated result.

### Task 3: Watershed segmentation

Read about the idea of “watershed” of a greyscale image from [https://en.wikipedia.org/wiki/Watershed_(image_processing)](https://en.wikipedia.org/wiki/Watershed_(image_processing)).

In this task you will roughly segment the parts of the colon from the given microscope image. You initially will need to radically blur the image for the watershed segmentation to work as expected. Complete the function `segment_colon`, which returns the binary skeleton between the segments. You may use dilation (morphological operator) to strengthen the skeleton lines.

## Exercise 3

### Task 1: Basic registration

Let’s register translated images. You should apply intensity based registration which use cross-correlation techniques. Complete the function `basic_registration`, which returns the moved and noisy head image in alighment with the centered head image.

### Task 2: Extraction of matching descriptors

Run and understand the code snippet which extracts and matches feature descriptors between images. Check out [this nice explanation](https://medium.com/data-breach/introduction-to-feature-detection-and-matching-65e27179885d) of feature detection and matching. Familiarize yourself with at least the [SURF](https://medium.com/data-breach/introduction-to-surf-speeded-up-robust-features-c7396d6e7c4e) and [SIFT](https://medium.com/data-breach/introduction-to-sift-scale-invariant-feature-transform-65d7f3a72d40) descriptors.

There is no simple way to estimate non-rigid (elastic B-splines) transformation in MATLAB or Python/OpenCV (external libraries would be needed), but you can check out how the algorithm works in the [ImageJ task](https://moodle.oulu.fi/mod/assign/view.php?id=227920).

### Task 3: Multimodel registration

As an introduction to joint histograms used in multimodal registration, in this task you will see how it is affected by image rotation. Complete the function `jisp2d`, which calculates the joint intensity scatter plot between two images.

