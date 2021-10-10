Program p;
var A : int64;
begin
    read(A);
    if ((A mod 10) <> 5) or (A >= 400000) then exit;
    write(A * A);
end.