%   ex1.m
%   Copyright (C) 2020  Zalan Rajna
%
%   This program is free software: you can redistribute it and/or modify
%   it under the terms of the GNU General Public License as published by
%   the Free Software Foundation, either version 3 of the License, or
%   (at your option) any later version.
%
%   This program is distributed in the hope that it will be useful,
%   but WITHOUT ANY WARRANTY; without even the implied warranty of
%   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
%   GNU General Public License for more details.
%
%   You should have received a copy of the GNU General Public License
%   along with this program.  If not, see <https://www.gnu.org/licenses/>.

close all;
clear;
tic;

%% Task 1
%   Histogram equalization
%   Hint: You can run a specific code section with Ctrl+Enter

xray = imread(fullfile('images','xray.png'));

figure;

subplot(221);
imshow(xray);
title('original xray image')
subplot(222);
imhist(xray);
title('histogram of original xray image')

xray_eq = equalize_histogram(xray);

subplot(223);
imshow(xray_eq);
title('modified xray image')
subplot(224);
imhist(xray_eq);
title('histogram of modified xray image')

%% Task 2
%   RGB to grayscale conversion
%   Hint: check out imwrite(I) function to save processed images to disk

hestain = imread(fullfile('images','hestain.png'));

figure;

subplot(221);
imshow(hestain);
title('original microscope image')

hestain_gray1 = rgb_grayscale(hestain, ones(1,3)./3);
subplot(223);
imshow(hestain_gray1);
title('equally weighted grayscale conversion')

hestain_gray2 = rgb_grayscale(hestain, [0.299, 0.587, 0.114]);
subplot(224);
imshow(hestain_gray2);
title('0.299R + 0.587G + 0.114B')

subplot(222);
hestain_diff = normalize_image(hestain_gray2 - hestain_gray1);
imshow(hestain_diff);
title('difference between grayscale conversions')

%% Task 3
%   Noise removal
%   Hint: in this exercise the final result is subjective

mri_pd = imread(fullfile('images','mri-pd.png'));

figure;

subplot(121);
imshow(mri_pd);
title('noisy proton density slice')

subplot(122);
mri_pd_enhanced = enhance_image(mri_pd);
imshow(mri_pd_enhanced);
title('enhanced proton density slice')

%% Runtime

disp(['Runtime (in seconds) was: ', num2str(toc)]);

%% Helper functions
%   You should write your functions in separate files

function J = normalize_image(I)
% Normalizes the image to have values stretched between 0 and 1
    J = im2double(I);
    J = J - min(J(:));
    J = J ./ max(J(:));
end
