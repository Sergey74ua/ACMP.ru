program p;
var A, B : integer;
begin
	read(A, B);
    if A = B then write('=')
    else if A > B then write('>')
    else write('<');
end.