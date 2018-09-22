classdef descZernike
    %DESCZERNIKE Descripteur de forme de Zernike
    %   Utilise les moments de Zernike :
    %   on convolue la forme avec chaque polynôme    
    
    properties (Constant = true) % variables statiques
        
        resolution = 256; % resolution en pixels des polynômes
        maxOrder = 10; % ordre maximal des polynômes
        % tableau contenant tous les polynômes de zernike
        polynoms = descZernike.getPolynoms();
        descSize = size(descZernike.polynoms,3); % nombre de valuers de moments
    end
    
    methods (Static = true)
        
        % retourne le polynôme de zernike d'ordres suivants :
        % n -> ordre radial
        % m -> order angulaire
        function polynom = getPolynom( m, n )
            
            w = descZernike.resolution;
            
            % TODO Question 2 :
            polynom = zeros(w,w);
            for i=1:w
                for j=1:w
                   r = sqrt((i/256)^2 + (j/256)^2);
                   theta = atan2(i/256, j/256);
                   sum = 0;
                   if abs(r) <= 1
                      for k=0:(m-abs(n))/2
                         sum = sum + ((-1^k) * (factorial(m - k)) / (factorial(k) * factorial((m+abs(n))/2 - k) * factorial((m-abs(n))/2 - k)) * r^(m-2*k));
                      end
                   end
                   polynom(i,j) = sum * exp((j/256)*n*theta);
                end
            end
            
        end
        
        % calcule tout un set de polynômes de Zernike
        function polynoms = getPolynoms()
            polynoms = descZernike.getPolynom(0,0);
            for m = 1:descZernike.maxOrder
                for n = m:-2:0
                   polynom = descZernike.getPolynom( m, n );
                   polynoms(:,:,end+1) = polynom;
                end
            end
        end
        
        % redimensionne et translate une forme sur le disque unitaire
        function dst = rescale(shape)
             
             shape = double(shape);
             
             h = size(shape,1);
             w = size(shape,2);
             
             % on calcule le centre de la forme
             yCoords = repmat(linspace(1,h,h)',[1 w]);
             xCoords = repmat(linspace(1,w,w),[h 1]);
             % barycentre
             yCenter = round(mean(mean(shape.*yCoords))/mean(mean(shape)));
             xCenter = round(mean(mean(shape.*xCoords))/mean(mean(shape)));
             
             % on calcule le rayon maximal de la forme
             xCoords = xCoords-xCenter; yCoords = yCoords-yCenter;
             rCoords = (xCoords.*xCoords + yCoords.*yCoords).^0.5;
             rValues = rCoords.*(shape./max(shape(:)));
             rMax = floor(max(rValues(:)));
             
             % on recentre et redimensionne la forme
             dst = shape( max(1,yCenter-rMax) : min(yCenter+rMax,h), ...
                 max(1,xCenter-rMax) : min(xCenter+rMax,w) );
             dst = imresize(dst,size(shape));
        end
    end
    
    properties
       values; % réponses aux polynômes de Zernike
    end
    
    methods
        
         % constructeur (à partir d'une image blanche sur noire)
         function dst = descZernike(shape)
             % TODO Question 2 :
             shape = descZernike.rescale(shape);
             dst.values = zeros(1,descZernike.descSize);
             polynoms = descZernike.polynoms;
             for k=1:descZernike.descSize
                sum = 0; 
                for i = 1:size(shape, 2)
                    for j=1:size(shape, 1) 
                       sum = sum + shape(i,j) * polynoms(i,j,k); 
                    end
                end
                dst.values(k) = sum;
             end
             dst.values = abs(dst.values);
         end
         
        % distance entre deux descripteurs
        function d = distance(desc1, desc2)
            d = mean(abs(desc1.values - desc2.values));
        end
    end
end

