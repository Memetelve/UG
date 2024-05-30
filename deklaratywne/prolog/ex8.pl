% F)

rev(R1, R2) :- rev(R1, R2, []).
rev([], R, R).
rev([H|T], R, Acc) :- rev(T, R, [H|Acc]).


shift([H|T], R) :- shift(T, H, R).
shift([], H, [H]).
shift([H|T], A, [H|R]) :-
    shift(T, A, R).


% G)

quadrat([], []).
quadrat([H1|T1], [H2|T2]) :-
    H2 is H1 * H1,
    quadrat(T1, T2).

% H)

combine([H1|[]], [H2|[]], [[H1, H2]]).
combine([H1|T1], [H2|T2], [[H1, H2]|R]) :-
    combine(T1, T2, R).

% I)

palindrome(L) :-
  rev(L, R),
  L = R.



% J)

p(X, L, Y, Z) :-
  append(_, [Y, X, Z|_], L).



