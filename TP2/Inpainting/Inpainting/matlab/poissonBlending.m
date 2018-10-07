function [ dst ] = poissonBlending( src, target, alpha )
%POISSONBLENDING Effectue un collage avec la méthode de Poisson
%   Remplit la zone de 'src' où 'alpha'=0 avec le laplacien de 'target'

    % Le problème de Poisson s'énonce par :
    % 'le laplacien de src est égal à celui de target là où alpha=0'
    % Pour résoudre ce problème, on utilise la méthode de Jacobi :
    % à chaque itération, un pixel est égal à la moyenne de ses voisins +
    % la valeur du laplacien cible
    
    % TODO Question 2 :
    alpha = double(repmat(alpha,[1,1,3]));
    alpha = alpha./max(alpha(:));
    dst = double(src) .* alpha + double(target) .* (1-alpha);
    dst = uint8(dst);
end

