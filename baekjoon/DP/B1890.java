package baekjoon.DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B1890 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int boardSize = Integer.parseInt(br.readLine());
        int[][] board = new int[boardSize][boardSize];
        long[][] dp = new long[boardSize][boardSize];

        for (int row = 0; row < boardSize; row++) {
            String[] line = br.readLine().split(" ");
            for (int col = 0; col < boardSize; col++) {
                board[row][col] = Integer.parseInt(line[col]);
            }
        }
        dp[0][0] = 1;
        for (int i = 0; i < boardSize; i++) {
            for (int j = 0; j < boardSize; j++) {
                int jump = board[i][j];
                if (jump == 0 || dp[i][j] == 0) {
                    continue;
                }
                if (i + jump < boardSize) {
                    dp[i + jump][j] += dp[i][j];
                }
                if (j + jump < boardSize) {
                    dp[i][j + jump] += dp[i][j];
                }
            }
        }
        System.out.println(dp[boardSize - 1][boardSize - 1]);
    }
}