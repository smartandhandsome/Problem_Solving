package baekjoon.DFSAndBFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class B2178 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int[] size = getSize();
        int[][] map = setMap(size[0], size[1]);
        int min = BFS(map);
        System.out.println(min);
    }

    public static int BFS(int[][] map) {
        int row = map.length;
        int col = map[0].length;
        boolean[][] visited = new boolean[row][col];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int[] coordinate = queue.poll();
            if (coordinate[0] == row && coordinate[1] == col) {
                break;
            }
            for (int i = 0; i < 4; i++) {
                int[] moveCoordinate = move(coordinate, i);
                if (moveCoordinate[0] < 0 || moveCoordinate[0] >= row ||
                        moveCoordinate[1] < 0 || moveCoordinate[1] >= col) {
                    continue;
                }
                if (visited[moveCoordinate[0]][moveCoordinate[1]] ||
                        map[moveCoordinate[0]][moveCoordinate[1]] == 0) {
                    continue;
                }
                map[moveCoordinate[0]][moveCoordinate[1]] += map[coordinate[0]][coordinate[1]];
                visited[moveCoordinate[0]][moveCoordinate[1]] = true;
                queue.add(moveCoordinate);
            }
        }
        return map[row - 1][col - 1];
    }

    public static int[] move(int[] coordinate, int direction) {
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        int moveX = coordinate[0] + dx[direction];
        int moveY = coordinate[1] + dy[direction];
        return new int[]{moveX, moveY};
    }

    public static int[][] setMap(int row, int col) throws IOException {
        int[][] map = new int[row][col];
        for (int i = 0; i < row; i++) {
            String line = br.readLine();
            for (int j = 0; j < col; j++) {
                map[i][j] = Character.getNumericValue(line.charAt(j));
            }
        }
        return map;
    }

    public static int[] getSize() throws IOException {
        String[] token = br.readLine().split(" ");
        int row = Integer.parseInt(token[0]);
        int col = Integer.parseInt(token[1]);
        return new int[]{row, col};
    }
}
