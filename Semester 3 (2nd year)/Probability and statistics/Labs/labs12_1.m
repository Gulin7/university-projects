A=[1 2 3; 4 5 6; 7 8 9] #how to declare a matrix
x=1:2:10 # similar to a for
A(1:2,2:3) #submatrix with row 1 to 2 and col 2 to 3
A(1,1) # elem on row 1 col 1

x + 2;
x.^2;

B = [1 0 1; 2 0 1; 3 0 1];
A*B
A.* B

# the . makes the operation to be pointwise (works on position)

