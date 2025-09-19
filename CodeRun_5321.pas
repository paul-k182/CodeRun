// 5321. Наряжаем ёлку
// https://coderun.yandex.ru/problem/decorating-tree

program Main;

uses
  SysUtils;

var
  k, i: shortint;
  b: longint;

begin
	ReadLn(k);
	b := 1;
	for i := 2 to k do
		b := (b shl 1) or 1;
	WriteLn(b);
end.