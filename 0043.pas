Program
    P;
Var
    N, M: integer = 0;
    S: string;
Begin
    Readln(S);
    For var i := 1 to N do
    begin
        Readln(S);
        If
            length(S)=6
        then
            writeln('Yes')
        else
            writeln('No');
    end;
end.

s=input()
n=m=0
for i in s:
  if i=='0':
    n+=1
    m=max(m, n)
  else:
    n=0
print(m)