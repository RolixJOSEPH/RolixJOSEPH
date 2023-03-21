package ht.chcl.rolix;
import java.util.Scanner;

// Classe de conversion $US/Gdes.
public class Conversion {
	
	float tauxEchange = 90;
	Scanner entrerClavier = new Scanner(System.in);
	
	
	public void dollarEnGdes(float montant) {
		System.out.println(montant + " $US en Gourdes: " + montant * tauxEchange + "Gdes");
	}
	
	
	public void GdesEndollar(float montant) {
		System.out.println(montant + " Gourdes en $US : " + montant / tauxEchange + "$US");
	}
	
	
}

