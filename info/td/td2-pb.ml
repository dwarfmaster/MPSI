
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

(* Question 2 *)
let rec existe f e = match e with
| []   -> false
| h::t -> if f h then true else existe f t;;

let rec qqsoit f e = match e with
| []   -> true
| h::t -> if not f h then false else qqsoit f t;;

let pred x = x > 10;;
existe pred [1; 4; 16; 3; 10; 55];;
qqsoit pred [1; 4; 16; 3; 10; 55];;

(* Question 3 *)
let filtre f e =
    let rec rflt f e l = match e with
    | [] -> l
    | h::t -> if f h then rflt f t (h::l) else rflt f t l
    in rflt f e [];;
filtre pred [1; 4; 16; 3; 10; 55];;

(* Question 4 *)
let ajoute a l =
    let rec raj a l ls = match l with
    | []   -> ls
    | h::t -> raj a t ((a::h)::ls)
    in raj a l [];;
ajoute 4 [[3; 5]; [6; 1]; [6; 8; 9]];;

let rec parties l = match l with
| []   -> [[]]
| h::t -> let ps = parties t in ps @ ajoute h ps;;
parties [0; 1; 2];;

(* Question 6 *)
let suivant a = match a with
| [1] -> []
| 1::h::t -> (h-1)::t
| h::t -> (h-1)::a;;
suivant [1;2;3];;

(* Question 7 *)
let partiesn n =
    let rec rpts a l = match a with
    | [] -> []::l
    | _  -> let next = suivant a in rpts next (a::l)
    in rpts [n] [];;
partiesn 3;;


