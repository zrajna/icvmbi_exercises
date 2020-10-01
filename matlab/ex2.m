%   ex2.m
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
%   Region growing segmentation
%   Hint: you should/can use imsegfmm function in fast_march

abdomen = imread(fullfile('images','abdomen.png'));

figure;

subplot(121);
imshow(abdomen);
title('original CT section');

seedpoint = [330, 170];

hold on;
plot(seedpoint(1), seedpoint(2), 'r+', 'MarkerSize', 30, 'LineWidth', 2);
legend('seed point', 'Location', 'bestoutside');

lung = fast_march(abdomen, seedpoint);

lung_overlaid = imoverlay(abdomen, lung, 'green');

subplot(122);
imshow(lung_overlaid);
title('segmented lung');

%% Task 2
%   Active contours segmentation
%   Hint: you should/can use activecontour function in segment_cells

cells = imread(fullfile('images','cells.png'));
cells = normalize_image(cells);

figure;

subplot(121);
imshow(cells);
title('original cells and initial mask');

roi = images.roi.Circle(gca, 'Center', [460, 430], 'Radius', 300);
mask = roi.createMask();

bin_result = segment_cells(cells, mask);

cells_overlay = imoverlay(cells, bin_result, 'green');

subplot(122);
imshow(cells_overlay);
title('segmented cells')

%% Task 3
%   Watershed segmentation
%   Hint: you should/can use watershed function in segment_colon

colon = imread(fullfile('images','colon.tif'));

figure;

subplot(121);
imshow(colon);
title('original colon image');

colon = rgb2gray(colon);
skeleton = segment_colon(colon);

colon_overlay = imoverlay(colon, skeleton, 'green');

subplot(122);
imshow(colon_overlay);
title('segmented colon (skeleton lines)')

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
