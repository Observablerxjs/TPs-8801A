function [ dst ] = clone( src, nbClones )
%CLONE Clone les personnages d'une boucle
%   src : frames de la vidéo (w,h,col,frames)
%   nbClones : nombre de clones (=0 si aucun clonage)

    % arguments par défault
    if nargin < 2, nbClones = 2; end

    % TODO : Question 2
    dst = src;
end

