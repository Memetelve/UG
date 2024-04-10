#lang racket

(define (sqrt x) (* x x))

(define (less x y) (x < y))
(define (equals x y) (and (not (< x y)) (not (< y x))))
(define (lte x y) (not (< y x)))
(define (gte x y) (or (< x y) (equals x y)))
(define (not_equals x y) (not (equals x y)))

(define (nwd x y)
    (if (> y 0)
        (nwd y (modulo x y))
        x
    )
)

(define (mod n d)
    (if (> n 0)
        (mod (- n d) d)
        (+ n d)
    )
)

;;; (modulo 201 11)
;;; (mod 201 11)

(define (nww x y)
    (/ (* x y) (nwd x y))
)

(define (same_values p1 p2 x y)
    (eq? (p1 x y) (p2 x y))
)

;;; (same_values + * 2 2)
;;; (same_values + * 3 3)
;;; (same_values > < 3 3)

(define (even x) 
    (if (zero? x)
        #t
        (odd (- x 1)
    )
))

(define (odd x) 
    (if (zero? x)
        #f
        (even (- x 1))
    )
)

;;; (even 11)
;;; (even 12)

(define (factorial x)
    (if (= (- x 1) 0)
        x
        (* x (factorial (- x 1)))
))

;;; (factorial 5)

(define (fib x)
    (cond   ((= x 0) 0)
            ((= x 1) 1)
            ((> x 1) ((fib (- x 1))))

    )
)


