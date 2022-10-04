Program
  P;
Var
  x1, y1, x2, y2: Byte;
Begin
  Readln(x1, y1, x2, y2);
  If
    (x1 + y1) mod 2 = (x2 + y2) mod 2
  then
    writeln('YES')
  else
    writeln('NO');
end.