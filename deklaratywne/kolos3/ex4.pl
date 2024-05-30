member(X, [X|_]).
member(X, [_|T]) :-
    member(X, T).


split(_, [], [], []).
split(V, [H|T], [H|R1], R2) :-
    H =< V,
    split(V, T, R1, R2).

split(V, [H|T], R1, [H|R2]) :-
    H > V,
    split(V, T, R1, R2).

append([], X, X).
append([H|T], L, [H|R]) :- append(T, L, R).
