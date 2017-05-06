connect(pc1,r1).
connect(pc5,r6).

connect(r1,r2).
connect(r2,r3).
connect(r3,r4).
connect(r3,r5).
connect(r1,r5).
connect(r5,r6).


path(X,Y):-
	connect(X,Y);connect(Y,X).

path(X,Y):-
	connect(X,Z),path(Z,Y),write(' <- '),write(Z).
