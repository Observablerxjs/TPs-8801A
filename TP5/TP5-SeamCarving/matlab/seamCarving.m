function [ dst ] = seamCarving( src, newHeight, newWidth )
%SEAMCARVING Redimensionne une image en préservant son contenu
%   Ne supprime que les pixels ne contenant pas d'information
%   Calcule d'abord la carte d'energie de l'image (contenu)
%   Puis calcule des 'seam' à enlever de l'image,
%   par programmation dynamique
%   Attention : src et dst peuvent avoir un nombre quelconque de canaux (4
%   ou plus, par exemple).

    % On redimensionne horizontalement
    dst = resizeH( src, newWidth );
    
    % On redimensionne verticalement
    dst = permute( dst,[2,1,3] ); % on tourne de 90deg
    dst = resizeH( dst, newHeight );
    dst = permute( dst,[2,1,3] );
end

% redimensionne horizontalement une image
function [ dst ] = resizeH( src, newWidth )

    % Choisit entre enlever ou ajouter des pixels
    if newWidth < size(src,2)
        dst = shrinkH( src, newWidth );
    else
        dst = enlargeH( src, newWidth );
    end
end

% Supprime des seams verticales
function dst = shrinkH( src, newWidth )

    % TODO : Question 3
    for k=1:size(src,2) - newWidth
       
        en = getEnergy(src);
        costs = pathsCost(en);
        seam = getSeam(costs);
        
        tmpImage = zeros(size(src,1), size(src,2) - 1, size(src,3));
        
        for i=1:size(seam, 1)
            tmpImage(i, :, :) = [src(i, 1:seam(i)-1,:), src(i, seam(i)+1:end,:)];
        end
        
        src = tmpImage;
    end
    
    dst = src;
    
end

% Duplique les pixels de seams verticales
function dst = enlargeH( src, newWidth )

    % TODO : Question 4
    
    for k=1:newWidth - size(src,2)
       
        en = getEnergy(src);
        costs = pathsCost(en);
        seam = getSeam(costs);
        
        tmpImage = zeros(size(src,1), size(src,2) + 1, size(src,3));
        
        for i=1:size(seam, 1)
            tmpImage(i, :, :) = [src(i, 1:seam(i)-1,:), src(i, seam(i)-1:end,:)];
        end
        
        src = tmpImage;
    end
    
    dst = src;
    
end