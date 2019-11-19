# ejercicio-14-segunda-parte-arnoldgar98
ejercicio-14-segunda-parte-arnoldgar98 created by GitHub Classroom

1. Se modela la ecuación de oscilador armónico simple.
2. De acuerdo a la ecuación se esperan soluciones de tipo coseno y seno. 
3. Si bien la solución muestra la forma del seno, con cada iteración computacional que pasa, se va aumentando la amplitud y esto es algo que no deberia suceder. Ya que no correspondería con el modelo de armonico simple y por tanto euler no es un metodo muy acertivo.
4. Al revisar las graficas obtenidas para el metodo Euler y RungeKutta. Se observa que las amplitudes para cada oscilación en el tiempo en el caso de euler es creciente. Mientras que con el método rungekutta permancen con igual amplitud en el tiempo. Los mismo sucede con el grafio de velcoidad, para euler se observan una aproximación al circulo, mientras que en rungekutta se la velocidad permanece casi con la misma amplitud en el tiempo. Esto se debe a la aproximación de pendientes que tiene el metodo de rungekuta lo cual lo hace el mejor metodo para resolver ODES.
5. se espera que las oscilaciones no cambien en el tiempo. Es decir que se genere el circulo para la velocidad y las amplitudes constantes para la posición.
6. Al agregar el termino de fricción, se genera el armonico "dumped", lo cual hace que la oscilación y la energía disminuyan con el tiempo. De allí que el grafico de posicion se observe con decaimiento en la amplitud y la velocidad es una espiral decreciente.
7. Por la teoria de ondas, se sabe que si se aumenta mucho el valor de lambda, la ecuación deja su caracter lineal y genera resultados dispersivos y esto es algo que no sirve para modelar armonico.
