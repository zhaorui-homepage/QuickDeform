function a = tm(magnitude,depth,strike,dip,rake)
[E,N] = meshgrid(linspace(-100,100,100));
N=-N;

% E,N,DEPTH,STRIKE,DIP,LENGTH,WIDTH,RAKE,SLIP,OPEN
%[uE,uN,uZ,geom] = quickquake(E,N,magnitude,depth,strike,dip,rake);
[uE,uN,uZ,geom] = quickquake(E,N,magnitude,depth,strike,dip,rake);

% ascending LOS, wrapped
the1=34;arfa1=-14;
A=[sind(the1)*sind(arfa1) -sind(the1)*cosd(arfa1) cosd(the1)];
asc=A(1).*uN+A(2).*uE+A(3).*uZ;
% Wasc = wrapmod(-4*pi/6 * asc,2*pi);


% descending LOS, wrapped
the1=34;arfa1=193;
A=[sind(the1)*sind(arfa1) -sind(the1)*cosd(arfa1) cosd(the1)];
desc=A(1).*uN+A(2).*uE+A(3).*uZ;
% Wdesc = wrapmod(-4*pi/6 * desc,2*pi);



a.e = uE;
a.n = uN;
a.z = uZ;
a.asc = asc;
a.desc = desc;

