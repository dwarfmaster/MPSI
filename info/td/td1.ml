
(* Exercice 2 *)
let permutation x y =
    let z = ref!x in
    x := !y;
    y := !z;;

let x = ref 5;;
let y = ref 6;;
permutation x y;;
print_string "(x,y) = (5,6) permuted :";;
print_int !x;;
print_int !y;;

(* Exercice 3 *)
let rec puissance x n =
    if n = 0 then
        1
    else
        x * (puissance x (n-1));;
puissance 2 5;;

(* Exercice 4 *)
let egale u v =
    if vect_length u <> vect_length v then
        false
    else let t = ref true in
        for i = 0 to vect_length u - 1 do
            if u.(i) <> v.(i) then
                t := false;
        done;
        !t;;
let u = [|1; 2; 4; 5|];;
let v = [|1; 2; 4; 3|];;
egale u u;;
egale u v;;

let egale2 u v =
    let flag = ref (vect_length u = vect_length v) in
    let i = ref 0 in
    while !i < vect_length u && !flag do
        flag := (u.(!i) = v.(!i))
    done;
    !flag;;
egale u u;;
egale u v;;

(* Exercice 5 *)
let fill u =
    for n = 2 to vect_length u / 2 do
        for i = 1 to vect_length u - 1 do
            if i > n && i mod n = 0 then u.(i) <- not u.(i);
        done;
    done;;

let ouverts u =
    for i = 0 to vect_length u - 1 do
        if not u.(i) then begin
            print_string "Switch off : ";
            print_int i;
            print_string "\n";
            end
    done;;
let sw = make_vect 50 true;;
fill sw;;
ouverts sw;;

(* Exercice 6 *)
let echange t i j =
    let m = ref t.(i) in
    t.(i) <- t.(j);
    t.(j) <- !m;;
echange u 2 3;;
u;;

let miroir t =
    for i = 0 to vect_length t / 2 - 1 do
        echange t i (vect_length t - i - 1)
    done;;
miroir u;;
u;;

let miroir2 t =
    let echng i j =
        let m = ref t.(i) in
        t.(i) <- t.(j);
        t.(j) <- !m;
    in for i = 0 to vect_length t / 2 - 1 do
        echng i (vect_length t - i - 1)
    done;;
miroir u;;
u;;

(* Exercice 7 *)
let babylone a e =
    let abs n = if n > 0. then n else (-1.) *. n in (* abs_float existe aussi *)
    let u = ref a in
    while abs (!u *. !u -. a) > e do
        u := !u/.2. +. a/.(2. *. !u)
    done;
    !u;;
babylone 2. 0.000001;;

(* Exercice 8 *)
let rec pgcd a b =
    if b = 0 then a else
        pgcd b (a mod b);;
pgcd 21 9;;

(* Exercice 9 *)
(* TODO *)
let drapeau_hollandais a =
    let m1 = ref 0 and m2 = ref (vect_length a - 1) in
    while a.(!m1) = -1 do
        m1 := !m1 + 1;
    done;
    while a.(!m2) = 1 do
        m2 := !m2 - 1;
    done;
    for i = 0 to vect_length a - 1 do
        if v.(i) = -1 then begin
            echange a i !m1;
            m1 := !m1 + 1;
        end
        else if v.(i) = 1 then begin
            echange a i !m2;
            m2 := !m2 - 1;
        end;
    done;;
let holl = [| 0, 1, 1, 0, 0, -1, -1, 0, 1, 0 |];;
drapeau_hollandais holl;;
holl;;

(* Exercice 10 *)
let lower_char c =
    let n = int_of_char c in
    if n >= 65 && n <= 90 then
        char_of_int (n + 32)
    else
        c;;
lower_char `e`;;
lower_char `R`;;

let lower_string s =
    for i = 0 to string_length s - 1 do
        s.[i] <- lower_char s.[i];
    done;
    s;;
lower_string "HELLO WoRlD !";;

let upper_char c =
    let n = int_of_char c in
    if n >= 97 && n <= 122 then
        char_of_int (n - 32)
    else
        c;;

let maj_string s =
    let maj = ref true in
    for i = 0 to string_length s - 1 do
        if !maj then begin
            s.[i] <- upper_char s.[i];
            maj := false
        end;
        if s.[i] == ` ` then maj := true
    done;
    s;;
maj_string "hello world, i'm happy !";;

