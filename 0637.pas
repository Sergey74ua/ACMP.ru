Program
  P;
Var
  n, k, s, i: Int64;
  arr: array of Word;
Begin
  Readln(n);
  SetLength(arr, n);
  For i := 0 to n-1 do
    read(arr[i]);
  Readln(k);
  s := 0;
  For i := 0 to n-1 do
    s := s + Min(arr[i], k);
  Writeln(s);
end.