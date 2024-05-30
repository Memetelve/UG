parent(tata, syn).
parent(dziadek, tata).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).


% length(0,[]).
% length(N,[_|L]) :- length(M,L), N is M+1.

member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

factorial(0, 1).
factorial(X, Z) :-
    X > 0,
    Y is X - 1,
    factorial(Y, W),
    Z is W * X.


fib(0, 1).
fib(1, 1).
fib(N, X) :-
    N > 1,
    A is N - 1,
    B is N - 2,
    fib(A, M),
    fib(B, P),
    X is M + P.


gcd(X, 0, X).

gcd(X, Y, Z) :-
    R is mod(X, Y),
    gcd(Y, R, Z).


