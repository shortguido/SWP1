package Pizza;

import Rostock.*;
import Berlin.*;
import Hamburg.*;

public class Test {
	public static void main (String[] args) {
		
		Pizzeria pizzeria = new PizzaFactory();
		Pizza ps = pizzeria.bestellePizza("Salami");
		System.out.println();
		RostockPizzeria rp = new RostockPizzeria();
		Pizza ph = rp.bestellePizza("Hawaii");
		System.out.println();
		BerlinPizzeria bp = new BerlinPizzeria();
		Pizza pq = bp.bestellePizza("Quattro Stagioni");
		System.out.println();
		HamburgPizzeria hp = new HamburgPizzeria();
		Pizza pc = hp.bestellePizza("Calzone");
	}
}
