%pdf:f(x) = P(X=x)
%cdf: F(x)=P(X<=x)
%c)
%P(X=0)
p1 = binopdf(0,3,0.5);
p2 = 1 - binopdf(1,3,0.5);
%d)P(X<=2)=F(2)
p3 = binopdf(2,3,0.5);
%p4 = ...;
%P(X<2) = P(X<=1)
%e)
%P(X>=1)=1-P(X<1)=1-P(X<=0)=1-P(X=0);
%f)N=?
%U=rand(3,N)
%Y=(U<0.5);
%X=sum(Y)
%clf
%hist(X)

