#lang racket

(define (square-list l)
    (
        map (lambda (x) (* x x)) l
    )
)
(square-list '(1 2 3))

(define (mapf f l)
    (
        map (lambda (x) (f x)) l
    )
)

(mapf (lambda (x) (+ 1 x)) '(4 5 6))
