//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.StringTokenizer;
//
//public class Main {
//    static int T;
//    static int N;
//    static int[] inputList;
//    static int[] targetList;
//    static int[] dp;
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        N = Integer.parseInt(br.readLine());
//        inputList = new int[N];
//
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        for(int j = 0; j < N; j++) {
//            inputList[j] = Integer.parseInt(st.nextToken());
//        }
//
//        T = Integer.parseInt(br.readLine());
//        targetList = new int[T];
//
//        st = new StringTokenizer(br.readLine());
//        for(int j = 0; j < T; j++) {
//            targetList[j] = Integer.parseInt(st.nextToken());
//        }
//
//        dp = new int[40001];
//        dp[0] = -1;
//        int maxIndex = 0;
//        for (int i = 1; i <= N; i++) {
//            int num = inputList[i-1];
//            maxIndex += num;
//            for (int j = 0; j <= maxIndex; j++) {
//                if (dp[j] != i && dp[j] != 0) {
//                    if (dp[Math.abs(j-num)] == 0) {
//                        dp[Math.abs(j-num)] = i;
//                    }
//                    if (dp[j+num] == 0) {
//                        dp[j+num] = i;
//                    }
//                }
//            }
//        }
//
//        for(int num : targetList) {
//            if (dp[num] != 0) {
//                System.out.print("Y ");
//            }
//            else {
//                System.out.print("N ");
//            }
//        }
//    }
//}
