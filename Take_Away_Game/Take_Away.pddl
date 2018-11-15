(define (domain n-take-away)
    (:objects ?stone-num - int ?pick-num - int)
    (:type normal)
    (:tercondition (= ?stone-num 0))
    (:action take
        :parameters (?x)
        :precondition (and (>= ?stone-num ?x) (>= ?pick-num ?x) (<= 0 ?x))
        :effect (decrease ?stone-num ?x))
)