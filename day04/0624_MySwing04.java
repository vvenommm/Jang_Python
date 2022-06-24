package day04;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.Font;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("구구단");
		lblNewLabel.setFont(new Font("굴림", Font.PLAIN, 30));
		lblNewLabel.setBounds(27, 10, 110, 42);
		contentPane.add(lblNewLabel);
		
		tf = new JTextField();
		tf.setFont(new Font("굴림", Font.PLAIN, 30));
		tf.setBounds(136, 13, 106, 37);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.setFont(new Font("굴림", Font.PLAIN, 30));
		btn.setBounds(254, 13, 159, 37);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setFont(new Font("Monospaced", Font.PLAIN, 15));
		ta.setBounds(27, 62, 287, 191);
		contentPane.add(ta);
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				gugu();
			}
		});
	}
	
	public void gugu() {
		int dan = Integer.parseInt(tf.getText());
		  
		for(int i = 1; i < 10; i++) {
			ta.append(dan + " * " + i + " = " + (dan*i) + "\n");
		}
	}
}
