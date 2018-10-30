% Fonction principale du TP sur le filtre bilat�ral

clc
clear all
close all

%% Denoising
% Il s'agit d'une simple application du filtre bilat�ral.

noise = rgb2hsv(imread('../data/taj-rgb-noise.jpg'));
figure;
%imshow(noise(:,:,3)); title('Image originale (bruit�e)');


% TODO Question 1 :
filtered = bilateralFilter(noise(:,:,3),[],0,1,min(size(noise,1),size(noise,2))/16,1/4);
figure;
%imshow(filtered); title('Image filtr�e');

%% Tone mapping
% Il s'agit de compresser la plage d'intensit�es d'une image en pr�servant
% les d�tails. Pour cela, on diminue les contrastes globaux en conservant
% les contrastes locaux.

% lecture de l'image hdr (� partir de 3 expositions diff�rentes)
srcFolder = '../data/hdr/memorial/'; ext = '.png';
src = double(imread([srcFolder 'low' ext])) + double(imread([srcFolder 'mid' ext])) + double(imread([srcFolder 'high' ext]));
figure; imshow(src); title('Avant normalization')
% normalisation
ReductionULineaire = src - min(src(:));
ReductionULineaire = ReductionULineaire./max(ReductionULineaire(:));
figure; imshow(ReductionULineaire); title('Réduction uniforme linéaire')

% Filtrage avec filtres Gaussien et bilatéral (Question 2)
filteredGauss(:,:,1) = imgaussfilt(src(:,:,1),250);
filteredGauss(:,:,2) = imgaussfilt(src(:,:,2),250);
filteredGauss(:,:,3) = imgaussfilt(src(:,:,3),250);

disp(max(filteredGauss(:)));
disp(min(filteredGauss(:)));



figure; imshow(filteredGauss); title('Image apres filtre gaussien')

diffGauss = src - filteredGauss;
figure; imshow(diffGauss); title('DiffGauss')

filteredBillateral(:,:,1) = bilateralFilter(src(:,:,1),[],min(src(:)),max(src(:)),min(size(src,1),size(src,2))/16,1/4);
filteredBillateral(:,:,2) = bilateralFilter(src(:,:,2),[],min(src(:)),max(src(:)),min(size(src,1),size(src,2))/16,1/4);
filteredBillateral(:,:,3) = bilateralFilter(src(:,:,3),[],min(src(:)),max(src(:)),min(size(src,1),size(src,2))/16,1/4);

%figure; imshow(filteredBillateral); title('Image apres filtre bilateral')

diffBilateral = src - filteredBillateral;
%figure; imshow(diffBilateral); title('DiffBilateral')



