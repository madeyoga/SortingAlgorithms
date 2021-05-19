import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class MergeSort {

    public static List<Integer> mergeSort(List<Integer> list) {
        int middle = list.size() / 2;

        List<Integer> leftArray = list.subList(0, middle);
        List<Integer> rightArray = list.subList(middle, list.size());

        List<Integer> sortedLeft = leftArray;
        List<Integer> sortedRight = rightArray;

        if (leftArray.size() > 1)
            sortedLeft = mergeSort(leftArray);

        if (rightArray.size() > 1)
            sortedRight = mergeSort(rightArray);

        int leftPointer = 0;
        int rightPointer = 0;

        // merge
        List<Integer> tempMergedArray = new ArrayList<>();
        while (leftPointer < sortedLeft.size() && rightPointer < sortedRight.size()) {
            int leftValue = sortedLeft.get(leftPointer);
            int rightValue = sortedRight.get(rightPointer);

            if (leftValue < rightValue) {
                tempMergedArray.add(leftValue);
                leftPointer += 1;
            }
            else {
                tempMergedArray.add(rightValue);
                rightPointer += 1;
            }
        }

        while (leftPointer < sortedLeft.size()) {
            tempMergedArray.add(sortedLeft.get(leftPointer));
            leftPointer += 1;
        }

        while (rightPointer < sortedRight.size()) {
            tempMergedArray.add(sortedRight.get(rightPointer));
            rightPointer += 1;
        }

        return tempMergedArray;
    }

    public static void main(String[] args) {
        List<Integer> arr = new ArrayList<>();

        int nData = 25;

        Random rand = new Random();
        // Add random numbers to array list
        for (int i = 0; i < nData; i++) {
            // Generate random number from 0 to 99;
            int number = rand.nextInt(100);
            arr.add(number);
            System.out.print(arr.get(i) + " ");
        }
        System.out.println();

        List<Integer> sortedArray = mergeSort(arr);

        System.out.println("SortedArray:");
        for (int i = 0; i < sortedArray.size(); i++) {
            System.out.print(sortedArray.get(i) + " ");
        }
    }
}
