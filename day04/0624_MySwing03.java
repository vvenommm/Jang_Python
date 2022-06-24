package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import java.awt.Font;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setFont(new Font("굴림", Font.PLAIN, 30));
		tf1.setBounds(38, 102, 52, 47);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setFont(new Font("굴림", Font.PLAIN, 30));
		tf2.setBounds(166, 102, 40, 47);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		tf3 = new JTextField();
		tf3.setFont(new Font("굴림", Font.PLAIN, 30));
		tf3.setBounds(305, 102, 65, 47);
		contentPane.add(tf3);
		tf3.setColumns(10);
		
		JLabel lblNewLabel = new JLabel("+");
		lblNewLabel.setFont(new Font("굴림", Font.PLAIN, 30));
		lblNewLabel.setBounds(118, 103, 27, 44);
		contentPane.add(lblNewLabel);
		
		JButton btn = new JButton("=");
		btn.setFont(new Font("굴림", Font.PLAIN, 30));
		btn.setBounds(235, 106, 58, 43);
		contentPane.add(btn);
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// TODO Auto-generated method stub
				super.mouseClicked(e);
				//아래와 같이 메소드를 만들어서 실행하거나
//				myclick();
				
				//아래와 같이 그냥 다 적거나
				String total = Integer.parseInt(tf1.getText()) + Integer.parseInt(tf2.getText()) + "";
				tf3.setText(total);
			}
		});
	}
	
	public void myclick() {
		String a = tf1.getText();
		String b = tf2.getText();
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		
		int sum = aa = bb;
		
		tf3.setText(String.valueOf(sum));
	}
}
