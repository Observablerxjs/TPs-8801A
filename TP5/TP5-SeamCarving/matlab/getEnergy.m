function [ energy ] = getEnergy( img )
%GETENERGY Retourne la carte d'énergie des pixels d'une image
%   Diverses possibilités : Norme L1, L2, L2^2 du gradient, Saillance,
%   Détecteur de Harris, Détection de visage, entropie, etc...
%   La fonction doit pouvoir fonctionner avec un nombre indéfini de canaux !

	% TODO : Question 1
    energy = ones(size(img,1),size(img,2));
end

