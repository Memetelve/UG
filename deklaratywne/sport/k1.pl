
shift([H|T], L2) :- shift(T, H, L2).
shift([], H, [H]).
shift([H1|T], H, [H1|L2]) :-
    shift(T, H, L2).

sil(0, [1]).
sil(N, [H, H1|T]) :-
    N1 is N - 1,
    sil(N1, [H1|T]),
    H is N * H1.


ord([_]).
ord([H, H2|T]) :-
    H =< H2,
    ord([H2|T]).
% N znak lista
nth(1, X, [X|_]).
nth(N, X, [H|T]) :-
    N1 is N - 1,
    nth(N1, X, T).


pal(L, L).
pal([_|L], L).
pal(L) :- pal(L, []).
pal([H|T], R) :- pal(T, [H|R]).


com([], [], []).
com([H1|T1], [H2|T2], [[H1, H2]|R]) :-
    com(T1, T2, R).

qua([],[]).
qua([H|T], [Q|R]) :-
    Q is H * H,
    qua(T, R).


