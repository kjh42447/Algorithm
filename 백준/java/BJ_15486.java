//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.StringTokenizer;
//
//public class Main {
//    static int N;
//    static int[][] inputList;
//    static long[] dp;
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        N = Integer.parseInt(br.readLine());
//        inputList = new int[2][N];
//        dp = new long[N+1];
//        for(int i = 0; i < N; i++) {
//            StringTokenizer st = new StringTokenizer(br.readLine());
//            inputList[0][i] = Integer.parseInt(st.nextToken());
//            inputList[1][i] = Integer.parseInt(st.nextToken());
//        }
//
//        for (int i = N-1; i >= 0; i--) {
//            dp[i] = dp[i+1];
//            if (inputList[0][i] + i <= N) {
//                long tmp = dp[inputList[0][i] + i] + inputList[1][i];
//                if (dp[i+1] < tmp) {
//                    dp[i] = tmp;
//                }
//            }
//        }
//
//        System.out.println(dp[0]);
//    }
//}
