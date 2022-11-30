package baekjoon.DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B11053 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int size = Integer.parseInt(br.readLine());
        String[] token = br.readLine().split(" ");
        int[] A = stringArrayToIntArray(token);
        int[] sizeOfLongestIncreasingSequence = getSizeOfLongestIncreasingSequence(A, size);
        System.out.println(getMaximum(sizeOfLongestIncreasingSequence));
    }

    public static int[] stringArrayToIntArray(String[] input) {
        int[] output = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            output[i] = Integer.parseInt(input[i]);
        }
        return output;
    }

    public static int[] initializeToOne(int size) {
        int[] output = new int[size];
        for (int i = 0; i < size; i++) {
            output[i] = 1;
        }
        return output;
    }

    public static int[] getSizeOfLongestIncreasingSequence(int[] A, int size) {
        int[] sizeOfLongestIncreasingSequence = initializeToOne(size);
        for (int i = 1; i < size; i++) {
            for (int j = 0; j < i; j++) {
                if (A[i] > A[j]) {
                    sizeOfLongestIncreasingSequence[i] = Math.max(sizeOfLongestIncreasingSequence[i], sizeOfLongestIncreasingSequence[j] + 1);
                }
            }
        }
        return sizeOfLongestIncreasingSequence;
    }

    public static int getMaximum(int[] arr) {
        int max = Integer.MIN_VALUE;
        for (int i = 0 ; i < arr.length; i++){
            if (max < arr[i]){
                max = arr[i];
            }
        }
        return max;
    }
}
