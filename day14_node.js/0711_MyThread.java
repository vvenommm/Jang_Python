package day14;

public class MyThread {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		printNumber();
		printAscii();
	}

	private static void printNumber() {
		// TODO Auto-generated method stub
		
		new Thread(new Runnable() {
			
			@Override
			public void run() {
				// TODO Auto-generated method stub
				for(int i = 1; i < 10001; i ++) {
					
					if(i%100 == 0) {
						System.out.println();
					}
					System.out.print(i + " ");
				}
			}
		}).start();
		
	}
	
	private static void printAscii() {
		// TODO Auto-generated method stub
		
		new Thread(new Runnable() {
			
			@Override
			public void run() {
				// TODO Auto-generated method stub
				for(int i = 1; i < 10001; i ++) {
					
					if(i%100 == 0) {
						System.out.println();
					}
					System.out.print((char)i + " ");
				}
			}
		}).start();
		
	}

}
