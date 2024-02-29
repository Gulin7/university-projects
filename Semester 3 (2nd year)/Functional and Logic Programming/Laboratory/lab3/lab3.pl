A)
is_prime1(2).
is_prime1(3).
is_prime1(P) :-
    P > 3,
    P mod 2 =\= 0,
    \+is_prime2(P, 3).

is_prime2(N, D) :-
    N mod D =:= 0.
is_prime2(N, D) :-
    D * D < N,
    D2 is D + 2,
    is_prime2(N, D2).

dub([], Res, Res).
dub([], [], _).
dub([H|T], R, Res) :-
    is_prime1(H),
    dub(T, [H,H|R], Res).
dub([H|T], R, Res) :-
    \+is_prime1(H),
    dub(T, [H|R], Res).



B)

% Predicate to check if a number is prime
is_prime(2).
is_prime(3).
is_prime(N) :-
    N > 3,
    N mod 2 =\= 0,
    \+ has_factor(N, 3).

has_factor(N, F) :-
    N mod F =:= 0.
has_factor(N, F) :-
    F * F < N,
    F2 is F + 2,
    has_factor(N, F2).

% Predicate to duplicate prime numbers in a sublist
duplicate_primes([], []).
duplicate_primes([H|T], [HD|TD]) :-
    is_list(H),
    duplicate_primes_in_sublist(H, HD),
    duplicate_primes(T, TD).
duplicate_primes([H|T], [H|TD]) :-
    \+ is_list(H),
    duplicate_primes(T, TD).

duplicate_primes_in_sublist([], []).
duplicate_primes_in_sublist([H|T], [H, H|TD]) :-
    is_prime(H),
    duplicate_primes_in_sublist(T, TD).
duplicate_primes_in_sublist([H|T], [H|TD]) :-
    \+ is_prime(H),
    duplicate_primes_in_sublist(T, TD).
