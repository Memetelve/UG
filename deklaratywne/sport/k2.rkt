#lang racket

(define (append l m)
    (if (null? l) m
        (cons (car l) (append (cdr l) m))
    )
)

(append '(1 2 3) '(4 5 6))

(define (nth n x l)
    (if (null? l) '()
        (if (eq? n 1)
        (cons x (cdr l))
        (cons (car l) (nth (- n 1) x (cdr l)))
        )
    )
)

(nth 5 'z '(a b c))

; (define (exists p l)
;     (foldl (lambda (x y) (
;         if (p x)
;         #t
;         y
;     )) #f l)
; )

(define (exists p l)
    (if (null? l) #f
        (if (p (car l))
        #t
        (exists p (cdr l))
        )
    )
)

(exists even? '(1 3 5 8 7))

(define (sum g a)
    (if (eq? a 0)
    (g a)
    (+ (g a) (sum g (- a 1)))
    )
)

(sum (lambda (x) (* x x)) 4)
