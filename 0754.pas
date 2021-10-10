program p;
var M1, M2, M3 : integer;
begin
    read(M1, M2, M3);
    if (M1<94) or (M2<94) or (M3<94) or (M1>727) or (M2>727) or (M3>727) then
         write('Error')
    else
    begin
      if (M1>M2) and (M1>M3) then write(M1)
      else if (M2>M1) and (M2>M3) then write(M2)
      else if (M3>M1) and (M3>M2) then write(M3)
      else write(M1);
    end;
end.