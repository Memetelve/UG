member2(X, L) :- member2(X, L, 0).
member2(_, _, 2).
member2(X, [X|T], C) :-
    C1 is C + 1,
    member2(X, T, C1).

member2(X, [_|T], C) :- member2(X, T, C).

down(-1, []).
down(N, [N|T]) :-
    N1 is N - 1,
    down(N1, T).
