# lab4, c)
# geometric f = counts the faiures until the first success
# up to now: conver to 1 all that are less then p
# now we do it in reverse: X = (U>=p) -> count failures

p = input("Enter the prob of success (0,1): ");
n = input("Enter the number of trials: ");
N = input("Enter the no simulations: ");

#X is a line vector with only 0s
X = zeros(1,N);

for i=1:N
  X(i) = 0;

  while rand >=p
    X(i) = X(i)+1;
  endwhile
endfor

k = 0:20;
p_k = geopdf(k,p);


U_X = unique(X);
n_X = hist(X, length(U_X));
rel_freq = n_X/N;

clf # clear run

plot(U_X, rel_freq, '*',k,p_k,'ro');
