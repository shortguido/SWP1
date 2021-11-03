
public class Iterativ {
	
	public static int summe(int[] a) {
		int summe = 0; // summe bei 0 beginnen lassen
		for (int i = 0; i < a.length; i++) {
			summe += a[i];
		}
		return summe;

	}

}
//Iterativ = mehrfache Ausführung einer oder mehrerer Anweisungen 
