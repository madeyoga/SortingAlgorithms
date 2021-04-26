import java.util.Random;

public class SelectionSort {
    public static void selectionSort(int[] arr) {
        int temp;

        for (int i = 0; i < arr.length; i++) {
            int smallestValueIndex = i;

            for (int j = i; j < arr.length; j++) {
                if (arr[j] < arr[smallestValueIndex]) {
                    smallestValueIndex = j;
                }
            }

            // swap
            temp = arr[i];
            arr[i] = arr[smallestValueIndex];
            arr[smallestValueIndex] = temp;
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

        selectionSort(arr);
        System.out.println("\n\nSorted Array:");

        // print sorted array
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
