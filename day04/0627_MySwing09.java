package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Font;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import static javax.swing.JOptionPane.showMessageDialog;
import javax.swing.SwingConstants;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JButton btn1;
	private JButton btn2;
	private JButton btn3;
	private JButton btn4;
	private JButton btn5;
	private JButton btn6;
	private JButton btn7;
	private JButton btn8;
	private JButton btn9;
	private JButton btn0;
	private JButton call;
	String ph = "";
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(12, 25, 207, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		btn1 = new JButton("1");
		btn1.setFont(new Font("굴림", Font.PLAIN, 15));
		btn1.setBounds(12, 76, 51, 23);
		contentPane.add(btn1);
//		btn1.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				showNum(2);
//			}
//		});
		
		btn2 = new JButton("2");
		btn2.setFont(new Font("굴림", Font.PLAIN, 15));
		btn2.setBounds(86, 77, 51, 23);
		contentPane.add(btn2);
//		btn2.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				showNum(2);
//			}
//		});
		
		btn3 = new JButton("3");
		btn3.setFont(new Font("굴림", Font.PLAIN, 15));
		btn3.setBounds(168, 77, 51, 23);
		contentPane.add(btn3);
//		btn3.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				showNum(3);
//			}
//		});
		
		btn4 = new JButton("4");
		btn4.setFont(new Font("굴림", Font.PLAIN, 15));
		btn4.setBounds(12, 124, 51, 23);
		contentPane.add(btn4);
//		btn4.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				showNum(4);
//			}
//		});
		
		btn5 = new JButton("5");
		btn5.setFont(new Font("굴림", Font.PLAIN, 15));
		btn5.setBounds(86, 125, 51, 23);
		contentPane.add(btn5);
//		btn5.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				showNum(5);
//			}
//		});
		
		btn6 = new JButton("6");
		btn6.setFont(new Font("굴림", Font.PLAIN, 15));
		btn6.setBounds(168, 125, 51, 23);
		contentPane.add(btn6);
//		btn6.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				showNum(6);
//			}
//		});
		
		btn7 = new JButton("7");
		btn7.setFont(new Font("굴림", Font.PLAIN, 15));
		btn7.setBounds(12, 174, 51, 23);
		contentPane.add(btn7);
//		btn7.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				showNum(7);
//			}
//		});
		
		btn8 = new JButton("8");
		btn8.setFont(new Font("굴림", Font.PLAIN, 15));
		btn8.setBounds(86, 175, 51, 23);
		contentPane.add(btn8);
//		btn8.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				showNum(8);
//			}
//		});
		
		btn9 = new JButton("9");
		btn9.setFont(new Font("굴림", Font.PLAIN, 15));
		btn9.setBounds(168, 175, 51, 23);
		contentPane.add(btn9);
//		btn9.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				showNum(9);
//			}
//		});
		
		btn0 = new JButton("0");
		btn0.setFont(new Font("굴림", Font.PLAIN, 15));
		btn0.setBounds(12, 219, 51, 23);
		contentPane.add(btn0);
//		btn0.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				showNum(0);
//			}
//		});
		
		call = new JButton("CALL");
		call.setFont(new Font("굴림", Font.PLAIN, 15));
		call.setBounds(86, 220, 133, 23);
		contentPane.add(call);
		
		call.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				calling();
			}
		});
		
		btn1.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn2.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn3.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn4.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn5.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn6.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn7.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn8.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn9.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn0.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
	}
	
	public void showNum(int num) {
		addNum(num);
		tf.setText(ph);
	}
	
	public void addNum(int num) {
		ph += num+"";
	}

	public void calling() {
		showMessageDialog(null, "calling\n" + tf.getText());
	}
	
	//쌤 답
	public void myclick(MouseEvent e) {
		JButton imsi = (JButton)e.getSource();
		String str_new = imsi.getText();
		String str_old = tf.getText();
		
		tf.setText(str_old + str_new);
	}
}
