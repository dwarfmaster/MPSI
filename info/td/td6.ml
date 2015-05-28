(* vim:set foldmethod=marker: *)

(* {{{ Pile *)
type 'a pile = { mutable contenu : 'a list };;

let creePile () = { contenu = []};;
let estVide p = p.contenu = [];;
let empile x p = p.contenu <- x :: p.contenu ;;
let depile p = match p.contenu with
  | [] -> failwith " pile vide "
  | x :: q -> p.contenu <- q ; x ;;
let sommet p = match p.contenu with
  | [] -> failwith " pile vide "
  | x :: q -> x ;;
(* }}} *)

(* {{{ Exercice 1 *)
type couleur = Bleue | Rouge and assiette = { Teinte : couleur ; Entier : int };;
let sort_assiettes asts =
    let bleues = creePile () and rouges = creePile () in
    while not estVide asts do
        let a = depile asts in
        if a.Teinte == Bleue then empile a bleues
                             else empile a rouges
    done;
    while not estVide bleues do
        empile (depile bleues) asts
    done;
    while not estVide rouges do
        empile (depile rouges) asts
    done;;
let asts = creePile ();;
empile {Teinte = Rouge; Entier = 1} asts;;
empile {Teinte = Bleue; Entier = 2} asts;;
empile {Teinte = Rouge; Entier = 3} asts;;
empile {Teinte = Rouge; Entier = 4} asts;;
asts;;
sort_assiettes asts;;
asts;;
(* }}} *)

(* {{{ Exercice 2 *)
type operateurs = Plus | Moins | Fois;;
type fonctions = Carre | Cube;;
type lexeme = Var of int | Fon of fonctions | Op of operateurs;;
let formule = [Var 2; Var 3; Var 1; Op Moins;
                Op Fois; Fon Carre; Var 7;
                Var 8; Op Moins; Op Plus];;

let traite_fon f pile =
    let x = depile pile in match f with
    | Carre -> empile (x*x) pile
    | Cube  -> empile (x*x*x) pile;;
let traite_op op pile =
    let x = depile pile and y = depile pile in match op with
    | Plus  -> empile (y + x) pile
    | Moins -> empile (y - x) pile
    | Fois  -> empile (y * x) pile;;
let evaluate form =
    let rec calculate pile exp = match exp with
    | [] -> depile pile
    | h::t -> begin match h with
        | Var v -> empile v pile
        | Fon f -> traite_fon f pile
        | Op op -> traite_op op pile;
    end;
        calculate pile t;
    in calculate (creePile()) form;;
evaluate formule;;

(* }}} *)

(* {{{ Exercice 3 *)
type parentheses = Po | Pf;;
let coherent pars =
    let rec test pars n = match pars with
    | [] -> if n == 0 then true else false
    | h::t -> if h == Po then test t (n + 1) else test t (n - 1)
    in test pars 0;;
let pars = [Po; Po; Pf; Po; Po; Pf; Po; Pf; Po; Pf; Pf; Pf];;
coherent pars;;

let coherent_taille pars =
    let rec test pars pile = match pars with
    | [] -> estVide pile
    | h::t -> if h > 0 then if estVide pile then empile h pile
                            else if h <= sommet pile then empile h pile
                                                     else failwith " big paren "
                       else begin let x = depile pile in
                            if x <> (-1 * h) then failwith " unclosed "
                       end;
              test t pile
    in try test pars (creePile()) with 
    | _ -> false;;
let pars2 = [5; 3; 3; -3; 2; 1; -1; -2; 3; 2; -2; -3; -3; -5];;
coherent_taille pars2;;

(* }}} *)

