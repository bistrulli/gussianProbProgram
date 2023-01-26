data {
  int<lower=0> N;
  vector<lower=0,upper=1>[N] y; 
}
parameters {
  vector[N] gauss;
  real theta;
}
model {
  gauss ~ gauss(0,1);
  theta ~ gauss(0,1);
  for (i in 1:N) { 
	target += y[i]*(gauss[i] < theta) ? 1 : 0;
  }
}
