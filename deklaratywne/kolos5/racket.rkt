#lang racket

(define (member x l)
    (if (null? l)
    #f
    (if (eq? (car l) x)
        #t
        (member x (cdr l))
    )
    )
)

(member 3 '(1 2 3))

; (define (delete x l)
;     (if (null? l)
;     '()
;         (if (eq? (car l) x)
;         (delete x (cdr l))
;         (cons (car l) (delete x (cdr l)))
;         )
;     )
; )



(define (fold f e l)
    (if (null? l) e (f (car l) (fold f e (cdr l))))
)

(define (delete x l)
    (fold (lambda (el a)
        (if (eq? el x)
        a
        (cons el a)
        )
    ) '() l)
)


(delete 4 '(1 2 3 4 4 5 4))

(define (twice l)
    (if (null? l)
    '()
    (cons (car l) (cons (car l) (twice (cdr l))))
    )
)

(twice '(1 2 3))

(define (sum f r)
    (if (eq? r 0)
    (f r)
    (+ (f r) (sum f (- r 1)))
    )
)

(sum (lambda (x) (+ x 2)) 3)


(define (split x l)
    (if (null? l)
    '(() ())
    (if (> (car l) x)
        (cons (car (split x (cdr l))) (cons (car l) (car (cdr (split x (cdr l))))))
        (if (< (car l) x)
            (cons (cons (car l) (car (split x (cdr l)))) (car (cdr (split x (cdr l)))))
            (split x (cdr l))
        )
    )
    )
)

; (split 5 '(1 2 3 4 5 6 7 8 9))


(define (rev l)
    (revh l '())
)

(define (revh l a)
    (if (null? l)
        a
        (revh (cdr l) (cons (car l) a))
    )
)

(rev '(1 2 3 4))

(define (square-list l)
    (if (null? l)
        '()
        (cons (* (car l) (car l)) (square-list (cdr l)))
    )
)

(square-list '(1 2 3 4))
