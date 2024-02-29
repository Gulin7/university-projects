pkg load statistics

%Remove # from rows

%We ask the user to input the required values for the binomial
n = input("Give the num. of trials n= ")
p = input("Give the prob of succes p= ")
%n is a natural number
%p is a value between 0 and 1
%x is the num of succeses x values for the pdf
x=0:1:n
px=binopdf(x,n,p);
hold on
plot(x,px,'r+')
%if u wish to have multiple graphs in the same window
%write the command "hold on";
%to give values to the CDF (com distrib funct)
%you must always simulate continuity, that is:
xx=0:0.01:n;
fx=binocdf(xx,n,p)
plot(xx,fx,'b')
%use hold on & legend to put them together
%HOMEWORK:
%whenever u have the time, try to find out how legend works
%keep in mind: always use comments and ask for input
