#lang racket

(define (product term next a b)
    (
        if (> a b)
        1.0
        (* (term a) (product term next (next a) b))
    )
)

;;; factorial
(product (lambda (x) x) (lambda (x) (+ x 1)) 1 5)

;;; pi aproximation
;;; (* (product (lambda (x) (/ (if (= (modulo x 2) 1) (- x 1) x) (if (= (modulo x 2) 0) (- x 1) x))) (lambda (x) (+ x 1)) 3 20000000) 4)


(define (accumlate combiner null-value term next a b)
    (
        if (> a b)
        null-value
        (combiner (term a) (accumlate combiner null-value term next (next a) b))
    )
)

(accumlate * 1.0 (lambda (x) x) (lambda (x) (+ x 1)) 1 5)

(define (filter-accumlate pred combiner null-value term next a b)
    (
        if (> a b)
        null-value
        (if (pred a)
        (combiner (term a) (filter-accumlate pred combiner null-value term next (next a) b))
        (combiner null-value (filter-accumlate pred combiner null-value term next (next a) b))
        )
    )
)

;;; function that checks if number is prime
(define (prime? n)
    (
        define (iter x)
            (
                if (> (* x x) n)
                #t
                (if (= (modulo n x) 0)
                #f
                (iter (+ x 1))
                )
            )
    )
    (iter 2)
)

(define (gcd a b)
    (
        if (> b 0)
        (gcd b (modulo a b))
        a
    )
)

;;; sum of squares of prime numbers in [a, b]
(filter-accumlate prime? + 0.0 (lambda (x) (* x x)) (lambda (x) (+ x 1)) 1 5)

;;; product of the natural numbers i smaller than n for which gcd(i,n) = 1
(filter-accumlate (lambda (x) (if (and (< x 10) (= (gcd x 10) 1)) #t #f)) * 1.0 (lambda (x) x) (lambda (x) (+ x 1)) 1 9)


(define (f g) (g 2))

;(f (lambda (x) (* x x)))
;(f (lambda (z) (+ z (* 3 z))))
;(f f)


(define (comb f g)
    (lambda (x) (f (g x))))

(define (square n) (* n n))

(define (double n) (+ n n))

;((comb square double) 5)

(define (samesign? a b)
    (
        if (> (* a b) 0)
        #t
        #f
    )
)

(define (root f a b m)
        (
            if (= m 100)
            (/ (+ a b) 2.0)
            (if (samesign? (f a) (f (/ (+ a b) 2)))
            (root f (/ (+ a b) 2) b (+ m 1))
            (root f a (/ (+ a b) 2) (+ m 1)))
        )
)

(define (twoja x) 
    (
        + (* x x x) (* 3 x) 3
    )
)

(root twoja -2 5 0)




