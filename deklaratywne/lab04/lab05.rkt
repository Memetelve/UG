#lang racket

;;; lab17

(define (myappend l m)
    (
        if (null? l)
        m
        (cons (car l) (append (cdr l) m))
    )
)

(define (mylast l) 
    (
        if (= (length l) 1)
        (car l)
        (mylast (cdr l))
    )
)

;;; (mylast '(1 45 754 542 4))

(define (rev-helper l m)
    (
        if (null? l)
        m
        (rev-helper (cdr l) (cons (car l) m))
    )
)

(define (reverse l)
    (
        rev-helper l '()
    )
)

;;; (reverse '(1 2 3 4))

(define (del-helper l x new)
    (
        if (null? l)
        new
        (
            if (= (car l) x)
            (del-helper (cdr l) x new)
            (del-helper (cdr l) x (cons (car l) new))
        )
    )
)


(define (mydelete l x)
    (
        reverse (del-helper l x '())
    )
)

(mydelete '(1 2 3 4) 4)


(define (pairing x y)
    (
        if (= (length x) 1)
        (list (cons (car x) (car y)))
        (cons (cons (car x) (car y)) (pairing (cdr x) (cdr y)))
    )
)

(pairing '(1 2 3) '(4 5 6))


;;; (define (splits l x)
;;;     (
;;;         if (= (length l) 1)

;;;     )
;;; )


(define (name x y z)
    (
        values x y z
    )
)

(name 1 1 1)
