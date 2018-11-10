% Fonction principale du TP sur le filtre bilat�ral

clc
clear all
close all

%% Denoising
% Il s'agit d'une simple application du filtre bilat�ral.

noise = rgb2hsv(imread('../data/taj-rgb-noise.jpg'));
figure;
imshow(noise(:,:,3)); title('Image originale (bruit�e)');


% TODO Question 1 :
filtered = bilateralFilter(noise(:,:,3),[],0,1,min(size(noise,1),size(noise,2))/16,1/4);
figure;
imshow(filtered); title('Image filtr�e');

%% Tone mapping
% Il s'agit de compresser la plage d'intensit�es d'une image en pr�servant
% les d�tails. Pour cela, on diminue les contrastes globaux en conservant
% les contrastes locaux.

% lecture de l'image hdr (� partir de 3 expositions diff�rentes)
srcFolder = '../data/hdr/memorial/'; ext = '.png';
src = double(imread([srcFolder 'low' ext])) + double(imread([srcFolder 'mid' ext])) + double(imread([srcFolder 'high' ext]));


% normalisation
src = src - min(src(:));
src = src./max(src(:));

figure; imshow(src); title('Avec Reduction uniforme Lineaire')

src = rgb2hsv(src);

% Filtrage avec filtres Gaussien et bilatéral (Question 2)

filteredGauss(:,:,3) = imgaussfilt(src(:,:,3),6);
filteredGauss(:,:,3) = src(:,:,3) - filteredGauss(:,:,3);
filteredGauss = filteredGauss-min(filteredGauss(:));
filteredGauss = filteredGauss./max(filteredGauss(:));
filteredGauss(:,:,1) = src(:,:,1);
filteredGauss(:,:,2) = src(:,:,2);
filteredGauss = hsv2rgb(filteredGauss);

figure; imshow(filteredGauss); title('Avec passe-haut Gaussien');


filteredBillateral(:,:,3) = bilateralFilter(src(:,:,3),[],min(min(src(:,:,3))),max(max(src(:,:,3))),25,1/4);
filteredBillateral(:,:,3) = src(:,:,3) - filteredBillateral(:,:,3);
filteredBillateral = filteredBillateral-min(filteredBillateral(:));
filteredBillateral = filteredBillateral./max(filteredBillateral(:));

filteredBillateral(:,:,1) = src(:,:,1);
filteredBillateral(:,:,2) = src(:,:,2);
filteredBillateral = hsv2rgb(filteredBillateral);

figure; imshow(filteredBillateral); title('Avec passe-haut Bilateral')





