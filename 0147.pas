Program
  P;
Var
  N, L, R, T: Int64;
Begin
  Readln(N);
  L := 0;
  R := 1;
  For var i := 1 to N do
  begin
    T := L;
    L := R;
    R := R+T;
  end;
  Writeln(L);
end.