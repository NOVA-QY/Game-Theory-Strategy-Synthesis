(define (domain subtraction-game)
    (:objects ?k)
    (:type normal)
    (:tercondition (= ?k 0))
    (:action move 
        :parameters (?x)
        :precondition (and (>= ?k ?x) (>= ?x 1) (or (= ?x 1) (= ?x 2) (= ?x 3)))
        :effect (decrease ?k ?x))
)