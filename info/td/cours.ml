
let maximum (v:int vect) =
    let m = ref v.(0) in
    for i = 1 to (vect_length v) - 1 do
        if v.(i) > !m then
            m := v.(i)
    done;
    !m;;

let rec fact n = match n with
    | 0 -> 1
    | _ -> n * fact (n-1);;
trace "fact";;
fact 4;;

let rec fact2 n t = match n with
    | 0 -> t
    | _ -> fact2 (n-1) (t*n);;
trace "fact2";;
fact2 4 1;;

let rec A m n = match m,n with
    | 0,_ -> n+1
    | _,0 -> A (m-1) 1
    | _,_ -> A (m-1) (A m (n-1));;
A 3 4;;

let rec pair n = match n with
    | 0 -> true
    | _ -> impair (n-1)
and impair n = match n with
    | 0 -> false
    | _ -> pair (n-1);;
pair 8;;
pair 5;;

let rec fibo_couple n = match n with
    | 0 -> (0,1)
    | _ -> let (u,v) = fibo_couple (n-1) in (v, u+v);;
let fibo2 n = fst (fibo_couple n);;
fibo2 20;;

