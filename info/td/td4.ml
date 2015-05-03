
(* Exercice 1 *)
let a = [|3; 5; 6; 4; 7|];;

let sum a =
    let s = ref 0 in
    for i = 0 to (vect_length a) - 1 do
        s := !s + a.(i)
    done;
    !s;;
sum a;;

let divsum a =
    let rec rdsum a i j = match j - i with
    | 0 -> a.(i)
    | 1 -> a.(i) + a.(j)
    | _ -> let m = (i + j) / 2 in rdsum a i m + rdsum a (m + 1) j
    in rdsum a 0 (vect_length a - 1);;
divsum a;;

(* Exercice 2 *)
(* On sépare le nombre de pièces en 3 paquets, on prend les deux premiers
 * paquets, et on compare leur poids. Si les deux paquets on le même poids,
 * la pièce est dans le troisième. Si les deux paquets n'ont pas le même poids,
 * la pièce est dans le plus lourd. On divise donc par trois le nombre de
 * pièces à tester à chaque itération. Pour 3^p pièces, il faut donc p pesées.
 * Dans le cas général, il faut toujours ceil(log_3(n)) \pm 1 pesées.
 *)

(* Exercice 3 *)
let rec puissance x n = match n with
| 0 -> 1.0
| 1 -> x
| _ -> match n mod 3 with
       | 0 -> puissance (x *. x *. x) (n / 3)
       | 1 -> x *. puissance (x *. x *. x) (n / 3)
       | 2 -> x *. x *. puissance (x *. x *. x) (n / 3);;
puissance 2.0 10;;
(* 3*log_3 n <= C(n) <= 5*log_3 (n+1)
 * Donc C(n) = O(ln n), même classe de complexité que l'exponentiation repide
 * d'ordre 2.
 *)

let puissancer =
    let rec rpow a x n = match n with
    | 0 -> a
    | 1 -> x *. a
    | _ -> match n mod 3 with
           | 0 -> rpow (x *. x *. x) (n / 3) a
           | 1 -> rpow (x *. x *. x) (n / 3) (a *. x)
           | 2 -> rpow (x *. x *. x) (n / 3) (a *. x *. x)
    in rpow 1.0;;
puissancer 2.0 10;;

(* Exercice 4 *)
let racine n =
    let s = ref 0 in
    while (!s * !s) <= n do
        s := !s + 1
    done;
    !s - 1;;
racine 26;;

let racineDiv n =
    let rec rcdv i j = match (j - i) with
    | 0 -> i
    | 1 -> if j * j > n then i else j
    | _ -> let m = (i + j) / 2 in
           let a = m*m in
           if a == n     then m
           else if a > n then rcdv i m
           else               rcdv m j;
    in rcdv 1 (n - 1);;
racineDiv 26;;
(* Complexité en O(log_2 n) *)

(* Exercice 5 *)
let produit_mat a b =
    [| [| a.(0).(0) * b.(0).(0) + a.(0).(1) * b.(1).(0);
          a.(0).(0) * b.(0).(1) + a.(0).(1) * b.(1).(1) |];
       [| a.(1).(0) * b.(0).(0) + a.(1).(1) * b.(1).(0);
          a.(1).(0) * b.(0).(1) + a.(1).(1) * b.(1).(1) |] |];;
let a = [| [| 1; 1 |]; [| 0; 1 |] |];;
let b = [| [| 1; 0 |]; [| 0; 1 |] |];;
produit_mat a b;;

let puiss a n =
    let rec rpuiss a n acc = match n with
    | 0 -> acc
    | 1 -> produit_mat a acc
    | _ -> match n mod 2 with
           | 0 -> rpuiss (produit_mat a a) (n / 2) acc
           | 1 -> rpuiss (produit_mat a a) (n / 2) (produit_mat acc a)
    in rpuiss a n [| [| 1; 0 |]; [| 0; 1 |] |];;
puiss a 5;;

let fibo n =
    let m = puiss [| [| 1; 1 |]; [| 1; 0 |] |] n in m.(0).(1);;
fibo 1;;
fibo 2;;
fibo 3;;
fibo 4;;
fibo 5;;
fibo 6;;

(* 8 produits par produit matriciel. 8 fois la complexité de l'exponantiation
 * rapide classique, d'où le résultat. *)

(* Exercice 6 *)
(* TODO *)

(* Exercice 7 *)
let pivot a b e =
    let v = a.(b) in
    let m = ref b in
    for i = b + 1 to e do
        if a.(i) < v then begin
            let swp = ref a.(i) in
            a.(i) <- a.(!m);
            a.(!m) <- !swp;
            m := !m + 1
        end
    done;
    !m;;
let tri_rapide l =
    let rec quick a b = match b - a with
           | x when x <= 0 -> ()
           | _ -> let m = pivot l a b in
                  if m == a then
                      quick (m+1) b
                  else begin
                      quick a (m-1);
                      quick m b;
                  end
    in quick 0 (vect_length l - 1);;
let a = [| 2; 5; 6; 3; 4; 8; 9; 6; 4; 5; 2; 1; 3; 6; 7; 4 |];;
tri_rapide a;;
a;;

(* Dans le pire des cas, pivot effectue (e - b) échanges. Dans ce cas,
 * m = b - 1. tri_rapide va faire des appels successifs en décroissants de 1 à
 * chaque fois. Si l'on imagine que le pire des cas est atteints à chaque
 * itératio, la complexité est en O(n!).
 *
 * On suppose maintenant que pivot coupe la liste en 2 à chaque fois. Il y a
 * dans ce cas ~n appels à pivot durant l'exécution. En considérant que pivot
 * fait (b-e) comparaisons, on trouve une complexité quadratique (TODO on doit
 * trouver en O(nln(n))).
 *)

(* TODO Version pour les listes *)

