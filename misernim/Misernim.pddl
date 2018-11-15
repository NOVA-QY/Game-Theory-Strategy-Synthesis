(define (domain Misernim)
    (:objects ?stone-num - int)
    (:type miser)
    (:tercondition (= ?stone-num 1))
    (:action take 
        :parameters (?x)
        :precondition (and (>= ?stone-num ?x) (or (= ?x 1) (= ?x 2) (= ?x 3)))
        :effect (decrease ?stone-num ?x))
)
