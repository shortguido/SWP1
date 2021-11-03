
public class Rekursiv {

	private static int sum(int i) {
		if (i > 0) {
			return i + sum(i - 1);
		}

		else {
			return 0;
		}

	}
}
//Rekursiv = Methode wird so lange aufgerufen bis eine Abbruchbedingung erfüllt ist