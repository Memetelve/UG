#lang racket

(define (append l k)
    (if (eq? l null)
    k
    (cons (car l) (append (cdr l) k))
    )
)

(append '(1 2) '(3 4))


(define (nth n x l)
    (if (not (eq? l '()))
    (if (= n 1)
        (cons x (cdr l))
        (cons (car l) (nth (- n 1) x (cdr l)))
    ) '())
)

(nth 4 'z '(a b c d e))


(define (fold f e l)
    (if (null? l) e (f (car l) (fold f e (cdr l)))))

(define (exists pred l)
    (if (null? (fold (lambda (x y) (
        if (pred x)
        (cons x y)
        y
    )) '() l)) #f #t)
)

(exists even? '(1 3))

(define (square x) (* x x))

(define (sum g a)
    (if (= a 0)
    (g a)
    (+ (g a) (sum g (- a 1)))
    )
)

(sum square 4)
(sum (lambda (x) (+ x 2)) 3)
