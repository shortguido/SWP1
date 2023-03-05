package Rostock;
import Pizza.Pizza;
import Pizza.Pizzeria;


public class RostockPizzeria extends Pizzeria {

	@Override
	public Pizza erstellePizza(String typ) {
		if (typ.equals("Salami")) {
			return new RostockSalamiPizza();
		} else if (typ.equals("Hawaii")) {
			return new RostockHawaiiPizza();
		} else if (typ.equals("Calzone")) {
			return new RostockCalzonePizza();
		} else if (typ.equals("Quattro Stagioni")) {
			return new RostockQuattroStagioniPizza();
		} else {
			return null;
		}
	}
}