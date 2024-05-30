#lang racket

(define (length l)
  (if (eq? l null) 0 (+ 1 (length (cdr l)))))

(length '(1 2 3 4))

(define (reverse l)
  (foldl cons '() l))

(reverse '(1 2 3 4))

(define (divisors x)
  (div x x))

(define (div x y)
  (if (not (eq? y 0)) (if (= (modulo x y) 0) (cons y (div x (- y 1))) (div x (- y 1))) '()))

(divisors 36)

(define (take-while p l)
  (if (not (eq? l null))
  (if (p (car l))
  (cons (car l) (take-while p (cdr l)))
  '())
  '()
  )
)

(take-while even? '(2 4 6 8 10 12))


(define x 3)
(define (p b)
  (define (pp b)
    (begin
      (+ x b)
      (set! x (* b 3))
    )
    b
  )
  (pp 2)
)

(print x)
(p 2)
(print x)
