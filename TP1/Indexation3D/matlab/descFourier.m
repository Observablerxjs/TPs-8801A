classdef descFourier
    %DESCFOURIER Descripteur de forme de Fourier
    %   calcule le contour de la forme, et retourne
    %   sa transformée de Fourier normalisée
    
    properties (Constant = true)
        nbPoints = 128; % nombre de points du contour
        descSize = 16; % fréquences du spectre à conserver
    end
    
    properties
       values; % spectre du contour (taille 'nbFreq') 
    end
    
    methods
         % constructeur (à  partir d'une image blanche sur noire)
         function dst = descFourier(shape)
            shape = im2bw(shape);
            % Vous pouvez utiliser les fonctions matlab :
            % bwtraceboundary, interp1, etc..
            
            % TODO Question 1 :
            dst.values = zeros(1,descFourier.descSize);
            selPix = [0 0];
            for i=2:size(shape, 2) - 1
                for j=2:size(shape, 1) - 1
                    currPix = shape(i,j);
                    resH = (shape(i - 1, j - 1) ~= currPix) || (shape(i - 1, j) ~= currPix) || (shape(i - 1, j + 1) ~= currPix);
                    resB = (shape(i + 1, j - 1) ~= currPix) || (shape(i + 1, j) ~= currPix) || (shape(i + 1, j + 1) ~= currPix);
                    resG = shape(i, j - 1) ~= currPix;
                    resD = shape(i, j + 1) ~= currPix;
                    if (resH || resB || resG || resD) && currPix == 1
                       selPix = [i j];
                       break;
                    end
                end
            end
            cont = bwtraceboundary(shape, selPix, 'NW');
            sigInter = interp1(1:size(cont, 1), cont, linspace(1, size(cont,1), dst.nbPoints));
            sigInter1 = abs(sigInter);
            sigInter2 = sigInter1(2:end);
            sigInter3 = sigInter2/sigInter2(1);
            dst.values = sigInter3(1:dst.descSize);
         end
         
         % distance entre deux descripteurs
        function d = distance(desc1, desc2)
           
            d = mean(abs(desc1.values - desc2.values));
        end
    end
    
end

