
(* Exercice 1 *)
let rec puissance x n = match n with
    | 0 -> 1
    | _ -> if n mod 2 == 0 then puissance (x*x) (n/2)
                           else x*puissance (x*x) (n/2);;
puissance 4 5;;

(* Exercice 2 *)
let rec horner p x = match list_length p with
    | 0 -> 0
    | _ -> (hd p) + x * horner (tl p) x;;
let lst = [1; 1; 1];;
horner lst 1;;

(* Exercice 4 *)
let rec mccarthy n = match n with
    | _ when n > 100 -> n - 10
    | _              -> mccarthy (mccarthy (n + 11));;
mccarthy 90;;
mccarthy 91;;
mccarthy 92;;
mccarthy 93;;
mccarthy 94;;
mccarthy 95;;
mccarthy 96;;
mccarthy 97;;
mccarthy 98;;
mccarthy 99;;
mccarthy 100;;
mccarthy 102;;

(* Exercice 5 *)
let rec appartient e l = match list_length l with
    | 0 -> false
    | _ -> if hd l == e then true else appartient e (tl l);;
appartient 3 [1; 5; 3; 5; 4];;

(* Exercice 6 *)
let rec concatene l1 l2 = match list_length l1 with
    | 0 -> l2
    | _ -> (hd l1) :: concatene (tl l1) l2;;
concatene [1; 3; 4] [5; 6; 2];;

let rec concatene_envers l1 l2 = match list_length l1 with
    | 0 -> l2
    | _ -> concatene_envers (tl l1) ((hd l1)::l2);;
concatene_envers [1; 2; 3; 4] [5; 6; 7];;

let retourne l = concatene_envers l [];;
retourne [1; 2; 3; 4; 5; 6; 7];;

(* Exercice 7 *)
let rec applique f l = match list_length l with
    | 0 -> []
    | _ -> (f (hd l)) :: applique f (tl l);;
applique (prefix + 5) [1;2;3;4;5];;

(* Exercice 8 *)
let rec element n l = match (n,l) with
    | (_,[])   -> failwith "liste trop courte"
    | (0,h::_) -> h
    | (_,_::t) -> element (n-1) t;;
element 3 [0;1;2;3;4;5];;

let rec insere_pos e n l = match (n,l) with
    | (_,[])   -> failwith "liste trop courte"
    | (0,_)    -> e :: l
    | (_,h::t) -> h :: insere_pos e (n-1) t;;
insere_pos 3 3 [0;1;2;4;5];;

let rec supprime n l = match (n,l) with
    | (_,[]) -> failwith "liste trop courte"
    | (0,_::t) -> t
    | (_,h::t) -> h :: supprime (n-1) t;;
supprime 3 [0;1;2;3;4;5];;
supprime 10 [0];;

(* Exercice 9 *)
let divise l =
    let rec subdiv p n = match (p,n) with
        | (_,0)       -> p
        | ((_,[]),_)  -> p
        | ((l1,h::t),_) -> subdiv (h::l1,t) (n-1);
    in subdiv ([],l) (list_length l / 2);;
divise [1;2;3;4;5;6;7;8;9];;

let rec fusion l1 l2 = match (l1,l2) with
    | ([],_)          -> l2
    | (_,[])          -> l1
    | (h1::t1,h2::t2) -> if h1 > h2 then h2 :: fusion l1 t2
                                    else h1 :: fusion t1 l2;;
fusion [1;3;6;7] [4;5;7;8];;

let rec trifusion l = match l with
    | []       -> []
    | h::[]    -> [h]
    | a::b::[] -> if a > b then [b;a] else [a;b]
    | l        -> let (l1,l2) = divise l in fusion (trifusion l1) (trifusion l2);;
trifusion [3; 5; 1; 6; 7; 9; 2; 5];;

(* Exercice 10 *)
let rec pgcd a b = match b with
    | 0 -> a
    | _ -> pgcd b (a mod b);;
pgcd 12 27;;

let rec pgcdn a b n = match b with
    | 0 -> (a,n)
    | _ -> pgcdn b (a mod b) (n + 1);;
pgcdn 12 27 0;;

let rec bezout a b = match b with
    | 0 -> (1,0)
    | _ -> 5;;

