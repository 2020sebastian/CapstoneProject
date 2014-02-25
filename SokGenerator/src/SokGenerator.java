import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

/**
 * @author sebastiandemian
 *
 */
public class SokGenerator {
	
	static Point2D a;
	static Point2D b;
	static Point2D c;
	static Point2D d;
	static Point2D e;
	static Point2D f;
	static Point2D g;
	static Point2D h;
	static Point2D i;
	static Point2D j;
	static Point2D k;
	static Point2D l;
	static Point2D m;
	static Point2D n;
	static Point2D o;
	static Point2D p;
	static Point2D q;
	static Point2D r;
	static Point2D s;
	static Point2D t;
	static Point2D u;
	static Point2D v;
	static Point2D w;
	static Point2D x;
	static Point2D y;
	static Point2D z;
	
	
	
	


	public static void generateKeyboard() throws FileNotFoundException{
		
		Scanner KeyboardScanner = new Scanner(new FileReader("bin/qwerty.txt"));
		
		while (KeyboardScanner.hasNextLine()){
			String line = KeyboardScanner.nextLine();
			String[] item = line.split("\\s+");
			
			//get letter
			char name = item[0].charAt(0);
			//System.out.println(name);
			
			//get coordinates
			int first = Integer.parseInt(item[1]);
			int second = Integer.parseInt(item[2]);
			
			
			if (name == 'a'){
				a = new Point2D(first, second);
			} else if (name == 'b') {
				b = new Point2D(first, second);
			} else if (name == 'c') {
				c = new Point2D(first, second);
			} else if (name == 'd') {
				d = new Point2D(first, second);
			} else if (name == 'e') {
				e = new Point2D(first, second);
			} else if (name == 'f') {
				f = new Point2D(first, second);
			} else if (name == 'g') {
				g = new Point2D(first, second);
			} else if (name == 'h') {
				h = new Point2D(first, second);
			} else if (name == 'i') {
				i = new Point2D(first, second);
			} else if (name == 'j') {
				j = new Point2D(first, second);
			} else if (name == 'k') {
				k = new Point2D(first, second);
			} else if (name == 'l') {
				l = new Point2D(first, second);
			} else if (name == 'm') {
				m = new Point2D(first, second);
			} else if (name == 'n') {
				n = new Point2D(first, second);
			} else if (name == 'o') {
				o = new Point2D(first, second);
			} else if (name == 'p') {
				p = new Point2D(first, second);
			} else if (name == 'q') {
				q = new Point2D(first, second);
			} else if (name == 'r') {
				r = new Point2D(first, second);
			} else if (name == 's') {
				s = new Point2D(first, second);
			} else if (name == 't') {
				t = new Point2D(first, second);
			} else if (name == 'u') {
				u = new Point2D(first, second);
			} else if (name == 'v') {
				v = new Point2D(first, second);
			} else if (name == 'w') {
				w = new Point2D(first, second);
			} else if (name == 'x') {
				x = new Point2D(first, second);
			} else if (name == 'y') {
				y = new Point2D(first, second);
			} else if (name == 'z') {
				z = new Point2D(first, second);
			}
			
		}
		
	}
	
	public static void drawOriginPoints(){
		
		StdDraw.setCanvasSize(1000, 500);
		StdDraw.setXscale(0, 1000);
		StdDraw.setYscale(0, 500);
		StdDraw.setPenRadius(.03);
		StdDraw.setPenColor(StdDraw.BLUE);
		
		a.draw();
		b.draw();
		c.draw();
		d.draw();
		e.draw();
		f.draw();
		g.draw();
		h.draw();
		i.draw();
		j.draw();
		k.draw();
		l.draw();
		m.draw();
		n.draw();
		o.draw();
		p.draw();
		r.draw();
		s.draw();
		t.draw();
		u.draw();
		v.draw();
		w.draw();
		x.draw();
		y.draw();
		z.draw();
	
		
		
	}

	
	@Override
	public String toString() {
		return x + "," + y;
	}

	public static void main(String[] args) throws IOException {
		
		
		
		
		

//Scanner WordScanner = new Scanner(new FileReader("bin/words.txt"));
Scanner WordScanner = new Scanner(new FileReader("bin/tinyWords.txt"));

			
			//initialize keyboard
			generateKeyboard();
			
			//draw key origins on the canvas
			drawOriginPoints();
			
			
			
			
			Point2D [] points = new Point2D[50];
			
			
			
			while (WordScanner.hasNextLine()){
				String word = WordScanner.nextLine().toLowerCase();
				System.out.print(word + ",");
				
				char[] foo = word.toCharArray();
				
				int length = 0;
				
	
				for (int item = 0; item < word.length(); item++){
					if (foo[item]== 'a'){
						points[item] = a;
					} else if (foo[item]== 'b'){
						points[item] = b;
					}  else if (foo[item]== 'c'){
						points[item] = c;
					} else if (foo[item]== 'd'){
						points[item] = d;
					} else if (foo[item]== 'e'){
						points[item] = e;
					} else if (foo[item]== 'f'){
						points[item] = f;
					} else if (foo[item]== 'g'){
						points[item] = g;
					} else if (foo[item]== 'h'){
						points[item] = h;
					} else if (foo[item]== 'i'){
						points[item] = i;
					} else if (foo[item]== 'j'){
						points[item] = j;
					} else if (foo[item]== 'k'){
						points[item] = k;
					} else if (foo[item]== 'l'){
						points[item] = l;
					} else if (foo[item]== 'm'){
						points[item] = m;
					} else if (foo[item]== 'n'){
						points[item] = n;
					} else if (foo[item]== 'o'){
						points[item] = o;
					} else if (foo[item]== 'p'){
						points[item] = p;
					} else if (foo[item]== 'r'){
						points[item] = r;
					} else if (foo[item]== 's'){
						points[item] = s;
					} else if (foo[item]== 't'){
						points[item] = t;
					} else if (foo[item]== 'u'){
						points[item] = u;
					} else if (foo[item]== 'v'){
						points[item] = v;
					} else if (foo[item]== 'w'){
						points[item] = w;
					} else if (foo[item]== 'x'){
						points[item] = x;
					} else if (foo[item]== 'y'){
						points[item] = y;
					} else if (foo[item]== 'z'){
						points[item] = z;
					}
					 
				}
				
				for (int i = 0; i < word.length()-1; i++){
					length += points[i].distanceTo(points[i+1]);
					
					//System.out.print(length);
							
				}
				
				
				//StdDraw.setPenRadius(.01);
				StdDraw.setPenRadius(.002);
				StdDraw.setPenColor(StdDraw.RED);
				System.out.print(points[0].x());
				System.out.print(",");
				System.out.print(points[0].y());
				System.out.print(",");
				System.out.print(points[word.length()-1].x());
				System.out.print(",");
				System.out.print(points[word.length()-1].y());
				System.out.print(",");
				System.out.print(length);
				
				
				
				
//				for (int i = 0; i < word.length()-1; i++){
//					System.out.print(points[i+1].x());
//					System.out.print(",");
//					System.out.print(points[i+1].y());
//					System.out.print(",");
		
					
					//points[i].drawTo(points[i+1]);
				
				//}
				System.out.println();
				
				//break;
			}
	
	}
}


