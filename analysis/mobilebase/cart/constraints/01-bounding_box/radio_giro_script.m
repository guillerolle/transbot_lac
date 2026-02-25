close all;
clear all;

A = 0.8;
W = linspace(0.5, A, 50);
theta = deg2rad(linspace(0,90,50));

LvsW = [];
for w = W
  L = linspace(0.5, 2.6*w, 50);

  dmin = [];
  for l = L
    d = [];
    for t = theta
      [dW, s] = radio_giro(t, A/w, l/w);
      d = [d, dW*w];
    endfor

  #plot(theta, d); grid on;
  dmin = [dmin, min(d)];

  #figure
  # hold on;
  endfor
  # plot(L/W, dmin>0, 'linewidth', 2); grid on;
  dd = find(dmin<0);
  L0 = interp1(dmin, L, 0);
  if size(dd)(2) == 0
    dd = size(dmin)(2);
  endif
  LvsW = [LvsW, L0/w];
endfor

figure(1)
plot(A./W, LvsW, 'linewidth', 2); xlabel('\lambda_2 = A/W'), ylabel('\lambda_1 = L/W'); grid on;

figsizecm = [4,3];
figure(2, "paperposition", [0,0,figsizecm(1), figsizecm(2)], "paperunits", "centimeters");

L_ = LvsW.*W;
plot(W*100, L_*100, 'linewidth', 8, 'displayname', 'Valid Combinations'); hold on;
%legend()
xl = xlim; yl = ylim;

fill( [W*100 xl(end) xl(1)], [L_*100, yl(1), yl(1)], 1, 'EdgeColor', 'none', 'facealpha', 0.5, 'HandleVisibility','off');

xlabel('W [cm]'), ylabel('L [cm]'); grid on; grid minor on;
set(gca, 'Position', [0.225, 0.225, 0.750, 0.725], 'linewidth', 1.5, 'fontsize', 18);
legend()

