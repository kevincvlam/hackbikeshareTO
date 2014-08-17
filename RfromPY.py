import pyRserve

rcmd = pyRserve.connect(host='localhost', port=6311)



print(rcmd('rnorm(20, mean=2, sd=0.1)'))

rcmd('b <- c(1,3,5,7,9)')
print(rcmd('b'))

rcmd('a <- c("COL1","COL1","COL1","COL2","COL2","COL2","COL3","COL3")')
rcmd('b <- c("Item1","Item1","Item2","Item2","Item3","Item3","Item3","Item3")')
rcmd('results <- table(a,b)')
print(rcmd('results'))

rcmd('x <- seq(-20,20,by=.5)')
rcmd('y <- dt(x,df=10)')
rcmd('plot(x,y)')

This is the output (the graph is plotted in R window and not shown here)
[ 2.02055894  2.05137019  1.97653928  1.99654565  2.08948691  2.07250623
  1.95475797  2.11145948  1.97653835  2.01341228  2.05299939  2.14354837
  2.06876532  1.94614396  1.9924665   2.08839507  1.87483786  2.08817775
  1.97000129  2.26570712]
[ 1.  3.  5.  7.  9.]
[[2 0 0]
 [1 1 0]
 [0 2 2]]
