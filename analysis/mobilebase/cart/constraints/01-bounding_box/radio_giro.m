function  [dW, s] = radio_giro(theta, AW, LW)
  % pi1 = d/W
  % s = (for completeness, has to verify 0 <= s <= 1)
  % pi3 = A/W
  % pi4 = L/W (valor que se quiere obtener)
  % theta = en radianes, desde 0 a 90°, toda la curva

  pi3 = AW;
  pi4 = LW;

  st = sin(theta);
  ct = cos(theta);
  A = [-st, ct; -ct, -st];
  B = - [pi3; pi3] + pi4 * [ct; 0] + [st; ct];
  sol = linsolve(A, B);
  dW = sol(1);
  s = sol(2)/LW;
