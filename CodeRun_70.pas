// 70. Ближайшее число
// https://coderun.yandex.ru/problem/nearest-number

program Main;

uses
  SysUtils;

var
  n, x, i, m: integer;
  r, v: real;
  ms: array[1..1000] of integer;

begin
	ReadLn(n);
   for i := 1 to n do
		Read(ms[i]);
	ReadLn(x);
	m := ms[1];
	r := Abs(x - m);
   for i := 2 to n do
		begin
			v := Abs(x-ms[i]);
			if v < r then
				begin
					r := v;
					m := ms[i];
				end;
		end;
	WriteLn(m);
end.