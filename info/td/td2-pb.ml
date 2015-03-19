
(* Question 1 *)
let rec union a b = match a with
    | []   -> b
    | h::t -> if mem h b then union t b
              else union t (h :: b);;
union [0; 4; 5] [5; 6; 7];;

let difference a b =
    let rec mdiff a b l = match a with
        | [] -> l
        | h::t -> if mem h b then mdiff t b l
                  else mdiff t b (h::l)
    in mdiff a b [];;
difference [0; 4; 5] [5; 6; 7];;

let intersection a b =
    let rec mint a b l = match a with
        | [] -> l
        | h::t -> if mem h b then mint t b (h::l)
                  else mint t b l
    in mint a b [];;
intersection [0; 4; 5] [5; 6; 7];;

