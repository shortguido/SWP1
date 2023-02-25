package Berlin;

import Pizza.Pizza;

public class BerlinerQuattroStagioniPizza implements Pizza {
	
	public void vorbereiten() {
		System.out.println("Quattro Stagioni-Pizza vorbereiten");
	}

	public void backen() {
		System.out.println("Quattro Stagioni-Pizza backen");
	}

	public void schneiden() {
		System.out.println("Quattro Stagioni-Pizza schneiden");
	}

	public void einpacken() {
		System.out.println("Quattro Stagioni-Pizza einpacken");
	}
}
