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
    n = 10;
   
    deltaIR = del2(double(target(:,:,1)));
    deltaIG = del2(double(target(:,:,2)));
    deltaIB = del2(double(target(:,:,3)));
    
    deltaI = zeros(size(target, 1),size(target, 2),3);
    deltaI(:,:,1) = deltaIR;
    deltaI(:,:,2) = deltaIG;
    deltaI(:,:,3) = deltaIB;
    
    deltaISR = del2(double(src(:,:,1)));
    deltaISG = del2(double(src(:,:,2)));
    deltaISB = del2(double(src(:,:,3)));
    
    deltaIS = zeros(size(src, 1),size(src, 2),3);
    deltaIS(:,:,1) = deltaISR;
    deltaIS(:,:,2) = deltaISG;
    deltaIS(:,:,3) = deltaISB;
    
    alpha = double(repmat(alpha,[1,1,3]));
    alpha = alpha./max(alpha(:));
    dst = double(src) .* alpha + deltaI .* (1-alpha);
    dst = uint8(dst);
    
    antDst = dst;
    
    for k = 1:n
        results = double(dst) .* (1-alpha);
        for i=1:size(dst,1)
            for j=1:size(dst,2)
                if results(i,j) ~= 0
                    if i > 1 && i < size(dst, 1) && j > 1 && j < size(dst, 2)

                        dst(i,j,:) = (double(antDst(i-1,j,:)) + double(antDst(i+1,j,:)) ...
                                     + double(antDst(i,j-1,:)) + double(antDst(i,j+1,:)))./4 + deltaI(i,j,:);
                        %dst(i,j,:) = 4*antDst(i,j,:) - antDst(i-1,j,:) - antDst(i+1,j,:) - antDst(i,j-1,:) - antDst(i,j+1,:);
                    %elseif i ==1 && j == 1   
                    end
                end
            end
        end
        antDst = dst;
    end
    
        
        
end

