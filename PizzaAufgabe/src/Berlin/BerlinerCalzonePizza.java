package Berlin;

import Pizza.Pizza;

public class BerlinerCalzonePizza implements Pizza {
	
	public void vorbereiten() {
		System.out.println("Calzone-Pizza vorbereiten");
	}

	public void backen() {
		System.out.println("Calzone-Pizza backen");
	}

	public void schneiden() {
		System.out.println("Calzone-Pizza schneiden");
	}

	public void einpacken() {
		System.out.println("Calzone-Pizza einpacken");
	}
}