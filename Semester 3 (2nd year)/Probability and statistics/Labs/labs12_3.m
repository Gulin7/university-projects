pkg load statistics

%Application2 lab2: a coin is tossed 3 times. X = number of heads that appear
%The distribution followed by X is a binomial ones
%It's parameters are: 3 num of trials n=3; p=0.5 probability
x = 0:1:3
px = binopdf(x,3,0.5);
%The probability distribution of x is:
%0 1 2 3
%1/8 3/8 3/8 1/8
%b): find the cumulative distribution function of X, Fx

