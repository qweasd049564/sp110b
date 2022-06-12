# 第一週筆記
* 編譯
```
編譯四步驟:前置處理、編譯、組譯、連結
```

* 基本概念
```
用gcc將程式碼編譯成執行檔
gcc sum.c
系統預設輸出檔案為 a.exe 或 a.out

也可用 -o 參數來指定輸出檔名
gcc sum.c -o sum
此時輸出檔案則是 sum.exe 或 sum.out
```
* gcc指令的含意
```
gcc -c sum.c -o sum
其中-c代表只激活預處理、編譯和彙編，sum.c為檔名
-o為參數，sum為指定檔名

gcc -S sum.c -o fib.s
-S的s必須為大寫，表示只激活預處理和編譯
fib.s表示為組合語言檔
如果fib.s的s為大寫，表示為須做前置處理的組合語言檔
```

* 補充
```
ar是gcc底下壓縮函式庫程式
.o靜態函式庫
.so動態函式庫
皆可壓縮到ar中
```

* Makefile特殊符號
```
$@ : 該規則的目標文件 (Target file)
$* : 代表 targets 所指定的檔案，但不包含副檔名
$< : 依賴文件列表中的第一個依賴文件 (Dependencies file)
$^ : 依賴文件列表中的所有依賴文件
$? : 依賴文件列表中新於目標文件的文件列表
```

* GCC常用命令及引數 (https://www.itread01.com/content/1547721922.html)