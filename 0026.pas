Program
  P;
Var
  x1, y1, r1, x2, y2, r2: Integer;
  d: Real;
Begin
  Readln(x1, y1, r1);
  Readln(x2, y2, r2);
  d := sqrt(sqr(abs(x1 - x2)) + sqr(abs(y1 - y2)));
  If
    (r1 + r2 >= d)  and
    (abs(r1 - r2) <= d)
  then
    writeln('YES')
  else
    writeln('NO')
end.