pkg load statistics

x = [ 7 7 4 5 9 9 ...
4 12 8 1 8 7 ...
3 13 2 1 17 7 ...
12 5 6 2 1 13 ...
14 10 2 4 9 11 ...
3 5 12 6 10 7 ...];

#x = [7 7 4 5 9 9 4 12 8 1 8 7 3 13 2 1 17 7 12 5 6 2 1 13 14 10 2 4 9 11 3 5 12 6 10 7]

n = length(x);
one_minus_alpha = input("Enter the confidence level: ");
alpha = 1 - one_minus_alpha;

sigma = 5;
m1 = mean(x)-sigma/sqrt(n) * norminv(1 - alpha/2, 0,1);
m2 = mean(x)-sigma/sqrt(n) * norminv(alpha/2, 0,1);

printf("The confidence interval for the mean when you know sigma(5) is: (m1,m2) = (%4.3f,%4.3f)\n ", m1, m2);

m1b = mean(x) - std(x)/sqrt(n) * tinv(1 - alpha/2, n-1);
m2b = mean(x) - std(x)/sqrt(n) * tinv(alpha/2, n-1);

printf("(m1b,m2b) = (%4.3f,%4.3f)\n ", m1b, m2b);

# s is computed with var and s(simple) is computed with std

v1 = (n-1) * var(x)/chi2inv(1-alpha/2,n-1);
v2 = (n-1) * var(x)/chi2inv(alpha/2,n-1);

printf("The confidence interval for the var is: (v1,v2) = (%4.3f,%4.3f)\n ", v1, v2);

s1 = sqrt(v1);
s2 = sqrt(v2);

printf("The conf inter for the std is: (s1,s2) = (%4.3f,%4.3f)\n", s1,s2)
