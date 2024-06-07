#lang racket

(define (append l m)
    (if (null? l)
    m
    (cons (car l) (append (cdr l ) m))
    )
)

(append '(1 2 3) '(1 2 3))

(define (delete x l)
    (foldr (lambda (a b) (
        if (eq? a x)
        b
        (cons a b)
    )) '() l)
)

(delete 'a '(a b c a))


(define (exchange x y l)
    (if (null? l)
    '()
    (if (eq? x (car l))
    (cons y (exchange x y (cdr l)))
    (cons (car l) (exchange x y (cdr l)))
    )
    )
)

(exchange 1 7 '(4 1 5 10 1))

(define (drop-while p l)
    (if (null? l)
    '()
    (if (p (car l))
    (drop-while p (cdr l))
    l
    )
    )
)

(drop-while even? '(2 4 6 7 8 10))
