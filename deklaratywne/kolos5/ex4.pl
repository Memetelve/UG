
rev(L1, L2) :- rev(L1, L2, []).
rev([], L, L).
rev([H|T], R, L) :-
    rev(T, R, [H|L]).


split(_, [], [], []).
split(X, [H|T], [H|L1], L2) :-
    H > X,
    split(X, T, L1, L2).

split(X, [H|T], L1, [H|L2]) :-
    H < X,
    split(X, T, L1, L2).

split(X, [H|T], L1, L2) :-
    split(X, T, L1, L2).
