program p;
var N : integer;
begin
  read(N);
  if N > 10000 then exit;
  if N > 0 then
  	write((N + 1) * (N / 2))
  else
  	write(-((abs(N) + 1) * (abs(N) / 2)-1))
end.