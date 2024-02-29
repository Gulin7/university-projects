%Compute the no occurances of an element e in a list
%occ(l1l2...ln,X)={1+occ(l2,l3,...,ln,X),l1=x
%occ(l2,l3,...,ln,X),l1!=X
%0,n=0

occ([],_,0).
%list el no; flowmodel(i,i,o)/(i,i,i)
occ([H|T],X,No):-
    H=X,
    !,
    occ(T,X,NewNow),
    No is NewNo+1.
occ([H|T],X,No):-
    H\=X,
    occ(T,X,No).

