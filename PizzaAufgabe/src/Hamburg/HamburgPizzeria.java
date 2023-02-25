package Hamburg;
import Pizza.Pizza;
import Pizza.Pizzeria;

// Berliner Pizzeria
public class HamburgPizzeria extends Pizzeria {
// Erstellung der speziellen Berliner Pizza
	public Pizza erstellePizza(String typ) {
		if (typ.equals("Salami")) {
			return new HamburgSalamiPizza();
		} else if (typ.equals("Hawaii")) {
			return new HamburgHawaiiPizza();
		} else if (typ.equals("Calzone")) {
			return new HamburgCalzonePizza();
		} else if (typ.equals("Quattro Stagioni")) {
			return new HamburgQuattroStagioniPizza();
		} else {
			return null;
		}
	}
}