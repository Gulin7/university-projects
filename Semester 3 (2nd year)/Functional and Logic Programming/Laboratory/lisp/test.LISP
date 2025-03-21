; double the numerical values in a list at any level 
; test:  
; > (double '(1 2 a (3 4) b c))  
; (2 4 A (6 8) B C) 
(defun doubleNumbers(l) 
   (cond
    ((null l) nil) ; daca lista e goala, nil
    ((numberp (car l)) ( cons (* (car l) 2) ( doubleNumbers(cdr l))) ) ;car=number, double it and give it to the next person
    ((listp (car l)) (cons (doubleNumbers(car l)) (doubleNumbers(cdr l)))) ;car=list, then call the function for it and for the tail
    (t (cons (car l) (doubleNumbers(cdr l)))) )) ;if neither list nor number, just append the head and call for the tail
;--------------------------------------------------------------------------
; given a list of length n of sublists representing work items and a list of length n of functions representing workers 
;obtain the list of results of performing the work by each worker on their corresponding work item 
; test: 
; > (work '(+ * -) '((2 3) (1 2) (7 5 1))) 
; (5 2 1) 
(defun work(list items)
  (mapcar #'apply list items))
;mapcar to apply the lambda function for each pair of list / items elements (1st w 1sts, 2nd w 2nd etc.)
;so for each operation in list it takes the first sublist in items
;lambda with the 2 parameters calls the execution of apply 
;apply applies the function operation to all elements in the list item
;-----------------------------

