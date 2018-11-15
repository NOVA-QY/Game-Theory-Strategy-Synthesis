(define (domain Chomp-Game)
    (:objects ?m ?n)
    (:type normal)
    (:tercondition (and (= ?m 1) (= ?n 1)))
    (:action eat 
        :parameters (?x ?y)
        :precondition (and (<= ?x ?m) (<= ?y ?n))
        :effect (and (decrease ?m ?x) (decrease ?n ?y)))
)