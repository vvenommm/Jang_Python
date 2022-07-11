package day14;

public class MyFunction {

	public static void main(String[] args) {
		// TODO 스레드
		printNumber();
		printAscii();

	}

	private static void printNumber() {
		// TODO Auto-generated method stub
		for(int i = 1; i < 10001; i ++) {
			
			if(i%100 == 0) {
				System.out.println();
			}
			System.out.print(i + " ");
		}
	}

	private static void printAscii() {
		// TODO Auto-generated method stub
		for(int i = 1; i < 10001; i ++) {
			
			if(i%100 == 0) {
				System.out.println();
			}
			System.out.print((char) i + " ");
		}
	}
	
}
