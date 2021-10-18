program p;

var N, S, i: integer;

begin
    readln(N);
    
    S := 1;
    for i := 1 to N do
      S := S + i;
    
    write(S);
end.