package Pizza;

// Abstrakte Pizzeria-Klasse
public abstract class Pizzeria {
	
	public abstract Pizza erstellePizza(String typ);

	public Pizza bestellePizza(String typ) {
		Pizza pizza = erstellePizza(typ);
		pizza.vorbereiten();
		pizza.backen();
		pizza.schneiden();
		pizza.einpacken();
		return pizza;
	}
}
