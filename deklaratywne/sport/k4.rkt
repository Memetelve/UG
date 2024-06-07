#lang racket

(define (del x l)
    (cond
        [(null? l) l]
        [(eq? (car l) x) (cdr l)]
        [else (cons (car l) (del x (cdr l)))]
    )
)

(del 3 '(1 2 3 4 3 2 1))

(define (count x l)
    (cond
        [(null? l) 0]
        [(eq? (car l) x) (+ 1 (count x (cdr l)))]
        [else (count x (cdr l))]
    )
)

(count 2 '(1 2 3 5 2 4 2))


(define (filter p l)
    (cond
        [(null? l) l]
        [(p (car l)) (cons (car l) (filter p (cdr l)))]
        [else (filter p (cdr l))]
    )
)

(filter even? '(1 2 3 4 5 6 7 8 9))


(define (inorder x)
    (cond
        [(null? x) '()]
        [else
            (append (inorder (cadr x)) (list (car x)) (inorder (caddr x)))
        ]
    )
)

(inorder '(4
    (3 () ())
    (2 (9 () ()) (7 () ()))
    ))
