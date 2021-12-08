
public class Bubblesort {
	public static void main(String[] args) {
		int[] arr = { 5, 4, 3, 2, 1 };
		bubblesort(arr);
	}

	public static void bubblesort(int[] array) {
		int stelle = 0;
		int hilfe = 0;
		if (array[stelle] >= array[stelle++]) {
			System.out.println(stelle);
			hilfe = array[stelle--];
			stelle++;
			array[stelle] = array[stelle--];
			hilfe = array[stelle];
			System.out.println(stelle);

			stelle++;
			System.out.println(stelle);
			System.out.println(array[0]);
		}
		for (int i = 0; i <= array.length; i++) {

		}
	}
}
