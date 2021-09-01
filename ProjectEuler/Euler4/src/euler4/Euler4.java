/*
 *A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

 Find the largest palindrome made from the product of two 3-digit numbers.
 */
package euler4;

/**
 *
 * @author blade
 */
public class Euler4 {

    public static Integer digit;
    public static boolean palindrome;
        
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

	int x;
	int tmp = 0, max = 0;
	int z, a = 999, b = 999;

	for (z = a; z > 0; z--) {
	    int y;
	    for (y = b; y > 0; y--) {
		digit = z * y;
		String dig = digit.toString();
		Euler4.palindrome = true;
		if (dig.length() % 2 == 0) {
		    for (x = 0; x < dig.length(); x++) {
			if (dig.charAt(x) != dig.charAt(dig.length() - x - 1)) {
			    Euler4.palindrome = false;
			    break;
			}//if


		    }//
		    if (Euler4.palindrome) {
			max = ( digit > max ) ? digit : max;
		    }
		}//if
	    }// for
	}//for
	System.out.println(max);
    }
}
