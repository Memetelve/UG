#lang racket

(define (append l m)
    (foldr (lambda (x a) (cons x a)) m l)
)

(append '(1 2 3) '(4 5 6))

; (define (delete x l)
;     (if (null? l) '()
;         (if (eq? (car l) x)
;             (delete x (cdr l))
;             (cons (car l) (delete x (cdr l)))
;         )
;     )
; )

; (define (delete x l)
;     (foldr (lambda (el a) (if (eq? x el) a (cons el a))) '() l)
; )

(define (delete x l)
    (foldr (lambda (el a) (if (eq? x el) a (append a (list el)))) '() l)
)

(delete 4 '(1 2 3 4 5 4 6 7 4 6))

(define (ex x y l)
    (cond
        [(null? l) l]
        [(eq? (car l) x) (cons y (ex x y (cdr l)))]
        [else (cons (car l) (ex x y (cdr l)))]
    )
)

(ex 1 2 '(1 3 3 4 1 2))

(define (dropw p l)
    (cond
        [(null? l) l]
        [(p (car l)) (dropw p (cdr l))]
        [else l]
    )
)

(dropw even? '(2 4 6 8 9 10))
