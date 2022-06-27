package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.Font;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JTextArea;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_start;
	private JTextField tf_last;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl1 = new JLabel("첫 별 수");
		lbl1.setBounds(49, 54, 54, 15);
		contentPane.add(lbl1);
		
		JLabel lbl1_1 = new JLabel("끝 별 수");
		lbl1_1.setBounds(49, 109, 54, 15);
		contentPane.add(lbl1_1);
		
		tf_start = new JTextField();
		tf_start.setFont(new Font("굴림", Font.PLAIN, 20));
		tf_start.setBounds(153, 51, 106, 21);
		contentPane.add(tf_start);
		tf_start.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setFont(new Font("굴림", Font.PLAIN, 20));
		tf_last.setColumns(10);
		tf_last.setBounds(153, 103, 106, 21);
		contentPane.add(tf_last);
		
		JButton btn = new JButton("별 출력");
		btn.setBounds(293, 86, 95, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setFont(new Font("Monospaced", Font.PLAIN, 15));
		ta.setBounds(49, 159, 210, 119);
		contentPane.add(ta);
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				star2(Integer.parseInt(tf_last.getText()));
			}
		});
	}
	
	public void star() {
		
		int start = Integer.parseInt(tf_start.getText());
		int last = Integer.parseInt(tf_last.getText());
		int star = 0;
		
		for (int i = 0; i < start; i++) {
            System.out.print("*");
            star = i;
        }
        for(int j = 0; j < last-star; j++) {
        	System.out.print("");
        }
        System.out.println();
	}
	
	public void star2(int max) {
		int start = Integer.parseInt(tf_start.getText());
		String s = "";
		
		//첫 시작 별 개수
		for(int i = 0; i < start-1; i++) {
			s += "*";
		}
		
		//마지막 시작 별 개수
		for(int i = 0; i < max-1; i++) {
			s += "*";
			ta.append(s + "\n");
//			System.out.print(s + "\n");
		}
	}
	
	//선생님 풀이
	public void myclick() {
		String a = tf_start.getText();
		String b = tf_last.getText();
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		
		String txt = "";
		
		for(int i = aa; i<=bb; i++) {
			txt += getStart(i);
		}
		
		ta.setText(txt);
	}
	
	public String getStart(int cnt) {
		String ret = "";
		for(int i = 0; i < cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		
		return ret;
	}
}
