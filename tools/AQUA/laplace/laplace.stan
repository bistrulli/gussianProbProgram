data {
  int I;
}
parameters {
  real norm;
  real lap;	
}
model {

  norm ~ gauss(0,1);
  lap ~ double_exponential(norm, 1);
  target += I*(lap > 0) ? 1 : 0;
}
