set terminal x11
set term canvas mousing size 500, 500
set xlabel "Miles"
set ylabel "Time"
set zlabel "Acceleration"
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb'grey' behind
set output "index.html"
plot "lsmplot.dat" title "LSM303 Accelerometer Graph" with linespoints
