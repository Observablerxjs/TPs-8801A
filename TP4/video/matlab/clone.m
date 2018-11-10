function [ dst ] = clone( src, nbClones )
%CLONE Clone les personnages d'une boucle
%   src : frames de la vidéo (w,h,col,frames)
%   nbClones : nombre de clones (=0 si aucun clonage)

    % arguments par défault
    if nargin < 2, nbClones = 2; end

    % TODO : Question 2
    dst = src;
    
    [startFrame, endFrame] = getBestLoop(src, 5);
    boucle = src(:, :, :, startFrame:endFrame);
    
    fond = uint8(sum(boucle, 4) ./ (endFrame - startFrame));
    
    elem = zeros(size(boucle, 1), size(boucle, 2), size(boucle, 4));
    res = uint8(zeros(size(boucle, 1), size(boucle, 2)));
    
    
    seuil = 5;
    
    for i=1: size(boucle, 4)
        res = rgb2gray(uint8(abs(double(boucle(:, :, :, i)) - double(fond))));
        indices = find(res < seuil);
        res(indices) = 0;
        elem(:, :, i) = double(res) ./ 255;
    end
    
    deph = 10;
    
    for i=1:size(boucle, 4)
        for j=1:nbClones
            boucle(:, :, :, i) = boucle(:, :, :, i) + uint8(elem(:, :, mod((i + j * deph) - 1, size(boucle, 4)) + 1) .* ...
                                 double(boucle(:, :, :, mod((i + j * deph) - 1, size(boucle, 4)) + 1)));
        end
    end
    
    dst = boucle;
    
end

