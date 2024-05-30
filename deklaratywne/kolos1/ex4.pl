
shift([H1|T1], L2) :- shift(H1, T1, L2).
shift(H, [], [H]).
shift(H, [H1|T1], [H1|R]) :-
    shift(H, T1, R).



fac(N, L) :-
    fac(N, 0, L).

fac(0, L, [1]).
fac(N, Acc, [R|L]) :-
    factorial(N, X),
    R is X,
    N1 is N - 1,
    fac(N1, Acc, L).

factorial(0, 1).
factorial(N, R) :-
    N1 is N - 1,
    factorial(N1, R1),
    R is N * R1.
