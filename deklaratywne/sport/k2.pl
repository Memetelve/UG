
twice([], []).
twice([H|T], [H, H|T2]) :-
    twice(T, T2).


postorder(nil, []).
postorder(t(X, L, B), R) :-
    postorder(L, R1),
    postorder(B, R2),
    append(R1, R2, Temp),
    append(Temp, [X], R).
