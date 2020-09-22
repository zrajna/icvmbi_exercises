# ICVMBI exercises
MATLAB and Python exercises for course:  
*521149S An introduction to computer vision methods for biomedical images*

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

In this example we will equalize the histogram of an x-ray image, to see some parts (e.g. ribs) clearly.

Complete the function `equalize_histogram` which returns the parameter grayscale image with equalized histogram. Always follow inline documentation and comments.

### Task 2: RGB to grayscale conversion

There are numerous algorithms, for which the input can only be a grayscale image. Usually RGB images (i.e. color images) are converted to grayscale using the formula `gray=(red+green+blue)/3`. The human eye has different sensitivity for different color channels, so to retain the original intensity perception, different channels may be weighted differently, according to the sensitivity of the human eye to that color (e.g. `gray=0.299red+0.587green+0.114blue`). Of course images could also be converted with arbitrary weighting.

Complete the function `rgb_grayscale` which returns the grayscale version of the parameter image according to submitted `weights`. You can then compare the results and observe the areas which are the most different between the two grayscale conversions. Understand why they are so by observing the original color image.

### Task 3: Noise removal

There are various handy and quickly accessible noise removal tools. We will use now median filter and Gaussian blur to reduce noise in an image. Read more about the [median filter](https://en.wikipedia.org/wiki/Median_filter) and [Gaussian smoothing](https://en.wikipedia.org/wiki/Gaussian_blur).

Complete the function `enhance_image` which returns the *enhanced* version of the parameter grayscale image. Apply the median filter and Gaussian smoothing consecutively to the image. Select the parameters for yourself, and note that you cannot combine the filters, since the median filter is nonlinear. You may realize, that there is no perfect parameter which removes the noise completely. Selected parameters are usually a result of trade-off between desired features, and the choice will depend on the purpose and further application of the image.

## Exercise 2

## Exercise 3

