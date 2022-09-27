Program
    P;
Var
    a, b, S: Int64;
Begin
  Readln(a, b);
  S := Round(Sqrt(a*b));
  If
    a*b = S*S
  then
    Writeln(S)
  else
    Writeln(0);
end.