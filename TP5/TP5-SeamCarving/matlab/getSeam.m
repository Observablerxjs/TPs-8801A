function [ seam ] = getSeam( costs )
%GETSEAM Retourne la seam verticale (un indice par ligne) de coût minimal
%   Remonte les coûts calculés pas la fonction "pathsCost"

    % TODO : Question 2
    h = size(costs,1);
    seam = ones(h,1);
    
    r_seam = find(costs(h, :)==min(costs(h, :)));
    seam(h) = r_seam(1,1);
    
    for i=h-1:-1:1
        if seam(i + 1) == 1
            minValue = min([costs(i, seam(i + 1)), costs(i, seam(i + 1) + 1)]);
            index = find(costs(i, seam(i + 1):seam(i + 1) + 1)==minValue) + seam(i + 1) - 1;
        elseif seam(i + 1) == size(costs,2)
            minValue = min([costs(i, seam(i + 1)), costs(i, seam(i + 1) - 1)]);
            index = find(costs(i, seam(i + 1) - 1:seam(i + 1))==minValue) + seam(i + 1) - 2;   
        else
            minValue = min([costs(i, seam(i + 1) - 1), costs(i, seam(i + 1)), costs(i, seam(i + 1) + 1)]);
            index = find(costs(i, seam(i + 1) - 1:seam(i + 1) + 1)==minValue) + seam(i + 1) - 2; 
        end
        seam(i) = index(1,1);
    end
end

