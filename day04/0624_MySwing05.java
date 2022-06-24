package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Font;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_mine;
	private JTextField tf_com;
	private JTextField tf_result;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
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
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_mine = new JLabel("나");
		lbl_mine.setFont(new Font("굴림", Font.PLAIN, 20));
		lbl_mine.setBounds(52, 28, 52, 15);
		contentPane.add(lbl_mine);
		
		JLabel lbl_com = new JLabel("com");
		lbl_com.setFont(new Font("굴림", Font.PLAIN, 20));
		lbl_com.setBounds(52, 84, 52, 15);
		contentPane.add(lbl_com);
		
		JLabel lbl_result = new JLabel("결과");
		lbl_result.setFont(new Font("굴림", Font.PLAIN, 20));
		lbl_result.setBounds(52, 138, 52, 30);
		contentPane.add(lbl_result);
		
		tf_mine = new JTextField();
		tf_mine.setFont(new Font("굴림", Font.PLAIN, 20));
		tf_mine.setBounds(185, 10, 138, 45);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);
		
		tf_com = new JTextField();
		tf_com.setFont(new Font("굴림", Font.PLAIN, 20));
		tf_com.setBounds(185, 68, 138, 46);
		contentPane.add(tf_com);
		tf_com.setColumns(10);
		
		tf_result = new JTextField();
		tf_result.setFont(new Font("굴림", Font.PLAIN, 20));
		tf_result.setBounds(166, 138, 157, 45);
		contentPane.add(tf_result);
		tf_result.setColumns(10);
		
		JButton btn = new JButton("게임하기");
		btn.setFont(new Font("굴림", Font.PLAIN, 20));
		btn.setBounds(52, 201, 120, 40);
		contentPane.add(btn);
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				hj();
			}
		});
	}
	
	public void hj() {
		int rnd = (int)(Math.random()*100+1);
		
		if(rnd%2 == 0) {
			tf_com.setText("짝");
		}else {
			tf_com.setText("홀");
		}
		
		if(tf_com.getText().equals(tf_mine.getText())) {
			tf_result.setText("\"나\"승리!");
		}else {
			tf_result.setText("\"컴퓨터\"승리!");
		}
	}

}
