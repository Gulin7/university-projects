%2 a)
p = input("Enter a p between [0.05;0.95]: ")

for n=10:3:1000
  k = 0:n
  y = binopdf(k,n,p)
  plot(k,y)
  pause(0.5)
endfor
%

