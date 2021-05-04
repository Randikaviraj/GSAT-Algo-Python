# GSAT-Algo-Python
```
procedure GSAT(A,Max_Tries,Max_Flips)
  A: is a CNF formula
  for i:=1 to Max_Tries do
    S <- instantiation of variables
    for j:=1 to Max_Iter do
      if A satisfiable by S then
        return S
      endif
      V <- the variable whose flip yield the most important raise in the number of satisfied clauses;
      S <- S with V flipped;
    endfor
  endfor
  return the best instantiation found
end GSAT
```

> This code solve the SAT problem using the GSAT solution,here we have to give CNF form problem in a text file in the following way.
> For Example: {{!B A !C}{B A !C}{!B !A !C}{B}{C}} will be written in SAT instance in DIMACS CNF input format.
```
 p cnf 3  5
 -2 1 -3 0
 2 1 -3 0
 -2 -1 -3 0
 2 0
 3 0
 ```
 
- First line contain the  `p cnf  <no of variables> <no of lines>`
- All variable has a unique no and not is signify by the negative sign
- Zero indicate the end of line(Not required to use zero at the end,inbuilt programme will recognoze the end of line)
  
## run programme using
```
python3 Gsat.py  <data input file name>
```
