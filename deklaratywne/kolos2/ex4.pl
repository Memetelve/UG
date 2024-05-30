%
postorder(nil, []).
postorder(ab(Label, Left, Right), R) :-
    postorder(Left, R1),
    postorder(Right, R2),
    append(R1, R2, X),
    append(X, [Label], R).

