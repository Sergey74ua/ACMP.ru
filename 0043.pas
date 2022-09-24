Program
    P;
Var
    N, M: integer;
    S: string;
Begin
    N := 0;
    M := 0;
    Readln(S);
    For var i := 1 to length(S) do
    begin
        If
            copy(S, i, 1)='0'
        then
            begin
            N := N+1;
            If N > M then M := N
            end
        else
            N := 0;
    end;
    writeln(M);
end.