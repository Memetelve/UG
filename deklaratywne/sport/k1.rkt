#lang racket

; (define (length l)
;     (if (null? l)
;         0
;         (+ 1 (length (cdr l)))
;     )
; )

(define (length l)
    (foldl (lambda (x y) (+ y 1)) 0 l)
)

(length '(1 2 3 4 5 6))


; (define (reverse l)
;     (foldl (lambda (x y) (
;         append (list x) y
;         )) '() l)
; )

(define (reverse l)
    (if (null? l) '()
        (append (reverse (cdr l)) (list (car l)))
    )
)

(reverse '(1 2 3 4))


(define (divisors x)
    (divh x x)
)

(define (divh x n)
    (if (eq? n 1) '(1)
        (if (eq? (modulo x n) 0)
            (cons n (divh x (- n 1)))
            (divh x (- n 1))
        )
    )
)

(divisors 9)

(define (takewhile p l)
    (if (null? l) '()
        (if (p (car l))
            (cons (car l) (takewhile p (cdr l)))
            '()
        )
    )
)

(takewhile even? '(2 4 6 8 9 10 12))

