function [ dst ] = poissonBlending( src, target, alpha )
%POISSONBLENDING Effectue un collage avec la méthode de Poisson
%   Remplit la zone de 'src' où 'alpha'=0 avec le laplacien de 'target'

    % Le problème de Poisson s'énonce par :
    % 'le laplacien de src est égal à celui de target là où alpha=0'
    % Pour résoudre ce problème, on utilise la méthode de Jacobi :
    % à chaque itération, un pixel est égal à la moyenne de ses voisins +
    % la valeur du laplacien cible
    
    % TODO Question 2 :
    
    %nombre d'iterations
    
    n = 100;
   
    deltaIR = 4*del2(double(target(:,:,1)));
    deltaIG = 4*del2(double(target(:,:,2)));
    deltaIB = 4*del2(double(target(:,:,3)));
    
    deltaI = zeros(size(target, 1),size(target, 2),3);
    deltaI(:,:,1) = deltaIR;
    deltaI(:,:,2) = deltaIG;
    deltaI(:,:,3) = deltaIB;
           
    
    alpha = double(repmat(alpha,[1,1,3]));
    alpha = alpha./max(alpha(:));
    dst = double(src) .* alpha;
    dst = uint8(dst);
        
    antDst = dst;
        
    for k = 1:n
        for i=1:size(dst,1)
            for j=1:size(dst,2)
                if alpha(i,j,:) ~= ones(1,1,3)
                    if i > 1 && i < size(antDst,1) && j > 1 && j < size(antDst,2)
                        dst(i,j,:) = (double(antDst(i-1,j,:)) + double(antDst(i+1,j,:)) ...
                                    + double(antDst(i,j-1,:)) + double(antDst(i,j+1,:)) + deltaI(i,j,:))./4;
                    end
                end
            end
        end
        antDst = dst;
    end        
end

