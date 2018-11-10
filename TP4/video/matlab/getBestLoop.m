function [ startFrame, endFrame ] = getBestLoop( src, minLength )
%GETBESTLOOP Calcule la paire de frames la plus ressemblante
%   minLength correspond à la taille minimale de la boucle vidéo
%   src correspond à une tableau 4D des pixels de la vidéo (w,h,col,frames)

    % TODO : Question 1
    startFrame = 1;
    endFrame = size(src,4);
    
end

