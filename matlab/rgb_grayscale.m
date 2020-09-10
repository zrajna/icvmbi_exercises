function J = rgb_grayscale(I, weights)
%RGB_GRAYSCALE Convert RGB image to grayscale
%   rgb_grayscale(I) transforms image I with 3 color channels to J
%   grayscale image according to specified weights; sum of weights is 1;
%   integer images are converted to double during the process

assert(3 == numel(weights), 'weights parameter should be a 3 element vector');
assert(abs(1-sum(weights)) < 1e-5, 'the sum of weights should be 1');
assert(3 == numel(size(I)), 'I should be an RGB image');
assert(3 == size(I,3), 'there should be 3 color channels in I');
I = im2double(I);

    % your code comes here, start with removing the following line
    J = squeeze(I(:,:,1));
    
end

