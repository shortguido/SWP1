package Berlin;
import Pizza.Pizza;
import Pizza.Pizzeria;

// Berliner Pizzeria
public class BerlinPizzeria extends Pizzeria {
// Erstellung der speziellen Berliner Pizza
	public Pizza erstellePizza(String typ) {
		if (typ.equals("Salami")) {
			return new BerlinerSalamiPizza();
		} else if (typ.equals("Hawaii")) {
			return new BerlinerHawaiiPizza();
		} else if (typ.equals("Calzone")) {
			return new BerlinerCalzonePizza();
		} else if (typ.equals("Quattro Stagioni")) {
			return new BerlinerQuattroStagioniPizza();
		} else {
			return null;
		}
	}
}