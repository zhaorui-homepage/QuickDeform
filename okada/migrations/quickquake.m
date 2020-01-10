function [uE,uN,uZ,dis_geom] = quickquake(E,N,Mw,depth,strike,dip,rake);
%QUICKQUAKE This function uses empirical equations to calculate 3D ground
%deformation field
%	   Lat    : Epicenter, latitude 
%	   Lon    : Epicenter, longitude 
%	   M0     : Moment magnitude, N-m 
%	   E,N    : coordinates of observation points in a geographic referential 
%	            (East,North,Up) relative to fault centroid (units are described below)
%	   DEPTH  : depth of the fault centroid (DEPTH > 0)
%	   STRIKE : fault trace direction (0 to 360?relative to North), defined so 
%	            that the fault dips to the right side of the trace
%	   DIP    : angle between the fault and a horizontal plane (0 to 90?
%	   LENGTH : fault length in the STRIKE direction (LENGTH > 0)
%	   WIDTH  : fault width in the DIP direction (WIDTH > 0)
%	   RAKE   : direction the hanging wall moves during rupture, measured relative
%	            to the fault STRIKE (-180 to 180?.
%	   SLIP   : dislocation in RAKE direction (length unit)
%	   OPEN   : dislocation in tensile component (same unit as SLIP)
%	Formulas and notations from Okada [1985] solution excepted for strain 
%	convention (here positive strain means compression), and for the fault 
%	parameters after Aki & Richards [1980], e.g.:
%	      DIP=90, RAKE=0   : left lateral (senestral) strike slip
%	      DIP=90, RAKE=180 : right lateral (dextral) strike slip
%	      DIP=70, RAKE=90  : reverse fault
%	      DIP=70, RAKE=-90 : normal fault
%   [uE,uN,uZ] = quickquake(M0,depth,strike,dip,rake);

% Moment magnitude
% Mw = 2/3*(log10(M0))-6.03;
M0 = 10^((Mw+6.03)*3/2);


% % Blaser et al. (2010), 4.8 < Mw < 9.5
% length1 = 10.^(0.57*Mw-2.37);
% width1  = 10.^(0.46*Mw-1.86);

% Well & Coppersmith (1994)
length1 = 10.^((Mw-4.38)/1.49);
width1  = 10.^((Mw-4.06)/2.25)
halfheight = width1 * sind(dip) / 2;

slide = length1*5;

% % [E,N] = meshgrid(linspace(-50,50,100));

D = width1./2.*sind(dip);

if (depth - D) < 0 
    depth = D;
end

slp = M0/(30e+9 * length1 *width1 *1e+6);

[uE,uN,uZ] = okada85(E,N,depth,strike,dip,length1,width1,rake,slp,0);
uE = uE.*100; uN = uN.*100;uZ = uZ.*100; % unit: cm
dis_geom = [length1,width1,depth,-dip,strike,rake]';

end
