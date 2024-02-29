#lab 4; b)

n = input("Enter the number of trials: ");
p = input("Enter the probability of success: ");
N = input("Enter the number of simulations: ");

U = rand(1,N);
X = sum(U<p); # getting 0s and 1s and then find out the no successes

k = 0:n; # vector of all those values
p_k = binopdf(k,n,p);

U_X = unique(X);
n_X = hist(X, length(U_X));
rel_freq = n_X/N;

clf # clear run

plot(U_X, rel_freq, '*',k,p_k,'ro');
