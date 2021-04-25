import java.util.Random;

public class BubbleSort {

    public static void bubbleSort(int[] arr) {
        int temp;
        for (int i = 0; i < arr.length; i++) {
            for (int j = i; j < arr.length; j++) {
                if (arr[i] > arr[j]) {
                    // swap
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[25];

        // Generate random array
        Random rand = new Random();

        // Add random numbers to array
        for (int i = 0; i < arr.length; i++) {
            // Generate random number from 0 to 99;
            int number = rand.nextInt(100);
            arr[i] = number;
            System.out.print(arr[i] + " ");
        }

        bubbleSort(arr);
        System.out.println("\nSorted Array: ");
        
        // print sorted array
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
