import java.util.Random;

public class InsertionSort {
    public static void insertionSort(int[] arr) {
        int temp;
        for (int i = 0; i < arr.length; i++) {
            int currentKey = arr[i];
            for (int j = i - 1; j >= 0; j--) {
                if (currentKey < arr[j]) {
                    // swap
                    temp = arr[j + 1];
                    arr[j + 1] = arr[j];
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

        insertionSort(arr);
        System.out.println("\n\nSorted Array:");

        // print sorted array
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
