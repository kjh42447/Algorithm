//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.StringTokenizer;
//
//public class Main {
//    static int N;
//    static int K;
//    static int[] inputList;
//    static long[] dp;
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        N = Integer.parseInt(st.nextToken());
//        K = Integer.parseInt(st.nextToken());
//        inputList = new int[N];
//        dp = new long[K+1];
//        dp[0] = 1;
//
//        for(int i = 0; i < N; i++) {
//            inputList[i] = Integer.parseInt(br.readLine());
//        }
//
//        for (int i = 0; i < N; i++) {
//            for (int j = inputList[i]; j <= K; j++) {
//                dp[j] += dp[j - inputList[i]];
//            }
//        }
//
//        System.out.println(dp[K]);
//    }
//}
