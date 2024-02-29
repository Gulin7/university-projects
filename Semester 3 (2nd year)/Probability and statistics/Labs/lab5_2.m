x1 = [22.4 21.7 24.5 23.4 21.6 23.3 22.4 21.6 24.8 20.0]
x2 = [17.7 14.8 19.6 19.6 12.1 14.8 15.4 12.6 14.0 12.2]

n1 = length(x1)
n2 = length(x2)

one_minus_alpha = input("Enter the confidence level: ");
alpha = 1 - one_minus_alpha;

printf("Solving the first ex");

sp = sqrt((n1-1)*var(x1) + (n2-1)*var(x2))/(n1+n2-1));

