//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.StringTokenizer;
//
//public class Main {
//    static int T;
//    static int N;
//    static int K;
//    static int[] inputList;
//    static long[] dp;
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        T = Integer.parseInt(br.readLine());
//        for (int t = 0; t < T; t++) {
//            N = Integer.parseInt(br.readLine());
//            inputList = new int[N];
//
//            StringTokenizer st = new StringTokenizer(br.readLine());
//            for(int j = 0; j < N; j++) {
//                inputList[j] = Integer.parseInt(st.nextToken());
//            }
//
//            K = Integer.parseInt(br.readLine());
//            dp = new long[K+1];
//            dp[0] = 1;
//
//            for (int i = 0; i < N; i++) {
//                for (int j = inputList[i]; j <= K; j++) {
//                    dp[j] += dp[j - inputList[i]];
//                }
//            }
//
//            System.out.println(dp[K]);
//        }
//    }
//}
