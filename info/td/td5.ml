(* vim:set foldmethod=marker: *)

(* {{{ Exercice 1 *)
let winr n p =
    let rec awin i j = match (i,j) with
    | (0,_) -> 1.0
    | (_,0) -> 0.0
    | _     -> p *. awin (i-1) j +. (1.0-.p) *. awin i (j-1)
    in awin n n;;
winr 5 0.7;;

let wine n p =
    let m = make_matrix (n+1) (n+1) (-1.0) in
    for i = 0 to n do
        m.(i).(0) <- 0.0;
        m.(0).(i) <- 1.0;
    done;
    let rec get i j =
        if m.(i).(j) < -0.5 then
            m.(i).(j) <- p *. get (i-1) j +. (1.0-.p) *. get i (j-1);
        m.(i).(j);
    in get n n;;
wine 5 0.7;;
wine 100 0.7;;
(* }}} *)

(* {{{ Exercice 2 *)
let nmoves n =
    let m = make_matrix (n+1) (n+1) (-1) in
    for i = 0 to n do
        m.(i).(n) <- 1;
        m.(n).(i) <- 1;
    done;
    let rec get i j =
        if m.(i).(j) < 0 then
            m.(i).(j) <- get i (j+1) + get (i+1) (j+1) + get (i+1) j;
        m.(i).(j);
    in get 0 0;;
nmoves 10;;
(* }}} *)

(* {{{ Exercice 3 *)
let msum a =
    let n = vect_length a - 1 in
    let m = make_matrix (n+1) (n+1) 0 in
    m.(0).(0) <- a.(0).(0);
    for i = 1 to n do
        m.(i).(0) <- a.(i).(0) + m.(i-1).(0);
        m.(i).(i) <- a.(i).(i) + m.(i-1).(i-1);
        for j = 1 to i - 1 do
            m.(i).(j) <- a.(i).(j) + max m.(i-1).(j-1) m.(i-1).(j);
        done;
    done;
    let mx = ref m.(n).(0) in
    for i = 1 to n do
        mx := max !mx m.(n).(i)
    done;
    !mx;;
let a = [| [| 3 |];
           [| 7; 4 |];
           [| 2; 4; 6 |];
           [| 8; 5; 9; 3 |] |];;
msum a;;

let mpath a =
    let n = vect_length a - 1 in
    let m = make_matrix (n+1) (n+1) 0 in
    m.(0).(0) <- a.(0).(0);
    for i = 1 to n do
        m.(i).(0) <- a.(i).(0) + m.(i-1).(0);
        m.(i).(i) <- a.(i).(i) + m.(i-1).(i-1);
        for j = 1 to i - 1 do
            m.(i).(j) <- a.(i).(j) + max m.(i-1).(j-1) m.(i-1).(j);
        done;
    done;
    let mx = ref m.(n).(0) in
    let j = ref 0 in
    for i = 1 to n do
        if m.(n).(i) > !mx then begin
            mx := m.(n).(i);
            j := i;
        end;
    done;
    let path = make_vect (n+1) 0 in
    path.(n) <- a.(n).(!j);
    for i = n downto 1 do
        if !j == i then
            j := !j - 1
        else if !j != 0 && m.(i-1).(!j-1) > m.(i-1).(!j) then
            j := !j - 1;
        path.(i-1) <- a.(i-1).(!j)
    done;
    path;;
mpath a;;
(* }}} *)

(* {{{ Exercice 4 *)
let distance a b =
    let n1 = string_length a - 1 and n2 = string_length b - 1 in
    let m = make_matrix (n1+1) (n2+1) 0 in
    for i = 1 to n1 do
        m.(i).(0) <- i;
    done;
    for j = 1 to n2 do
        m.(0).(j) <- j;
    done;
    for i = 1 to n1 do
        for j = 1 to n2 do
            if a.[i-1] == b.[j-1] then
                m.(i).(j) <- m.(i-1).(j-1)
            else
                m.(i).(j) <- 1 + min m.(i).(j-1) 
                                 (min m.(i-1).(j) m.(i-1).(j-1));
        done;
    done;
    m.(n1).(n2);;
distance "niche" "chien";;

let add_char s c =
    let s2 = make_string 1 c in
    s2 ^ s;;
add_char "Hell" `o`;;

let alignement a b =
    let n1 = string_length a - 1 and n2 = string_length b - 1 in
    let m = make_matrix (n1+1) (n2+1) 0 in
    for i = 1 to n1 do
        m.(i).(0) <- i;
    done;
    for j = 1 to n2 do
        m.(0).(j) <- j;
    done;
    for i = 1 to n1 do
        for j = 1 to n2 do
            if a.[i-1] == b.[j-1] then
                m.(i).(j) <- m.(i-1).(j-1)
            else
                m.(i).(j) <- 1 + min m.(i).(j-1) 
                                 (min m.(i-1).(j) m.(i-1).(j-1))
        done;
    done;
    let s1 = ref "" and s2 = ref "" in
    let i = ref (n1 + 1) and j = ref (n2 + 1) in
    while !i > 0 && !j > 0 do
        if a.[!i-1] == b.[!j-1] then
            begin
                s1 := add_char !s1 a.[!i-1];
                s2 := add_char !s2 a.[!i-1];
                i := !i - 1;
                j := !j - 1
            end
        else
            if m.(!i).(!j) - 1 == m.(!i).(!j-1) then
                begin
                    s1 := add_char !s1 `-`;
                    s2 := add_char !s2 b.[!j-1];
                    j := !j - 1
                end
            else if m.(!i).(!j) - 1 == m.(!i-1).(!j) then
                begin
                    s1 := add_char !s1 a.[!i-1];
                    s2 := add_char !s2 `-`;
                    i := !i - 1
                end
            else
                begin
                    s1 := add_char !s1 a.[!i-1];
                    s2 := add_char !s2 b.[!j-1];
                    i := !i - 1;
                    j := !j - 1
                end;
    done;
    (!s1, !s2);;
alignement "niche" "chien";;

(* }}} *)

