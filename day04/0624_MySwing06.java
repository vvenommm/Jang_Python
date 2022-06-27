package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import java.awt.Font;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JLabel;
import javax.swing.JButton;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JTextField tf4;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setFont(new Font("굴림", Font.PLAIN, 20));
		tf1.setBounds(22, 28, 106, 30);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl1 = new JLabel("에서");
		lbl1.setFont(new Font("굴림", Font.PLAIN, 20));
		lbl1.setBounds(140, 28, 49, 25);
		contentPane.add(lbl1);
		
		tf2 = new JTextField();
		tf2.setFont(new Font("굴림", Font.PLAIN, 20));
		tf2.setColumns(10);
		tf2.setBounds(201, 28, 106, 30);
		contentPane.add(tf2);
		
		JLabel lbl2 = new JLabel("까지");
		lbl2.setFont(new Font("굴림", Font.PLAIN, 20));
		lbl2.setBounds(319, 31, 78, 25);
		contentPane.add(lbl2);
		
		tf3 = new JTextField();
		tf3.setFont(new Font("굴림", Font.PLAIN, 20));
		tf3.setColumns(10);
		tf3.setBounds(22, 100, 106, 30);
		contentPane.add(tf3);
		
		tf4 = new JTextField();
		tf4.setFont(new Font("굴림", Font.PLAIN, 20));
		tf4.setColumns(10);
		tf4.setBounds(22, 165, 106, 43);
		contentPane.add(tf4);
		
		JButton btn = new JButton("배수의 합은");
		btn.setFont(new Font("굴림", Font.PLAIN, 20));
		btn.setBounds(152, 100, 155, 30);
		contentPane.add(btn);
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
	}
	
	//이 파일 안에서만 쓰겠다고 하면 private으로 해도 됨
	public void myClick() {
		int start = Integer.parseInt(tf1.getText());
		int end = Integer.parseInt(tf2.getText());
		int num = Integer.parseInt(tf3.getText());
		int sum = 0;
		
		for(int i = start; i <= end; i++) {
			if(i%num == 0) {
				sum += i;
			}
		}
		tf4.setText(String.valueOf(sum));
	}

}
