function [ seam ] = getSeam( costs )
%GETSEAM Retourne la seam verticale (un indice par ligne) de coût minimal
%   Remonte les coûts calculés pas la fonction "pathsCost"

    % TODO : Question 2
    h = size(costs,1);
    seam = ones(h,1);
end

