package day04;

public class MyGugudan {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		for(int i = 1; i < 10; i++) {
//			System.out.println(i + "단");
//			for(int j = 1; j < 10; j++) {
//				System.out.println(i + " * " + j + " = " + (i*j));
//			}
//		}
		
		//짝수만 출력
//		for(int i = 1; i < 10; i++) {
//			if (i % 2 == 0) {
//				System.out.println(i + "단");
//				for (int j = 1; j < 10; j++) {
//					System.out.println(i + " * " + j + " = " + (i * j));
//				}
//			}
//		}
		
		//9, 8, 6, 3만 출력
		int[] num = {9, 8, 6, 3};
		
		for(int i = 0; i < num.length; i++) {
			System.out.println(num[i] + " * " + 1 + " = " + (num[i] * 1));
			System.out.println(num[i] + " * " + 2 + " = " + (num[i] * 2));
			System.out.println(num[i] + " * " + 3 + " = " + (num[i] * 3));
			System.out.println(num[i] + " * " + 4 + " = " + (num[i] * 4));
			System.out.println(num[i] + " * " + 5 + " = " + (num[i] * 5));
			System.out.println(num[i] + " * " + 6 + " = " + (num[i] * 6));
			System.out.println(num[i] + " * " + 7 + " = " + (num[i] * 7));
			System.out.println(num[i] + " * " + 8 + " = " + (num[i] * 8));
			System.out.println(num[i] + " * " + 9 + " = " + (num[i] * 9));
		}
		
		
	}
}
