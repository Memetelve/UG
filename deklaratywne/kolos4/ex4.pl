
member2(X, L) :- member2(X, L, 0).
member2(_, _, 2).
member2(X, [X|L], V) :-
    V1 is V+1,
    member2(X, L, V1).

member2(X, [H|L], V) :- member2(X, L, V).



down(-1, []).
down(N, [N|A]) :-
    N1 is N - 1,
    down(N1, A).
