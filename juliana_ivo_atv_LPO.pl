/* Seguir essa lógica pra resolução da atividade:
    filho(X, Y) -> X é filho de Y. (Ben é filho de Han Solo)
    tio(X, Y)  -> X é tio de Y. (Luke é tio de Ben)
    avo(X, Y) -> X é avô de Y. (Anakin é avô de Ben)
    descendente(X,Y) -> X é descendente de Y. (Y é descendente de Ben)
    ancestral(X, Y) -> X é ancestral de Y. (Shimi — mãe de Anakin — é ancestral de Ben) */

%Fatos

pai('Han Solo').
filho('Ben').
tio('Luke').
avo('Anakin').
descendente('Y').
ancestral('Shimi').

%Predicados (o mesmo que relações (regras))

pai('Han Solo', 'Ben').

filho(X, Y) :-
    pai(Y, X).

tio('Luke', 'Ben').

avo('Anakin', 'Ben').

descendente(X, Y) :-
    pai(Y, X).
/*o descendente de X(Ben) é Y, então o pai de Y é X(Ben)*/

ancestral('Shimi', 'Ben') :-
    descendente(Y, X).
/*o ancestral de X(Ben) é Y, então o descendente de Y é X(Ben)*/

%Inicializacao
:- initialization(imprime_relacoes).

imprime_relacoes :-
    imprime_filho('Ben'),
    imprime_tio('Ben'),
    imprime_avo('Ben'),
    imprime_descendente('Ben'),
    imprime_ancestral('Ben').

imprime_filho(X) :-
    filho(X, Y),
    write('O filho de '), write(Y),
    write(' e '), write(X), nl, !.

imprime_tio(X) :-
    tio(Y, X),
    write('O tio de '), write(X),
    write(' e '), write(Y), nl, !.

imprime_avo(X) :-
    avo(Y, X),
    write('O avo de '), write(X),
    write(' e '), write(Y), nl, !.

imprime_descendente(X) :-
    descendente(X, Y),
    write(X), write(' e descendente de '),
    write(Y), nl, !.

imprime_ancestral(X) :-
    ancestral(Y, X),
    write(Y), write(' e ancestral de '),
    write(X), nl, !.