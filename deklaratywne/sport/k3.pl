
member(X, [X|_]).
member(X, [_|T]) :-
    member(X, T).


split(_, [], [], []).

split(X, [H|L], [H|L1], L2) :-
    H < X,
    split(X, L, L1, L2).

split(X, [H|L], L1, [H|L2]) :-
    H > X,
    split(X, L, L1, L2).

split(X, [_|L], L1, L2) :-
    split(X, L, L1, L2).


odd([_,_]).
odd([_,_|T]) :- odd(T).
