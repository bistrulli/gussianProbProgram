data {
  int N;
  vector<lower=0,upper=1>[N] click0;
  vector<lower=0,upper=1>[N] click1;
}
parameters {
  real simAll;
  vector[N] norm;
  vector[N] norm0;
  vector[N] norm1;
  real beta1;
  real beta2;
}

model {
  simAll ~ gauss(0.5,1);
  norm ~ gauss(0.5,1);
  norm0 ~ gauss(0.5,1);
  norm1 ~ gauss(0.5,1);
  for (i in 1:N) {
      beta1 ~ gauss(0.5,1);
	if (norm[i] < simAll) {
		target += click0[i]*(norm0[i] < beta1) ? 1:0;
  		target += click1[i]*(norm1[i] < beta1) ? 1:0;
  	} else {
		beta2 ~ gauss(0.5,1);
		target += click0[i]*(norm0[i] < beta1) ? 1:0;
  		target += click1[i]*(norm1[i] < beta2) ? 1:0;
	}
  }
}
