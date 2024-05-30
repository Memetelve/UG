eliminate(X, [], []).
eliminate(X, [X,X|T], R) :- eliminate(X, T, R).
eliminate(X, [H|T], [H|R]) :- eliminate(X, T, R).


f(X, 0) :- X < 3.
f(X, 2) :- 3 =< X, X < 6.
f(X, 4) :- 6 =< X.


p(1).
p(2) :- !.
p(3).
