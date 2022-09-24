Program
    p;
Const
    C: string = 'ABCEHKMOPTXY';
    D: string = '0123456789';
Var
    N: integer;
    S: string;
Begin
    Readln(N);
    For var i := 1 to N do
    begin
        Readln(S);
        If
            (length(S)=6) and
            (copy(S, 1, 1) in C) and
            (copy(S, 2, 1) in D) and
            (copy(S, 3, 1) in D) and
            (copy(S, 4, 1) in D) and
            (copy(S, 5, 1) in C) and
            (copy(S, 6, 1) in C)
        then
            writeln('Yes')
        else
            writeln('No');
    end;
end.