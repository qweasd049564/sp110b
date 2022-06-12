# do while
## 程式碼
```
void DOWHILE() {
  int dowhileBegin = nextLabel(); //L0
  int dowhileEnd = nextLabel(); //L1
  emit("(L%d)\n", dowhileBegin);
  skip("do");
  skip("while");
  skip("(");
  int e = E();
  emit("if not T%d goto L%d\n", e, dowhileEnd);
  skip(")");
  skip(";");
  emit("goto L%d\n", dowhileBegin);
  emit("(L%d)\n", dowhileEnd);
}
```
## test
```
s=0;
i=1;
do {
  s = s + i;
  i = i + 123;
} while (i <= 555);
```
## 執行結果
```
s=0;
i=1;
do {
  s = s + i;
  i = i + 123;
} while (i <= 555);
========== lex ==============
token=s
token==
token=0
token=;
token=i
token==
token=1
token=;
token=do
token={
token=s
token==
token=s
token=+
token=i
token=;
token=i
token==
token=i
token=+
token=123
token=;
token=}
token=while
token=(
token=i
token=<
token==
token=555
token=)
token=;
========== dump ==============
0:s
1:=
2:0
3:;
4:i
5:=
6:1
7:;
8:do
9:{
10:s
11:=
12:s
13:+
14:i
15:;
16:i
17:=
18:i
19:+
20:123
21:;
22:}
23:while
24:(
25:i
26:<
27:=
28:555
29:)
30:;
============ parse =============
t0 = 0
s = t0
t1 = 1
i = t1
(L0)
t2 = s
t3 = i
t4 = t2 + t3
s = t4
t5 = i
t6 = 123
t7 = t5 + t6
i = t7
t8 = i
t9 = 555
t10 = t8 < t9
if not T10 goto L1
goto L0
(L1)
```

