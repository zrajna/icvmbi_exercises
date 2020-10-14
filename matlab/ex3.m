%   ex3.m
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
%   Registering translated images
%   Hint: you should/can use imregcorr and imwarp/imtranslate functions in basic_registration

head = imread(fullfile('images','head.png'));
head_moved = imread(fullfile('images','head_moved.png'));

figure;

subplot(221);
imshow(head);
title('original head (1)');
subplot(222);
imshow(head_moved);
title('moved and noisy head (2)');


head_corrected = basic_registration(head_moved, head);

subplot(223);
imshow(head_corrected);
title('corrected and noisy head (3)');

sq_difference = (head - head_corrected).^2;

subplot(224);
imagesc(sq_difference);
title('squared difference (1,3)');
colorbar;

%% Task 2
%   Extraction of matching SIFT descriptors

mri1 = imread(fullfile('images','mri1.png'));
mri2 = imread(fullfile('images','mri2.png'));

figure;

subplot(221);
imshow(mri1);
title('MRI 1');

subplot(222);
imshow(mri2);
title('MRI 2');


pts1 = detectSURFFeatures(mri1, 'MetricThreshold', 100);
pts2 = detectSURFFeatures(mri2, 'MetricThreshold', 100);

[f1,vpts1] = extractFeatures(mri1, pts1, 'Upright', true);
[f2,vpts2] = extractFeatures(mri2, pts2, 'Upright', true);

indexPairs = matchFeatures(f1,f2) ;
matchedPoints1 = vpts1(indexPairs(:,1));
matchedPoints2 = vpts2(indexPairs(:,2));


ax = subplot(2, 1, 2);
showMatchedFeatures(mri1, mri2, matchedPoints1, matchedPoints2, 'Parent', ax);
title(ax, 'matching SIFT descriptors');

%% Task 3
%   Multimodal registration
%   Hint: image values start with 0, MATLAB array indexing starts with 1


body_ct = imread(fullfile('images','body_ct.png'));
body_mri = imread(fullfile('images','body_mri.png'));
body_mri_rot = imread(fullfile('images','body_mri_rotated.png'));

figure;

subplot(231);
imshow(body_ct);
title('CT body (1)');
subplot(232);
imshow(body_mri);
title('MRI body (2)');
subplot(233);
imshow(body_mri_rot);
title('MRI rotated body (3)');

jisp1 = jisp2d(body_ct, body_mri);
subplot(223);
imagesc(jisp1, [0, 50]);
xlabel('CT');
ylabel('MRI');
title('JISP of aligned imges (1,2)');
colorbar;

jisp2 = jisp2d(body_ct, body_mri_rot);
subplot(224);
imagesc(jisp2, [0, 50]);
xlabel('CT');
ylabel('MRI');
title('JISP of unaligned imges (1,3)');
colorbar;

%% Runtime

disp(['Runtime (in seconds) was: ', num2str(toc)]);
