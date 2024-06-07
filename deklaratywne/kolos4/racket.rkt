#lang racket

(define (delete x l)
    (if (null? l)
    '()
    (if (eq? (car l) x)
        (cdr l)
        (cons (car l) (delete x (cdr l)))
    )
    )
)

(delete 1 '(2 3 4 1 33 1))
