
//funcion que dice en que cuadrante estan las dos variables
// para definir la funcion en PSenInt se debe usar la sintaxis Funcion name <- name2 ( variables que se tienen que pasar ejemplo:(coX,coY) ) 
//name2 debe ser diferente a name
Funcion cuadrante <- calcular_cuadrante ( coX,coY )
	si coX >0 y coY>0 Entonces
		Escribir "primer cuadrante"
	FinSi
	si coX <0 y coY>0 Entonces
		Escribir "segundo cuadrante"
	FinSi
	si coX <0 y coY<0 Entonces
		Escribir "tercer cuadrante"
	FinSi
	si coX >0 y coY<0 Entonces
		Escribir "cuarto cuadrante"
	FinSi
	si coX =0 y coY<>0 Entonces
		Escribir "sobre el eje Y"
	FinSi
	si coY =0 y coX<>0 Entonces
		Escribir "sobre el eje X"
	FinSi
	si coX =0 y coY=0 Entonces
		Escribir "origen"
	FinSi
Fin Funcion

//la funcion area_perimetro trabaja llamando la funcion cuadrante por eso mismo no es necesario llamar cuadrante para mostrar en que cuadrante esta
//en programacion orientada o objeto (POO) se llama composición 
Funcion area_perimetro <- areaTriangulo ( coX,coY )
	//las variables dentro de la funcion no hace falta definirlas porque son momentaneas solo en el Algoritmo es necesario definir
	cuadrante<-calcular_cuadrante ( coX,coY );
	//condicion segun el cuadrante en el que esta
	si cuadrante <> "origen" Entonces
		si cuadrante <> "sobre el eje X" y cuadrante <> "sobre el eje Y" Entonces
			//busque las formulas por chatgpt nose como sacar perimetro ni area :(
			area<- 0.5 *coX *coY;	
			hipotenusa <-(coX*coX) + (coY*coY);
			perimetro <- coX + coY + hipotenusa;
			//muestra area y perimetro
			Escribir "Area:", area," / ","Perimetro: ",perimetro;
		SiNo
			si cuadrante ="sobre el eje X" Entonces
				area<-coY;
				perimetro<-2 * coY + 2;
				Escribir "Area:", area," / ","Perimetro: ",perimetro;
			SiNo
				area<-coX;
				perimetro<-2*coX+2;
				Escribir "Area:", area," / ","Perimetro: ",perimetro;
			FinSi
		FinSi

		
	FinSi
Fin Funcion


Algoritmo main
	// se asignan las variables como real 
	Definir coX,coY como real;
	Escribir "==ingrese cordenada primra la X y despues la Y==";
	//leer ambas variables una despues de la otra una primera o otra despues
	leer cox,coy;
	//si quieres que muestre la funcion de cuadrante sacar la // de a linea 58
	//cuadrante <- calcular_cuadrante ( coX,coY )
	Escribir "===============================";
	//esta Funcion toma las dos variables y genera el calculo para la formula del calulo me apoye de chat gpt porque ni idea
	area_perimetro <- areaTriangulo ( coX,coY )
	
FinAlgoritmo


