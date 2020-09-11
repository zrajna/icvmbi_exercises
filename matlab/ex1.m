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
%   along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
subplot(222);
imhist(xray);

xray_eq = equalize_histogram(xray);

subplot(223);
imshow(xray_eq);
subplot(224);
imhist(xray_eq);

%% Task 2
%   RGB to grayscale conversion
%   Hint: check out imwrite(I) function to save processed images to disk

hestain = imread(fullfile('images','hestain.png'));

figure;

subplot(221);
imshow(hestain);

hestain_gray1 = rgb_grayscale(hestain, ones(1,3)./3);
subplot(223);
imshow(hestain_gray1);

hestain_gray2 = rgb_grayscale(hestain, [0.299, 0.587, 0.114]);
subplot(224);
imshow(hestain_gray2);

subplot(222);
hestain_diff = normalize_image(hestain_gray2 - hestain_gray1);
imshow(hestain_diff);

%% Task 3
%   Noise removal
%   Hint: in this exercise the final result is subjective

mri_pd = imread(fullfile('images','mri-pd.png'));

figure;

subplot(121);
imshow(mri_pd);

subplot(122);
mri_pd_enhanced = enhance_image(mri_pd);
imshow(mri_pd_enhanced);

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
