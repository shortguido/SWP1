package Pizza;

// Abstrakte Pizzeria-Klasse
public abstract class Pizzeria {
// Factory-Methode zum Erstellen der Pizza
	public abstract Pizza erstellePizza(String typ);

	public void bestellePizza(String typ) {
		Pizza pizza = erstellePizza(typ);
		pizza.vorbereiten();
		pizza.backen();
		pizza.schneiden();
		pizza.einpacken();
	}
}
