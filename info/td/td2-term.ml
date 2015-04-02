
(* Exercice 1 *)
let lth l =
    let rec mlth l ln = match l with
    | []   -> ln
    | _::t -> mlth t (ln + 1)
    in mlth l 0;;
lth [3; 5; 6; 6];;

(* Exercice 2 *)
let horner p x =
    let rec rhorner p x acc = match p with
    | []   -> acc
    | a::q -> rhorner q x (a + x*acc)
    in rhorner (rev p) x 0;;
horner [1; 2; 3; 0] 3;;

(* Exercice 3 *)
let applique f l =
    let rec rapp f l acc = match l with
    | []   -> acc
    | h::t -> rapp f t ((f h) :: acc)
    in rev (rapp f l []);;
let func x = x*x;;
applique func [1;2;3;4;5];;

(* Exercice 4 *)
let rec pgcd a b = match b with
    | 0 -> a
    | _ -> pgcd b (a mod b);;
pgcd 12 27;;

let bezout a b =
    let rec mbezout (a,b) (x1,y1) (x2,y2) = match b with
        | 0 -> (x1,y1)
        | _ -> let (q,r) = (a/b,a mod b) in mbezout (b,r) (x2,y2) (x1-q*x2, y1-q*y2)
    in mbezout (a,b) (1,0) (0,1);;
bezout 144 13;;

(* Exercice 5 *)
let mccarthy1 n = match n with
| _ when n > 100 -> n - 10
| _ -> 91;;
mccarthy1 3;;

let mccarthy n =
    let rec rmc n c = match (n,c) with
    | (_,0) -> n
    | _ when n > 100 -> rmc (n - 10) (c - 1)
    | _ -> rmc (n + 11) (c + 1)
    in rmc n 1;;
mccarthy (-359);;

