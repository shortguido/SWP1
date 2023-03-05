package Pizza;

public class PizzaFactory extends Pizzeria {
	public Pizza erstellePizza(String typ) {
		Pizza pizza = null;
		
		if (typ.equals("Calzone"))
			pizza = new CalzonePizza();
		else if (typ.equals("Hawaii"))
			pizza = new HawaiiPizza();
		else if (typ.equals("Salami"))
			pizza = new SalamiPizza();
		else if (typ.equals("QuattroStagioni"))
			pizza = new QuattroStagioniPizza();
		
		return pizza;
	}
}
