#lang racket

(define (member x l)
    (cond
        [(null? l) #f]
        [(eq? (car l) x) #t]
        [else (member x (cdr l))]
    )
)

(member 'x '(a b c d e z))

(define (delete x l)
    (foldl (lambda (item acc) (
        if (eq? item x)
        acc
        (append acc (list item))
    )) '() l)
)

(delete 4 '(1 2 3 4 5 6 4 2))

(define (twice l)
    (cond
        [(null? l) l]
        [else (cons (car l) (cons (car l) (twice (cdr l))))]
    )
)

(twice '(1 2 3 4 5))


(define (sum f r)
    (cond
        [(zero? r) (f r)]
        [else (+ (f r) (sum f (- r 1)))]
    )
)

(sum (lambda (x) (* x x)) 4)
