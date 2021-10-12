program p;

var S, T: byte;

begin
    readln(S, T);
    if T > S then
      write(T-S)
    else
      write(12-S+T);
end.