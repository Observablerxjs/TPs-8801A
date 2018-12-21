function [ energy ] = getEnergy( img )
%GETENERGY Retourne la carte d'énergie des pixels d'une image
%   Diverses possibilités : Norme L1, L2, L2^2 du gradient, Saillance,
%   Détecteur de Harris, Détection de visage, entropie, etc...
%   La fonction doit pouvoir fonctionner avec un nombre indéfini de canaux !

	% TODO : Question 1
    [FX, FY] = gradient(img);
    
    normFX = zeros(size(FX,1),size(FX,2));
    normFY = zeros(size(FY,1),size(FY,2));
    
    for k=1:size(img,3)
        normFX = normFX + FX(:,:,k).^2;
        normFY = normFY + FY(:,:,k).^2; 
    end
    
    energy = (normFX + normFY).^(1/2);
end

