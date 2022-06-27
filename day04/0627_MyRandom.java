package day04;

public class MyRandom01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr9 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
		
		for(int i=0; i<arr9.length; i++) {
			System.out.print(arr9[i] + " / ");
		}
	}

}


///////////////////////////////////////////////////////////////////


package day04;

import java.util.ArrayList;

public class MyRandom03 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//remove(int index)와 혼란을 야기할 수 있으므로 제네릭 타입을 바꿔줌
		ArrayList<String> arr9 = new ArrayList<String>();
		ArrayList<String> arr3 = new ArrayList<String>();
		arr9.add(1 + "");
		arr9.add(2 + "");
		arr9.add(3 + "");
		
		for(int i = 0; i<3; i++) {
			int rnd = 0;
			String a = arr9.get(0);
			arr3.add(a);
			arr9.remove(0); //앞으로 한 자리씩 당겨짐 -> 그러면 remove도 (0)번째, 꺼내는 것도 (0)번째인걸로 뽑으면 됨.
		}
		System.out.println(arr3.get(0));
		System.out.println(arr3.get(1));
		System.out.println(arr3.get(2));
	}
}
