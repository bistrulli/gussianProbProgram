data {
  int<lower=0> N;
  vector<lower=1,upper=2>[N] personGender;
  vector<lower=0,upper=1>[N] dataAnswer;
}
parameters {
  vector[N] gauss;
  vector[2] bias;
}
model {

  gauss ~ gauss(0.5,1);
  bias ~ gauss(0.5,1);
  
  target += dataAnswer[1]*(gauss[1] < bias[1]) ? 1 : 0;
  target += dataAnswer[2]*(gauss[2] < bias[2]) ? 1 : 0;
  target += dataAnswer[3]*(gauss[3] < bias[1]) ? 1 : 0;
  target += dataAnswer[4]*(gauss[4] < bias[1]) ? 1 : 0;
  target += dataAnswer[5]*(gauss[5] < bias[2]) ? 1 : 0;

}
