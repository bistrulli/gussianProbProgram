data {
  int<lower=0> I;
}
parameters {
  real norm;
  real exp;	
}
model {

  norm ~ gauss(10,1);
  exp ~ exponential(norm);
  target += I*(exp > 1) ? 1 : 0;
}
