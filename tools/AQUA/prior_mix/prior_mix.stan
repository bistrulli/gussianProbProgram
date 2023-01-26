data {
 int<lower = 0> N;
 vector[N] y;
}

parameters {
    real<lower=-5,upper=5> mu;
}

model {
target += log_mix(0.8,normal_lpdf(mu| 4, 0.5), normal_lpdf(mu| -4, 0.5));
 for (n in 1:N)
    target += student_t_lpdf(y[n] | 5,  mu, 2);;
}
