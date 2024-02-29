%ask the user for number of simulations
N=input("Enter the number of simulations: ")
U= rand(3,N)
Y = (U<0.5)
X = sum(Y)
clf
hist(X)
%-----------------------------------------------

