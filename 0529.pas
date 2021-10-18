program p;

var X1, Y1, X2, Y2, X, Y: integer;
    S: real;
begin
    readln(X1, Y1, X2, Y2);
    X := X2 - X1;
    Y := Y2 - Y1;
    S := sqrt(X * X + Y * Y);
    write(S:0:5);
end.