/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package euler;

/**
 *
 * @author rafal
 */
public class Euler {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int start = 1;
        int stop = 10;

        for (int y = stop; y <= 100; y++) {
            int sum = 0;
            int squareOfTheSum = 0;
            int sumOfTheSquares = 0;

            for (int i = start; i <= y; i++) {
                squareOfTheSum = squareOfTheSum + (int) Math.pow(i, 2);
                sum += i;
            }//for
            sumOfTheSquares = (int) Math.pow(sum, 2);

            System.out.println("zakres: " + start + " do " + y + "\tsuma kwadratów: "
                    + sumOfTheSquares + "\tkwadrat sum: " + squareOfTheSum + "\t\tróżnica: " + (sumOfTheSquares - squareOfTheSum));
        }
    }
}
