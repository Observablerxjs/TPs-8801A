function [ startFrame, endFrame ] = getBestLoop( src, minLength )
%GETBESTLOOP Calcule la paire de frames la plus ressemblante
%   minLength correspond à la taille minimale de la boucle vidéo
%   src correspond à une tableau 4D des pixels de la vidéo (w,h,col,frames)

    % TODO : Question 1
    startFrame = 1;
    endFrame = size(src,4);
    
    dist = Inf(size(src, 4), size(src, 4));
    
    for i=1:size(src,4)
        for j=i+1:size(src,4)
            dist(i,j) = sqrt(sum(sum(sum((double(src(:, :, :, i)) - double(src(:, :, :, j))).^2))));
            dist(j,i) = dist(i,j);
        end
    end
    
    wk = 1;
    m = 15;
    distFilt = Inf(size(src, 4), size(src, 4));
    
    for i=1:size(src,4)
        for j=i+1:size(src,4)
            if (j - i) < minLength
                distFilt(i, j) = Inf;
            else
                distFilt(i, j) = 0;
                for k=-m:m-1
                    distFilt(i, j) = distFilt(i, j) + (wk * dist(mod(i+k-1, size(src,4)) + 1, mod(j+k-1, size(src,4)) + 1));
                end
            end
        end
    end
    [M1, I1] = min(distFilt);
    [M2, I2] = min(M1);
    startFrame = I1(I2);
    endFrame = I2;
end

