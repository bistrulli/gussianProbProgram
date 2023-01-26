parameters {
  real<lower=0,upper=1> nationality;
  real<lower=0,upper=1> perfect;
  real<lower=0,upper=10> gpa;
}

model {
  nationality ~ uniform(0,1);
  perfect ~ uniform(0,1);
  if (nationality < 0.5) {
  	if (perfect < 0.1) {
		gpa ~ uniform(8,10);
	}
	else {
		gpa ~ uniform(0,10);
	}
  } else {
	if (perfect < 0.15) {
		gpa ~ uniform(3,4);
	}
	else {
		gpa ~ uniform(0,4);
	}
  }

target += (nationality > 0.5 && gpa > 3) || (gpa >= 8 && gpa <= 10)? 1 : 0;
}
