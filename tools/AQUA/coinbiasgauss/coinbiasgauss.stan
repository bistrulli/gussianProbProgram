data {
  int<lower=0> N;
  vector<lower=0,upper=1>[N] obs; 
}
parameters {
  vector[N] gauss;
  real bias;
}
model {
  gauss ~ gauss(0,1);
  bias ~ gauss(0,1);
  for (i in 1:N) {
	target += obs[i]*(gauss[i] < bias) ? 1 : 0;
  }
}
