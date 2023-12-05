## Time 80 random

```
C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2> c: && cd "c:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2" && cmd /C "C:\Users\Hans\AppData\Local\Programs\Python\Python311\python.exe c:\Users\Hans\.vscode\extensions\ms-python.python-2023.20.0\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher 62106 -- "C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2\testtime.py" "
partition_dyn random 80:
True 98.0856ms
98.0856ms
partition_bnb random 80:
True 98352.6669ms
98352.6669ms
```

## Time 40 random

```
C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2> c: && cd "c:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2" && cmd /C "C:\Users\Hans\AppData\Local\Programs\Python\Python311\python.exe c:\Users\Hans\.vscode\extensions\ms-python.python-2023.20.0\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher 62170 -- "C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2\testtime.py" "
partition_dyn random 40:
True 18.9908ms
18.9908ms
partition_bnb random 40:
True 44.0004ms
44.0004ms
```

## Time 10 random

```
C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2> c: && cd "c:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2" && cmd /C "C:\Users\Hans\AppData\Local\Programs\Python\Python311\python.exe c:\Users\Hans\.vscode\extensions\ms-python.python-2023.20.0\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher 62179 -- "C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2\testtime.py" "
partition_dyn random 10:
True 1.9965ms
1.9965ms
partition_bnb random 10:
False 0.9992ms
0.9992ms
```

## Singular

```
C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2>testtime.py
partition_dyn random 10:
True    0 milliseconds ago 2.9697 ms    40.2 kB 40.2 kB
2.9697 ms       40.2
partition_bnb random 10:
False   0 milliseconds ago 1.029 ms     704 Bytes       0.704 kB
1.029 ms        0.704

C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2>testtime.py
partition_dyn random 10:
True    0 milliseconds ago 2.0115 ms    40.2 kB 40.2 kB
2.0115 ms       40.2
partition_bnb random 10:
False   0 milliseconds ago 0.0 ms       704 Bytes       0.704 kB
0.0 ms  0.704

C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2>testtime.py
partition_dyn random 10:
True    0 milliseconds ago 1.9722 ms    40.2 kB 40.2 kB
1.9722 ms       40.2
partition_bnb random 10:
False   0 milliseconds ago 0.9952 ms    704 Bytes       0.704 kB
0.9952 ms       0.704

C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2>testtime.py
partition_dyn random 10:
True    2 seconds ago 2.0051 ms 40.2 kB 40.2 kB
2.0051 ms       40.2
partition_bnb random 10:
False   0 milliseconds ago 0.9074 ms    704 Bytes       0.704 kB
0.9074 ms       0.704

C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2>testtime.py
partition_dyn random 10:
True    0 milliseconds ago 1.9996 ms    40.2 kB 40.2 kB
1.9996 ms       40.2
partition_bnb random 10:
False   0 milliseconds ago 0.9861 ms    704 Bytes       0.704 kB
0.9861 ms       0.704

C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2>testtime.py
partition_dyn random 10:
True    2.9957 ms       40.2 kB 0 milliseconds ago      40.2 kB
2.9957 ms       40.2
partition_bnb random 10:
False   1.9972 ms       0.704 kB        0 milliseconds ago      704 Bytes
1.9972 ms       0.704

C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2>testtime.py
partition_dyn random 10:
True    2.9929 ms       40.2 kB 0 milliseconds  40.2 kB
2.9929 ms       40.2
partition_bnb random 10:
False   0.0 ms  0.704 kB        0 milliseconds  704 Bytes
0.0 ms  0.704

C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2>testtime.py
partition_dyn random 10:
True    3.0041 ms       40.2 kB 0 milliseconds  40.2 kB
3.0041 ms       40.2 kB 0 milliseconds  40.2 kB
partition_bnb random 10:
False   1.0812 ms       0.704 kB        0 milliseconds  704 Bytes
1.0812 ms       0.704 kB        0 milliseconds  704 Bytes
```

### Avg

```
C:\Users\Hans\Desktop\Kuliah Semester 5\Kotak Sementara\DAA TE 2>testtime.py
partition_dyn random 10:
True    2.0075 ms       40.2 kB 0 milliseconds  40.2 kB
True    4.0002 ms       40.2 kB 0 milliseconds  40.2 kB
True    4.0069 ms       40.2 kB 0 milliseconds  40.2 kB
Avg     3.3382 ms       40.2 kB 0 milliseconds  40.2 kB
partition_dyn random 40:
True    34.0126 ms      382.12 kB       0 milliseconds  382.1 kB
True    29.0589 ms      382.12 kB       0 milliseconds  382.1 kB
True    32.068 ms       382.12 kB       0 milliseconds  382.1 kB
Avg     31.7132 ms      382.12 kB       0 milliseconds  382.1 kB
partition_dyn random 80:
True    88.9711 ms      1195.6 kB       0 milliseconds  1.2 MB
True    81.9921 ms      1195.6 kB       0 milliseconds  1.2 MB
True    63.9966 ms      1195.6 kB       0 milliseconds  1.2 MB
Avg     78.3199 ms      1195.6 kB       0 milliseconds  1.2 MB
partition_bnb random 10:
False   1.0092 ms       0.704 kB        0 milliseconds  704 Bytes
False   1.0047 ms       0.704 kB        0 milliseconds  704 Bytes
False   0.9913 ms       0.704 kB        0 milliseconds  704 Bytes
Avg     1.0018 ms       0.704 kB        0 milliseconds  704 Bytes
partition_bnb random 40:
True    69.9921 ms      4.48 kB 0 milliseconds  4.5 kB
True    63.9904 ms      4.48 kB 0 milliseconds  4.5 kB
True    65.0012 ms      4.48 kB 0 milliseconds  4.5 kB
Total   66.3279 ms      4.48 kB 0 milliseconds  4.5 kB
partition_bnb random 80:
True    131819.3316 ms  9.44 kB 2 minutes       9.4 kB
True    119248.1163 ms  9.44 kB a minute        9.4 kB
True    122654.2242 ms  9.44 kB 2 minutes       9.4 kB
Total   124573.8907 ms  9.44 kB 2 minutes       9.4 kB
```