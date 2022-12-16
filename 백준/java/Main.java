import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static long[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        dp = new long[N+1];
        for(int i = 1; i <= N; i++) {
            dp[i] = i;
        }

        for (int i = 5; i < N+1; i++) {
            dp[i] = i;
            for (int j = i-5; j < i-2; j++) {
                long tmp = dp[j] * (i-j-1);
                if (dp[i] < tmp) {
                    dp[i] = tmp;
                }
            }
        }

        System.out.println(dp[N]);
    }
}
