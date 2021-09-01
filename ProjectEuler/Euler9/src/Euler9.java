/*
 * 
 A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
 a2 + b2 = c2

 For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

 There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 Find the product abc.
 */

class Euler9 {

    public static void main(String args[]) {
	int a = 3, b = 4, c = 5;

	// wiedzac, ze dla dowolnego a,b,c, gdzie a^2+b^2=c^2 i dla dowolnego d
	// spelniona jest zaleznosc, ze (da)^2+(db)^2 = (dc)^2 mozemy zalozyc, ze (a+b+c)*d = 1000

	int d;
	for (d = 1; d <=10; d++  ) {
	    int tmp_a = a * d;
	    int tmp_b = b * d;
	    int tmp_c = c * d;
	    
	    //obliczamy tw. Pitagorasa dla obliczonych wartosci trojki
	    // sprawdzamy, czy suma a,b i c = 1000
	    if ( ( Math.pow(tmp_a,2) + Math.pow( tmp_b,2 ) ) == Math.pow( tmp_c, 2 ) ) {
		if ( tmp_a + tmp_b + tmp_c == 1000 ) {
		    System.out.println("znaleziona trojka: "+tmp_a+", "+tmp_b+", "+tmp_c+" suma: "+tmp_a+tmp_b+tmp_c);
		} else {
		    System.out.println(Math.pow(tmp_a,2)+", "+Math.pow(tmp_b,2)+", "+(Math.pow(tmp_a,2) + Math.pow( tmp_b,2 )));
		}
	    }//if
	}
	System.out.println();
    }
}
