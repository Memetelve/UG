reverse(L, R) :- reverse(L, R, []).
reverse([], R, R).
reverse([H|T], R, A) :-
    reverse(T, R, [H|A]).
