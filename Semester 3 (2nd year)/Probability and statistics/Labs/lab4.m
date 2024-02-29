#lab 4
%a

N =  input("give num of simuations: ");
p = input("input the probability to be between (0,1): ");

U = rand(1,N);
X = (U<p);

U_X =  [0 1];
n_X = hist(X, length(U_X));
rel_freq = n_X/N
