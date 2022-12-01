package baekjoon.Greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B1931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int numsMeeting = Integer.parseInt(br.readLine());
        List<Meeting> meetings = new ArrayList<>();
        for (int i = 0; i < numsMeeting; i++) {
            String[] token = br.readLine().split(" ");
            meetings.add(makeMeeting(token));
        }
        Collections.sort(meetings);
        int answer = maxNumsMeeting(meetings);
        System.out.println(answer);
    }

    public static Meeting makeMeeting(String[] input) {
        int start = Integer.parseInt(input[0]);
        int end = Integer.parseInt(input[1]);
        return new Meeting(start, end);
    }

    public static int maxNumsMeeting(List<Meeting> meetings) {
        int numsMeeting = 0;
        int lastMeeting = 0;
        for (Meeting meeting : meetings) {
            if (lastMeeting <= meeting.start) {
                numsMeeting++;
                lastMeeting = meeting.end;
            }
        }
        return numsMeeting;
    }
}

class Meeting implements Comparable<Meeting> {
    int start;
    int end;

    Meeting(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public int compareTo(Meeting another) {
        if (this.end == another.end) {
            return this.start - another.start;
        }
        return this.end - another.end;
    }
}