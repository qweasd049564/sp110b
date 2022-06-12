# c6加上DoWhile

## enum
```
enum { // token : 0-127 直接用該字母表達， 128 以後用代號。
  Num = 128, Fun, Sys, Glo, Loc, Id,
  Char, Else, Enum, If, Int, Return, Sizeof, While, Do,//新增Do
  Assign, Cond, Lor, Lan, Or, Xor, And, Eq, Ne, Lt, Gt, Le, Ge, Shl, Shr, Add, Sub, Mul, Div, Mod, Inc, Dec, Brak
};
```
## compiler
```
int compile(int fd) {
  int i, *t;
  // 編譯器
  p = "char else enum if int return sizeof while do"  // 新增do
      "open read write close printf malloc free memset memcmp exit void main";
  i = Char; while (i <= While) { next(); id[Tk] = i++; } // add keywords to symbol table
  i = OPEN; while (i <= EXIT) { next(); id[Class] = Sys; id[Type] = INT; id[Val] = i++; } // add library to symbol table
  next(); id[Tk] = Char; // handle void type
  next(); idmain = id; // keep track of main

  if (!(lp = p = malloc(poolsz))) { printf("could not malloc(%d) source area\n", poolsz); return -1; }
  if ((i = read(fd, p, poolsz-1)) <= 0) { printf("read() returned %d\n", i); return -1; }
  p[i] = 0; // 設定程式 p 字串結束符號 \0

  return prog();
}
```
## 加上Do
```
else if(tk == Do){    //do語句
    next();
    a = e +1 //While條件符合，再做一次 
    stmt();
    if(tk == While){
      next();
      if(tk == '(') next(); 
      else{
        printf("%d: open paren expexted\n", line);
        exit(-1);
      }
      expr(Assign);  //處理判斷式
      if(tk == ')')next();
      else{
        printf("%d: open paren expexted\n", line);
        exit(-1);
      }
      if(tk == ';') next();
      else{
        printf("%d: open paren expexted\n", line);
        exit(-1);
      }
      *++e = BNZ; //判斷式不等於0
      *++e = (int)a;
    }else{
      printf("%d: synatx error\n",line);// 當語法錯誤，回報error
      exit(-1);
    }
  }
  ```