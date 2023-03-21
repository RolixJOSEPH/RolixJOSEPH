package ht.chcl.rolix;
import java.util.Scanner;


public class Main {
	static Scanner entrerClavier = new Scanner(System.in);
	
	
	public static int menu() {
		int choix;
		System.out.println("1: Dollars en Gourdes US\n"
				+ "2: Gourdes en dollars \n"
				+"0: Quiter\n"
				+ "Choisir Votre option");
		choix = entrerClavier.nextInt();
		return(choix);
	}

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("  __________XCHANGE Gdes/$US________");
		System.out.println("Taux d'echange par defaut: 90gdes/&US\n");
		
		Conversion conversion1 = new Conversion();
		float qtite = 0;
		int option = -1 ;
		
		
		while (option != 0 ) {
			option = menu();
			
			switch (option) {
				case 1:{
					System.out.println("Conversion $US en Gourdes");
					System.out.println("Entrer le montant:");
					qtite = entrerClavier.nextFloat();
					conversion1.dollarEnGdes(qtite);
					break;
				}
				case 2:{
					System.out.println("Conversion Gourdes en $US");
					System.out.println("Entrer le montant:");
					qtite = entrerClavier.nextFloat();
					conversion1.GdesEndollar(qtite);
					break;
				}
				
				case 0:{
					System.out.println("Bye");
					System.exit(0);
					break;
					
				}
				default:{
					System.out.println("Choix invalide");
					break;
					
				}
		
			}
		}
	}

}
