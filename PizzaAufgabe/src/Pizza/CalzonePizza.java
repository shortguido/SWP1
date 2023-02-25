package Pizza;

public class CalzonePizza implements Pizza {
	
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