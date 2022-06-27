package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;

public class MySwing07 extends JFrame {
	
	JLabel lbl1;
	JLabel lbl2;
	JLabel lbl3;
	JLabel lbl4;
	JLabel lbl5;
	JLabel lbl6;

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl1 = new JLabel("__");
		lbl1.setBounds(12, 24, 52, 15);
		contentPane.add(lbl1);
		
		lbl2 = new JLabel("__");
		lbl2.setBounds(76, 24, 52, 15);
		contentPane.add(lbl2);
		
		lbl3 = new JLabel("__");
		lbl3.setBounds(141, 24, 52, 15);
		contentPane.add(lbl3);
		
		lbl4 = new JLabel("__");
		lbl4.setBounds(217, 24, 52, 15);
		contentPane.add(lbl4);
		
		lbl5 = new JLabel("__");
		lbl5.setBounds(281, 24, 52, 15);
		contentPane.add(lbl5);
		
		lbl6 = new JLabel("__");
		lbl6.setBounds(372, 24, 52, 15);
		contentPane.add(lbl6);
		
		JButton btn = new JButton("로또!");
		btn.setBounds(174, 190, 95, 23);
		contentPane.add(btn);
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				lotto2();
			}
		});
	}
	
	public void lotto() {
		List<Integer> numbers = new ArrayList<Integer>();
		for(int i = 1; i<=45; i++){
			numbers.add(i);
		}
		
		List<Integer> lotto = new ArrayList<Integer>();
		
		
		int rnd =0;
		int temp = 0;
		while(true) {
			if(lotto.size()>= 6) {
				break;
			}
			
			rnd = (int) (Math.random()*numbers.size());
			if(numbers.get(rnd) > 0) {
				lotto.add(numbers.get(rnd));
				numbers.set(rnd, -1); //그냥 numbers.add(rnd) = -1로 해도 됨
				//혹은 다 섞은 후 remove 써서 없애버리고 항상 0번째거만 뽑아도 됨
			}
			
		}
		
		/*
		for(int i=0; i<lotto.size(); i++) {
			System.out.print(lotto.get(i) + " ");
		}
		System.out.println();
		for(int i=0; i<numbers.size(); i++) {
			System.out.print(numbers.get(i) + " ");
		}
		*/
		
		lbl1.setText(lotto.get(0) + "");
		lbl2.setText(lotto.get(1) + "");
		lbl3.setText(lotto.get(2) + "");
		lbl4.setText(lotto.get(3) + "");
		lbl5.setText(lotto.get(4) + "");
		lbl6.setText(lotto.get(5) + "");
		
	}
	
	public void lotto2() {
		List<Integer> numbers = new ArrayList<Integer>();
		List<Integer> lotto = new ArrayList<Integer>();
		
		for(int i = 1; i<=45; i++){
			numbers.add(i);
		}
		
		int rnd =0;
		int temp = 0;
		
		for(int i = 0; i < 6; i++) {
			rnd = (int)(Math.random()*numbers.size());
			lotto.add(numbers.get(rnd));
			numbers.remove(rnd);
		}
		
		lbl1.setText(lotto.get(0) + "");
		lbl2.setText(lotto.get(1) + "");
		lbl3.setText(lotto.get(2) + "");
		lbl4.setText(lotto.get(3) + "");
		lbl5.setText(lotto.get(4) + "");
		lbl6.setText(lotto.get(5) + "");
	}
}
